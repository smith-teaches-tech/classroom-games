#!/usr/bin/env python3
# Run from anywhere:  python3 extended-essay/_build/build_subjects.py
"""Builds extended-essay/subjects/ (index + one page per subject) from the JSON files in _build/hubs/.
Content in the JSON comes from the IB Extended essay guide (first assessment 2027), with page references.
Source targets come from build_steps.SOURCE_GROUPS so the numbers stay identical to steps 7 and 9."""
import os, json, html, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "subjects")
spec = importlib.util.spec_from_file_location("bs", os.path.join(HERE, "build_steps.py"))
bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)
TARGETS = {g: (c, a) for g, _, c, a, _ in bs.SOURCE_GROUPS}
GROUP_OF = {"language-a": "lang", "language-b": "lang", "visual-arts": "va", "mathematics": "math"}  # everything else: "big"

# Order and grouping on the index page (the guide's groups; ASD subjects only)
ORDER = [
 ("Studies in language and literature", ["language-a"]),
 ("Language acquisition", ["language-b"]),
 ("Individuals and societies", ["business-management", "economics", "global-politics"]),
 ("Sciences", ["biology", "chemistry", "physics"]),
 ("Mathematics", ["mathematics"]),
 ("The arts", ["visual-arts"]),
]
BLURB = {
 "language-a": "Close analysis of a literary or language text, supported by literary criticism.",
 "language-b": "The language, culture or literature of the language you're learning, studied through texts first written in that language.",
 "business-management": "A real organisation or business issue, analysed with business management tools and theory.",
 "economics": "An economic theory tested against real evidence, often in one place and time period.",
 "global-politics": "A political issue or case, analysed through the main political concepts and academic sources.",
 "biology": "A biology experiment (or similar published data) with controlled variables and a standardised method.",
 "chemistry": "A chemistry investigation (or similar published data) with controlled variables and a standardised method.",
 "physics": "A physics investigation (or similar published data) with controlled variables and a standardised method.",
 "mathematics": "Mathematics beyond the syllabus, or mathematics used to model or analyse data. A literature review is required.",
 "visual-arts": "Analysis of a small body of artworks in their context, supported by art history and criticism. Images are required.",
}
SAMPLE_NAME = {"interdisciplinary": "Interdisciplinary"}  # data/samples.js subject name when it differs from the hub's subject name

SCIENCE_NOTE = ("<b>At ASD:</b> your science EE should use primary (experimental) data. "
                "The IB allows science essays based on secondary data, but EE workshop guidance says secondary-data essays rarely reach the top mark bands.")
PRIMARY_NOTE = {
 "lang": "Your primary text (the novel, play, poems, films or songs you analyse) counts towards your Collect target. Annotate your secondary sources.",
 "va": "The 3 or 4 artworks your essay analyses count towards your Collect target. Annotate your secondary sources.",
}

e = html.escape
def ul(items, cls=""):
    return '<ul%s>%s</ul>' % (' class="%s"' % cls if cls else "", "".join("<li>%s</li>" % e(i) for i in items))
def pg(refs, key):
    p = (refs or {}).get(key)
    return ' <span class="pg">(guide p. %s)</span>' % e(str(p)) if p else ""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | EE Subject Guides</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{up}shared/ee.css">
<link rel="stylesheet" href="{up}shared/steps.css">
<style>
.pg{{font-size:13.5px;color:var(--muted);font-weight:400}}
.glance{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:0 0 8px}}
.glance .panel{{padding:14px 16px}}
.glance .k{{font-size:12.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--stud);margin:0 0 4px}}
.glance p{{margin:0}}
.samples-list{{list-style:none;padding:0;margin:0;display:grid;gap:8px}}
.samples-list li{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px}}
.samples-list .gr{{display:inline-block;min-width:26px;text-align:center;font-weight:700;border-radius:6px;background:var(--stud-soft);color:var(--stud);margin-right:8px}}
.subjgroup{{margin-top:28px}}
.subjgroup h2{{font-size:20px;margin-bottom:10px}}
.tile.mine{{border-color:var(--stud);box-shadow:0 0 0 2px var(--stud-soft)}}
</style>
</head>
<body{bodyattr}>
<div class="shell narrow">
  <div class="top">
    <a class="mark" href="{up}" title="Extended Essay hub">EE</a>
    <nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>
  </div>
  <header class="hero">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </header>
  <main class="step-body">
{body}
  </main>
  <footer><a href="{back_href}">{back_text}</a></footer>
</div>
{scripts}
</body>
</html>
"""

def crumbs(up, last, mid=None):
    c = ['<a href="%s../">Classroom tools</a>' % up, '<a href="%s">Extended Essay</a>' % up]
    if mid: c.append(mid)
    c.append("<span>%s</span>" % e(last))
    return '<span class="sep">/</span>'.join(c)

def samples_block(sample_subject, slug):
    return """
    <h2>Sample essays in {s}</h2>
    <p>IB sample essays with the examiner's marks. The letter grades are estimates until the IB publishes the official 2027 grade boundaries.</p>
    <ul class="samples-list" id="samples"></ul>
    <p><a class="btn" href="../../samples/?subject={q}">Open all {s} samples</a></p>""".format(s=e(sample_subject), q=e(sample_subject).replace(" ", "%20"))

SAMPLES_JS = """<script src="../../data/samples.js"></script>
<script>
(function(){
  var subj = %s, ul = document.getElementById("samples"); if(!ul) return;
  function letter(t,o){ if(t==null) return "?"; var b=window.EE_BOUNDARIES[o]; for(var i=0;i<b.length;i++){ if(t>=b[i][1]) return b[i][0]; } return "E"; }
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  var list = (window.EE_SAMPLES||[]).filter(function(s){ return s.subject===subj; });
  list.sort(function(a,b){ return (b.total==null?-1:b.total/b.outOf) - (a.total==null?-1:a.total/a.outOf); });
  if(!list.length){ ul.outerHTML = '<p class="muted">There are no IB sample essays in this subject yet. Use the sample essays in a related subject, and the examples above.</p>'; return; }
  ul.innerHTML = list.map(function(s){
    var g = letter(s.total, s.outOf), mark = s.total==null ? "mark in the examiner comments" : s.total+"/"+s.outOf+(s.outOf===34?" (previous rubric)":"");
    return '<li><span class="gr">'+g+'</span><span class="small muted">'+esc(mark)+'</span><br>'+esc(s.rq)+'</li>';
  }).join("");
})();
</script>""" 

def tool_def(slug, subject, think):
    prompts = [{"id": "topic", "type": "text", "label": "My idea or broad topic right now:", "prefill": "__PREFILL_TOPIC__"}]
    prompts += [{"id": "q%d" % (i + 1), "type": "long", "label": q, "rows": 3} for i, q in enumerate(think)]
    prompts.append({"id": "verdict", "type": "choice", "label": "Now that I've answered these questions, I think %s is:" % subject,
                    "options": ["A strong fit for my idea", "Possible, but I need to check with a teacher", "Probably not the right subject for this idea"]})
    d = {"id": "hub-" + slug, "stepLabel": "Subject guide · " + subject, "title": "Is %s right for my idea?" % subject,
         "intro": "Your answers are private to you. Use these questions to test your idea against what the guide expects in %s. Then copy your answers into your RRS (researcher's reflection space: your own EE notebook)." % subject,
         "sections": [{"heading": "Test my idea", "prompts": prompts}]}
    s = json.dumps(d, ensure_ascii=False, indent=1)
    return s.replace('"__PREFILL_TOPIC__"', bs.PREFILLS["__PREFILL_TOPIC__"])

def subject_page(d):
    slug, subject = d["slug"], d["subject"]
    refs = d.get("refs", {})
    grp = GROUP_OF.get(slug, "big")
    c, a = TARGETS[grp]
    sample_subject = SAMPLE_NAME.get(slug, subject)
    b = []
    b.append('    <div class="glance">'
             '<div class="panel"><p class="k">In the guide</p><p>%s, pages %s</p></div>'
             '<div class="panel"><p class="k">Source targets</p><p>Collect %d · annotate %d</p></div>'
             '<div class="panel"><p class="k">Sample essays</p><p><a href="#samples-h">See below</a></p></div></div>'
             % (e(d.get("group", "")), e(d.get("pages", "")), c, a))
    if grp in PRIMARY_NOTE:
        b.append('    <p class="small muted">%s</p>' % e(PRIMARY_NOTE[grp]))
    b.append("    <h2>What makes a %s EE different%s</h2>" % (e(subject), pg(refs, "distinctive")))
    b += ["    <p>%s</p>" % e(p) for p in d["distinctive"]]
    b.append("    <h2>Primary and secondary sources%s</h2>" % pg(refs, "sources"))
    b.append('    <div class="kv"><div class="panel"><h3>Primary</h3><p>%s</p></div><div class="panel"><h3>Secondary</h3><p>%s</p></div></div>'
             % (e(d["sources"]["primary"]), e(d["sources"]["secondary"])))
    if slug in ("biology", "chemistry", "physics"):
        b.append('    <div class="note"><p style="margin:0">%s</p></div>' % SCIENCE_NOTE)
    b.append("    <h2>How researchers in %s answer questions%s</h2>" % (e(subject), pg(refs, "methods")))
    b.append("    " + ul(d["methods"]))
    b.append("    <h2>Choosing a topic%s</h2>" % pg(refs, "choosing_topic"))
    b.append("    " + ul(d["choosing_topic"]))
    if d.get("examples"):
        b.append("    <h2>Examples from the guide</h2>")
        rows = "".join('<tr><td><b>%s</b>%s</td><td>%s <span class="pg">(p. %s)</span></td></tr>'
                       % (e(x.get("topic", "")), ("<br><i>%s</i>" % e(x["rq"])) if x.get("rq") else "", e(x.get("why", "")), e(str(x.get("page", "")))) for x in d["examples"])
        b.append('    <div class="tablewrap"><table class="info"><thead><tr><th>Topic and research question</th><th>Why it works</th></tr></thead><tbody>%s</tbody></table></div>' % rows)
    b.append("    <h2>How the essay is usually built%s</h2>" % pg(refs, "structure"))
    b.append("    " + ul(d["structure"]))
    b.append("    <h2>Common problems to avoid%s</h2>" % pg(refs, "pitfalls"))
    b.append("    " + ul(d["pitfalls"]))
    if d.get("rules"):
        b.append('    <div class="note warn"><p style="margin:0 0 6px"><b>Rules for %s EEs</b>%s</p>%s</div>' % (e(subject), pg(refs, "rules"), ul(d["rules"])))
    b.append('    <div id="samples-h"></div>' + samples_block(sample_subject, slug))
    b.append('    <div data-tool="hub-%s"></div>' % slug)
    b.append('    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Subject-specific guidance": %s, pages %s. Source targets: ASD, based on an analysis of strong EEs (IB sample essays graded B or higher).</p>' % (e(subject), e(d.get("pages", ""))))
    scripts = SAMPLES_JS % json.dumps(sample_subject) + """
<script src="../../shared/thinking-tools.js"></script>
<script>
EETools.define(%s);
</script>""" % tool_def(slug, subject, d["think"])
    return PAGE.format(title=e(subject), desc=e("What an Extended Essay in %s needs: sources, methods, topics, examples and pitfalls from the IB guide." % subject),
                       up="../../", bodyattr="", crumbs=crumbs("../../", subject, '<a href="../">Subject guides</a>'),
                       eyebrow="Subject guide", h1=e(subject) + " EE", lede=e("What the IB expects from an Extended Essay in %s, and how to test whether your idea fits." % subject),
                       body="\n".join(b), back_href="../", back_text="← All subject guides", scripts=scripts)

def interdisciplinary_page(d):
    refs = d.get("refs", {})
    c, a = TARGETS["big"]
    b = []
    b.append('    <div class="glance"><div class="panel"><p class="k">In the guide</p><p>The interdisciplinary pathway, pages %s</p></div>'
             '<div class="panel"><p class="k">Source targets</p><p>Collect %d · annotate %d</p></div>'
             '<div class="panel"><p class="k">Sample essays</p><p><a href="#samples-h">See below</a></p></div></div>' % (e(d.get("pages", "")), c, a))
    b.append("    <h2>What an interdisciplinary EE is%s</h2>" % pg(refs, "distinctive"))
    b += ["    <p>%s</p>" % e(p) for p in d["distinctive"]]
    b.append("    <h2>Interdisciplinary or subject-focused?%s</h2>" % pg(refs, "when_to_choose"))
    b.append("    " + ul(d["when_to_choose"]))
    b.append("    <h2>The five frameworks</h2>")
    b.append('    <div class="tablewrap"><table class="info"><thead><tr><th>Framework</th><th>What it covers</th></tr></thead><tbody>%s</tbody></table></div>'
             % "".join('<tr><th>%s</th><td>%s <span class="pg">(p. %s)</span></td></tr>' % (e(f["name"]), e(f["summary"]), e(str(f.get("page", "")))) for f in d["frameworks"]))
    if d.get("subjects_rules"):
        b.append('    <div class="note warn"><p style="margin:0 0 6px"><b>Rules about subjects</b>%s</p>%s</div>' % (pg(refs, "subjects_rules"), ul(d["subjects_rules"])))
    b.append("    <h2>Developing an interdisciplinary research question%s</h2>" % pg(refs, "developing_rq"))
    b.append("    " + ul(d["developing_rq"]))
    if d.get("examples"):
        b.append("    <h2>Examples from the guide</h2>")
        rows = "".join('<tr><td><b>%s</b><br><i>%s</i><br><span class="small muted">%s · %s</span></td><td>%s <span class="pg">(p. %s)</span></td></tr>'
                       % (e(x.get("topic", "")), e(x.get("rq", "")), e(x.get("subjects", "")), e(x.get("framework", "")), e(x.get("why", "")), e(str(x.get("page", "")))) for x in d["examples"])
        b.append('    <div class="tablewrap"><table class="info"><thead><tr><th>Topic and research question</th><th>Why it works</th></tr></thead><tbody>%s</tbody></table></div>' % rows)
    b.append("    <h2>Integrating the two subjects%s</h2>" % pg(refs, "integration"))
    b.append("    " + ul(d["integration"]))
    b.append("    <h2>Common problems to avoid%s</h2>" % pg(refs, "pitfalls"))
    b.append("    " + ul(d["pitfalls"]))
    if d.get("supervision"):
        b.append("    <h2>Supervision%s</h2>" % pg(refs, "supervision"))
        b.append("    " + ul(d["supervision"]))
    b.append('    <div id="samples-h"></div>' + samples_block("Interdisciplinary", "interdisciplinary"))
    b.append('    <div data-tool="hub-interdisciplinary"></div>')
    b.append('    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "The interdisciplinary pathway", pages %s. Source targets: ASD, based on an analysis of strong EEs (IB sample essays graded B or higher).</p>' % e(d.get("pages", "")))
    scripts = SAMPLES_JS % json.dumps("Interdisciplinary") + """
<script src="../../shared/thinking-tools.js"></script>
<script>
EETools.define(%s);
</script>""" % tool_def("interdisciplinary", "the interdisciplinary pathway", d["think"])
    return PAGE.format(title="Interdisciplinary pathway", desc=e("What an interdisciplinary Extended Essay needs: the five frameworks, choosing two subjects, research questions and examples from the IB guide."),
                       up="../../", bodyattr="", crumbs=crumbs("../../", "Interdisciplinary", '<a href="../">Subject guides</a>'),
                       eyebrow="Subject guide", h1="Interdisciplinary EE", lede="Two DP subjects and one of the IB's five frameworks, working together on one research question.",
                       body="\n".join(b), back_href="../", back_text="← All subject guides", scripts=scripts)

def index_page(hubs):
    b = ['    <div class="note"><p style="margin:0">Your subject choice and one backup subject are due on the date in the EE calendar. Read the subject guide for your first choice <b>and</b> for your backup. Then use the thinking tool at the bottom of each subject guide to test your idea.</p></div>',
         '    <p class="small muted" id="mine-note" hidden>Your subject from step 1 is highlighted.</p>']
    for gname, slugs in ORDER:
        tiles = []
        for s in slugs:
            if s not in hubs: continue
            d = hubs[s]
            tiles.append('<a class="tile live" data-subject="%s" href="%s/"><h3>%s</h3><p>%s</p></a>'
                         % (e(d["subject"]), s, e(d["subject"]), e(BLURB.get(s, ""))))
        if tiles:
            b.append('    <section class="subjgroup"><h2>%s</h2><div class="grid2">%s</div></section>' % (e(gname), "".join(tiles)))
    if "interdisciplinary" in hubs:
        b.append('    <section class="subjgroup"><h2>Two subjects</h2><div class="grid2"><a class="tile live" data-subject="Interdisciplinary" href="interdisciplinary/"><h3>Interdisciplinary EE</h3><p>Two DP subjects and one of the five frameworks, working on one research question.</p></a></div></section>')
    b.append('    <p class="small muted" style="margin-top:24px">Writing your EE in another subject? Ask the EE coordinator first, then read that subject\'s section of the IB <i>Extended essay guide</i>. The <a href="../samples/">sample essays</a> include History, Psychology, ESS and Design Technology.</p>')
    script = """<script src="../shared/thinking-tools.js"></script>
<script>
(function(){
  var p = EETools.read("step-1","pathway")||"", s = p==="Subject-focused (one subject)" ? (EETools.read("step-1","subject")||"") : (p==="Interdisciplinary (two subjects)" ? "Interdisciplinary" : "");
  var t = s && document.querySelector('.tile[data-subject="'+s+'"]');
  if(t){ t.classList.add("mine"); document.getElementById("mine-note").hidden=false; }
})();
</script>"""
    return PAGE.format(title="Subject guides", desc="What an Extended Essay needs in each ASD subject, from the IB guide.", up="../", bodyattr="",
                       crumbs=crumbs("../", "Subject guides"), eyebrow="For Students", h1="Subject guides",
                       lede="What the IB expects from an Extended Essay in each subject you can choose at ASD. Read these subject guides before you choose your subject.",
                       body="\n".join(b), back_href="../", back_text="← Extended Essay hub", scripts=script)

def build():
    hubs = {}
    for f in sorted(glob.glob(os.path.join(HERE, "hubs", "*.json"))):
        data = json.load(open(f, encoding="utf-8"))
        for d in (data if isinstance(data, list) else [data]):
            hubs[d["slug"]] = d
    os.makedirs(ROOT, exist_ok=True)
    for slug, d in hubs.items():
        os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
        out = interdisciplinary_page(d) if slug == "interdisciplinary" else subject_page(d)
        open(os.path.join(ROOT, slug, "index.html"), "w", encoding="utf-8").write(out)
        print("wrote subjects/%s/index.html" % slug)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(index_page(hubs))
    print("wrote subjects/index.html")

if __name__ == "__main__":
    build()
