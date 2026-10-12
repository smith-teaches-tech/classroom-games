#!/usr/bin/env python3
# Run from anywhere:  python3 extended-essay/_build/build_steps.py   (rewrites students/step-0 … step-7). The leading underscore keeps this folder off GitHub Pages.
"""Builds extended-essay/students/step-N/index.html for the live steps.
Content lives in STEPS below. Output is plain HTML that can also be edited by hand."""
import os, json, html

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "students")

ASD_SUBJECTS = ["Language A", "Language B", "Visual Arts", "Biology", "Chemistry", "Physics",
                "Business Management", "Economics", "Global Politics", "Mathematics"]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title} — EE for Students</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../../shared/ee.css">
<link rel="stylesheet" href="../../shared/steps.css">
</head>
<body data-step="{n}">
<div class="shell narrow">
  <div class="top">
    <a class="mark" href="../../" title="Extended Essay hub">EE</a>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="../../../">Classroom tools</a><span class="sep">/</span><a href="../../">Extended Essay</a><span class="sep">/</span><a href="../">For Students</a><span class="sep">/</span><span>{crumb}</span></nav>
  </div>

  <header class="hero">
    <p class="stepno" id="stepno"></p>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
  </header>

  <main class="step-body">
{body}

    <div data-tool="step-{n}"></div>

    <nav class="stepnav" id="stepnav" aria-label="Steps"></nav>
  </main>

  <footer><a href="../">← All steps</a></footer>
</div>

<script src="../../data/steps.js"></script>
<script src="../../shared/step-nav.js"></script>
<script src="../../shared/thinking-tools.js"></script>
<script>
{script}
EETools.define({tool});
</script>
</body>
</html>
"""

def tool_js(d):
    # json for data; functions (prefill) are injected as raw JS via placeholders
    s = json.dumps(d, ensure_ascii=False, indent=1)
    for k, v in PREFILLS.items():
        s = s.replace('"%s"' % k, v)
    return s

PREFILLS = {
    "__PREFILL_SUBJECT__": 'function(){ var p=EETools.read("step-1","pathway"); if(p==="Interdisciplinary (two subjects)"){ var a=EETools.read("step-1","sub1")||"", b=EETools.read("step-1","sub2")||""; return (a||b)?"Interdisciplinary: "+[a,b].filter(Boolean).join(" + "):"Interdisciplinary"; } if(p==="Subject-focused (one subject)"){ return EETools.read("step-1","subject")||""; } return ""; }',
    "__PREFILL_STYLE__": 'function(){ return EETools.read("step-2","style")||""; }',
    "__PREFILL_TOPIC__": 'function(){ return EETools.read("step-1","chosen")||""; }',
}

def checklist(items):
    return {"heading": "Before you move on", "prompts": [{"id": "done", "type": "checklist", "label": "Tick each one when it is true.", "items": items}]}

STEPS = []

# ───────────────────────── STEP 0 ─────────────────────────
STEPS.append(dict(
 n=0, crumb="Start here", title="Start here",
 desc="What the IB Extended Essay is, how the steps on this site work, and how to set up your RRS.",
 lede="What the extended essay is, how this site works, and the one document you need before you begin.",
 body="""
    <h2>What the extended essay is</h2>
    <p class="why">The extended essay (EE) is a piece of independent research on a question you choose. You investigate it, then write up your findings as a formal academic essay.</p>
    <div class="kv">
      <div class="panel"><h3>4,000 words maximum</h3><p>Examiners stop reading at 4,000 words, so anything after that point is not marked.</p></div>
      <div class="panel"><h3>One subject or two</h3><p>A subject-focused essay uses one DP subject. An interdisciplinary essay combines two DP subjects through one of five frameworks.</p></div>
      <div class="panel"><h3>Three reflection sessions</h3><p>You meet your supervisor three times: a first session, an interim session, and a final session called the viva voce.</p></div>
      <div class="panel"><h3>A 500-word reflective statement</h3><p>Written after the viva voce on the Reflection and Progress Form (RPF), and marked under Criterion E.</p></div>
    </div>
    <p>IB examiners mark the essay out of 30 across five criteria (A Framework for the essay, B Knowledge and understanding, C Analysis and line of argument, D Discussion and evaluation, E Reflection). The mark becomes a grade from A to E. Your EE grade and your TOK grade together earn up to three points towards your diploma, and a grade E in the EE is a failing condition.</p>

    <h2>How the core fits together</h2>
    <div class="kv">
      <div class="panel"><h3>CAS</h3><p>Shows you what you care about — often the best source of an EE topic.</p></div>
      <div class="panel"><h3>TOK</h3><p>Gives you the questioning: what counts as evidence in a subject, and which methods it trusts.</p></div>
      <div class="panel"><h3>Your subjects</h3><p>Give you the knowledge, concepts and terminology.</p></div>
      <div class="panel"><h3>The EE</h3><p>Is where you put all three together, on your own question.</p></div>
    </div>

    <h2>How this site works</h2>
    <p>There are 18 steps in four stages: Explore, Narrow, Research and write, and After submission. Do them in order. Each step page has:</p>
    <ul>
      <li><b>Why this step matters</b> and <b>what to do</b>, in a short guide.</li>
      <li><b>A thinking tool</b> — questions that help you brainstorm. Nothing is submitted or graded. Your answers save in your browser, and a button copies them into your RRS Google Doc.</li>
      <li><b>Before you move on</b> — a short checklist at the end of the thinking tool.</li>
    </ul>
    <p>Your extended essay is your own independent work. The thinking tools only ask questions; they never write anything for you.</p>

    <h2>Set up your RRS before anything else</h2>
    <p>The IB strongly recommends that every EE student keeps a <b>researcher's reflection space (RRS)</b>: a place to record what you read, what you think, the questions that come up, and the decisions you make. You will use your RRS to prepare for each reflection session, and it is the best source for your reflective statement at the end.</p>
    <ol class="do">
      <li>Create a Google Doc called <b>EE RRS — your name</b>.</li>
      <li>Add a heading for today's date, then copy the thinking tool below into the Google Doc with the <b>Copy for Google Docs</b> button.</li>
      <li>Do the same at every step. Add your own notes in between — reactions to sources, new questions, things you changed your mind about.</li>
    </ol>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Reflection and the extended essay" and "Assessment".</p>
""",
 tool=dict(id="step-0", stepLabel="Start here", title="Who are you as a researcher?",
  intro="Answer quickly and honestly. You are looking for patterns in what already interests you — the topic often hides in here.",
  sections=[
   {"heading":"You as a thinker","prompts":[
     {"id":"questions","type":"long","label":"What questions do you keep coming back to — in class, online, or with friends?","rows":3},
     {"id":"argue","type":"long","label":"What have you argued about this year? What side were you on, and why?","rows":3},
     {"id":"flow","type":"text","label":"In which class does time disappear for you?"}]},
   {"heading":"You as a doer","prompts":[
     {"id":"cas","type":"long","label":"Which CAS experiences mattered most to you? What did they make you curious about?","rows":3},
     {"id":"hobby","type":"long","label":"What do you make, fix, play, collect, follow or practise outside school?","rows":3}]},
   {"heading":"You as a researcher","prompts":[
     {"id":"lookedup","type":"long","label":"What have you looked up recently just because you wanted to know?","rows":3},
     {"id":"subjects","type":"multi","label":"Which of these DP subjects do you study?","options":ASD_SUBJECTS},
     {"id":"pattern","type":"long","label":"Look back over your answers. What pattern do you notice? Write two or three possible areas you could research.","rows":3}]},
   checklist(["I know the EE has a 4,000-word limit and three reflection sessions.",
              "I have created my RRS Google Doc.",
              "I have copied this thinking tool into my RRS."])
  ])
))

# ───────────────────────── STEP 1 ─────────────────────────
STEPS.append(dict(
 n=1, crumb="Step 1", title="Choose a subject and a broad topic",
 desc="Choose a broad EE topic, pick the subject-focused or interdisciplinary pathway, and check your subject fits.",
 lede="Start with something you genuinely care about, then decide which subject — or which two subjects — will study it.",
 body="""
    <h2>Why this step matters</h2>
    <p class="why">You will live with this topic for more than a year. The IB guide calls choosing a topic "arguably the most important stage" of the extended essay, because it drives everything that follows.</p>
    <p>At this stage you only need a <b>broad topic</b> — an area such as "sport and national identity" or "water use in desert cities". You will narrow it into a research question later, in steps 8 to 10.</p>

    <h2>One topic, several subjects</h2>
    <p>The same broad topic can become very different essays depending on the subject that studies it. The IB guide uses sport as an example:</p>
    <div class="tablewrap"><table class="info">
      <thead><tr><th>Subject</th><th>How that subject might approach sport</th></tr></thead>
      <tbody>
        <tr><th>Global Politics</th><td>Explore global discourses around women in sport and how these influence political decisions about gender rights.</td></tr>
        <tr><th>Business Management</th><td>Analyse a case study of a brand sponsoring a football club.</td></tr>
      </tbody></table></div>
    <p>What makes an essay belong to a subject is not the content but the <b>concepts, methods and theories</b> of that subject that you use to investigate it.</p>

    <h2>Choose your pathway</h2>
    <div class="kv">
      <div class="panel"><h3>Subject-focused pathway</h3><p>One DP subject. The IB strongly recommends a subject you are already studying in the DP, so you can build on concepts and methods you know.</p></div>
      <div class="panel"><h3>Interdisciplinary pathway</h3><p>Two DP subjects combined, positioned within one of the five interdisciplinary frameworks. The IB strongly recommends that you study at least one of the two subjects.</p></div>
    </div>
    <p><b>The five interdisciplinary frameworks</b>, with some of the IB's suggested topic areas:</p>
    <ul>
      <li><b>Power, equality, justice</b> — health, education, racism, gender, poverty, fairness, conflict.</li>
      <li><b>Culture, identity, expression</b> — belief systems, the politics of identity, sporting competitions, art and science, music, protests, cultural heritage, gaming.</li>
      <li><b>Movement, time, space</b> — migration, refugees, virtual communities, astronomy, urbanism, social media, globalization, museums.</li>
      <li><b>Evidence, measurement, innovation</b> — art and science, literature and science, mathematics in science, gaming, social media.</li>
      <li><b>Sustainability, development, change</b> — environmental, social and economic sustainability; economic and social development; food; health; poverty.</li>
    </ul>
    <p>Your topic only needs to fit one framework broadly, and it does not need to touch every word in the framework's name. The two subjects do not need an even 50/50 balance — the balance depends on your research question.</p>
    <div class="note warn"><p style="margin:0"><b>Rule:</b> Environmental Systems and Societies (ESS) and Literature and Performance are "cross-disciplinary" subjects. You can write a subject-focused essay in either one, but you cannot use either one in the interdisciplinary pathway.</p></div>

    <h2>Rules to know for your subject</h2>
    <ul>
      <li><b>Language A:</b> the essay must be based on one or more clearly defined texts, and at least one text must have been originally written in the language of the essay. You cannot base it on a text studied as part of your language and literature course. Avoid biographical, historical or sociological topics — the focus must be literary or language analysis.</li>
      <li><b>Language B:</b> you cannot write it in a language you study as Language A. Every text you analyse must have been originally written or spoken in the target language — translations are not accepted.</li>
      <li><b>Visual Arts:</b> the essay must stay on artistic meaning and analysis; do not drift into psychology, history or sociology, or treat artworks as documentary evidence.</li>
      <li><b>Mathematics:</b> the essay can be theoretical (mathematics beyond the syllabus) or practical (using mathematics to investigate an issue or data). A review of the literature is always required.</li>
      <li><b>Every subject:</b> your EE must not duplicate any other work you submit for the diploma, such as an internal assessment (IA).</li>
    </ul>

    <h2>Check: is this really your subject?</h2>
    <p>Before you go further, make sure the topic belongs to the subject you are choosing. Ask yourself which concepts, theories and methods from that subject you would use. If you cannot name any, the topic may belong to a different subject. Changing subject later costs you time and may involve a fee, so talk to the EE coordinator if you are unsure.</p>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Overview of extended essay pathways", "Generic guidance" and "Subject-specific guidance".</p>
""",
 tool=dict(id="step-1", stepLabel="Step 1 · Choose a subject and a broad topic", title="Take your idea for a walk",
  intro="Brainstorm widely first, then choose. Use your answers from Start here if you completed it.",
  sections=[
   {"heading":"Three possible broad topics","prompts":[
     {"id":"topics","type":"table","label":"List three broad topics you could research.","columns":["Broad topic","Why I care about it","Which subject(s) could study it","What would that subject ask about it?"],"rows":3,"max":6}]},
   {"heading":"Your choice","prompts":[
     {"id":"chosen","type":"text","label":"The broad topic I am going to explore first:"},
     {"id":"q1","type":"long","label":"What aspect or issue within this broad topic really interests me?","rows":3},
     {"id":"pathway","type":"choice","label":"Which pathway fits this topic best right now?","options":["Subject-focused (one subject)","Interdisciplinary (two subjects)","Not sure yet"]},
     {"id":"subject","type":"choice","label":"Which subject?","options":ASD_SUBJECTS+["Another subject"],"showIf":{"id":"pathway","equals":"Subject-focused (one subject)"}},
     {"id":"whysf","type":"long","label":"Why is a subject-focused approach appropriate for my topic?","rows":3,"showIf":{"id":"pathway","equals":"Subject-focused (one subject)"}},
     {"id":"sub1","type":"text","label":"First subject:","showIf":{"id":"pathway","equals":"Interdisciplinary (two subjects)"}},
     {"id":"sub2","type":"text","label":"Second subject:","showIf":{"id":"pathway","equals":"Interdisciplinary (two subjects)"}},
     {"id":"framework","type":"choice","label":"Which framework best suits my topic?","options":["Power, equality, justice","Culture, identity, expression","Movement, time, space","Evidence, measurement, innovation","Sustainability, development, change"],"showIf":{"id":"pathway","equals":"Interdisciplinary (two subjects)"}},
     {"id":"whyid","type":"long","label":"Why does my topic need both subjects? What would each one add that the other cannot?","rows":3,"showIf":{"id":"pathway","equals":"Interdisciplinary (two subjects)"}},
     {"id":"stretch","type":"long","label":"How can I challenge myself and expand my thinking beyond what we have covered in class?","rows":3}]},
   {"heading":"Is this really my subject?","prompts":[
     {"id":"concepts","type":"long","label":"Name two or three concepts, theories or methods from my subject that I could use on this topic.","hint":"If you cannot name any yet, look through your subject notes or textbook, or ask your subject teacher.","rows":3},
     {"id":"worry","type":"long","label":"What worries me about this topic? (Too broad? Not enough sources? Too close to my IA?)","rows":2}]},
   checklist(["I have one broad topic to explore.",
              "I have chosen a pathway and a subject (or two subjects and a framework), or I know what I need to find out to decide.",
              "I have checked the rules for my subject on this page.",
              "I have copied this thinking tool into my RRS."])
  ])
))
# ───────────────────────── STEP 2 ─────────────────────────
STEPS.append(dict(
 n=2, crumb="Step 2", title="Choose your citation style: APA or MLA",
 desc="Choose APA or MLA for your extended essay before you collect any sources, and set up PowerNotes.",
 lede="Decide how you will cite sources now — before you collect a single one — so you never have to redo your records.",
 body="""
    <h2>Why this step matters</h2>
    <p class="why">From step 3 onward you will collect around 40 sources. If you record each one in your chosen style as you find it, your works cited list at step 16 is almost finished already. If you switch styles halfway, you redo every entry.</p>
    <p>The IB does not require one particular style. It requires you to acknowledge every source using a standard style of referencing, consistently, throughout the essay. At ASD you will use <b>APA</b> or <b>MLA</b>.</p>

    <h2>Which style for which subject?</h2>
    <div class="tablewrap"><table class="info">
      <thead><tr><th>Style</th><th>Usually used in</th><th>In-text citation looks like</th></tr></thead>
      <tbody>
        <tr><th>MLA</th><td>Language A, Language B, Visual Arts</td><td>(Orwell 112)</td></tr>
        <tr><th>APA</th><td>Biology, Chemistry, Physics, Business Management, Economics, Global Politics, Mathematics</td><td>(Smith &amp; Lee, 2021, p. 4)</td></tr>
      </tbody></table></div>
    <p>These are the usual choices, not rules. Confirm the style with your supervisor, then use it for the whole essay. For an interdisciplinary essay, choose the style that suits the subject doing most of the work, and agree it with your supervisor.</p>
    <p>Use the current edition of your style. At the time of writing that is the MLA Handbook, 9th edition, and the APA Publication Manual, 7th edition. The Purdue Online Writing Lab has clear guides to both: <a href="https://owl.purdue.edu/owl/research_and_citation/mla_style/mla_formatting_and_style_guide/mla_general_format.html" target="_blank" rel="noopener">MLA guide</a> · <a href="https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html" target="_blank" rel="noopener">APA guide</a>.</p>

    <h2>Works cited, reference list and bibliography</h2>
    <ul>
      <li>A <b>reference list</b> (APA) or <b>works cited</b> list (MLA) includes only the sources you cite in the body of your essay.</li>
      <li>A <b>bibliography</b> lists every source you consulted during your research, including the ones you did not cite.</li>
    </ul>

    <h2>What to record for every source</h2>
    <p>Whatever style you choose, capture these details the moment you find a source — they are much harder to find again later:</p>
    <ul>
      <li>Author(s) or organisation</li>
      <li>Title of the work (and the journal, book or website it appears in)</li>
      <li>Date of publication</li>
      <li>Publisher</li>
      <li>URL or DOI, and the date you accessed it</li>
      <li>Page numbers for anything you might quote</li>
    </ul>

    <h2>Set up PowerNotes</h2>
    <ol class="do">
      <li>Log in to PowerNotes and create a project for your extended essay.</li>
      <li>Set the project's citation style to the style you have chosen, if your account offers that setting.</li>
      <li>Every time you save a source from step 3 onward, check the citation PowerNotes creates. Automatic citations often miss authors, dates or page numbers — fix them straight away.</li>
    </ol>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Writing your extended essay" (reference list and bibliography; citation and referencing) and "The ethical researcher".</p>
""",
 tool=dict(id="step-2", stepLabel="Step 2 · Choose your citation style", title="My citation style",
  sections=[
   {"heading":"Decide","prompts":[
     {"id":"subjectnow","type":"text","label":"My subject (from step 1):","prefill":"__PREFILL_SUBJECT__"},
     {"id":"style","type":"choice","label":"The citation style I will use:","options":["APA","MLA"]},
     {"id":"why","type":"long","label":"Why this style suits my subject:","rows":2},
     {"id":"confirmed","type":"choice","label":"Has my supervisor confirmed this style?","options":["Yes","Not yet — I will ask at our next meeting"]}]},
   {"heading":"Practise","prompts":[
     {"id":"practice","type":"long","label":"Find any one source on your topic and write its full citation in your chosen style.","hint":"Check it against the Purdue OWL guide for your style before you move on.","rows":3},
     {"id":"intext","type":"text","label":"Now write the in-text citation you would use for that source:"}]},
   checklist(["I have chosen APA or MLA.",
              "I have set up a PowerNotes project for my EE.",
              "I know the difference between a works cited list and a bibliography.",
              "I have copied this thinking tool into my RRS."])
  ])
))

# ───────────────────────── STEP 3 ─────────────────────────
STEPS.append(dict(
 n=3, crumb="Step 3", title="Open sources: get the background",
 desc="Use encyclopedias, reputable news and organisation websites to learn the background and key terms of your EE topic.",
 lede="Before you read research papers, learn the landscape: the key terms, people, events and debates in your topic.",
 body="""
    <h2>Why this step matters</h2>
    <p class="why">Scholarly articles assume you already know the basics. Open sources — free, general, easy to read — give you those basics quickly, so the harder reading in steps 4 to 6 makes sense.</p>
    <p>Open sources are for <b>orientation</b>. You will rarely cite them heavily in your final essay, but they point you towards the sources you will cite.</p>

    <h2>Where to look</h2>
    <ul>
      <li><b>Encyclopedias:</b> Encyclopaedia Britannica, subject encyclopedias, the Stanford Encyclopedia of Philosophy for ideas and theories.</li>
      <li><b>Wikipedia:</b> good for an overview — and its reference list at the bottom of each article is a map to better sources. Follow the references; do not cite Wikipedia itself.</li>
      <li><b>Reputable news:</b> BBC, Reuters, The Guardian, The Economist, Al Jazeera English, and newspapers from the country your topic is about.</li>
      <li><b>Organisations:</b> United Nations agencies, the World Health Organization, the World Bank, government statistics offices, museums, professional bodies.</li>
      <li><b>Open-access material:</b> free articles found through Google Scholar, and the free ERIC database for education topics.</li>
    </ul>

    <h2>Judge every source</h2>
    <p>The IB guide points out that you would judge "a post on Reddit, a sensationalist newspaper article, a blog post by an apparent expert and an article in a reputable academic journal" very differently. For each open source, ask:</p>
    <ul>
      <li><b>Who</b> wrote it, and what makes them qualified?</li>
      <li><b>When</b> was it published? Is it still current?</li>
      <li><b>Why</b> was it written — to inform, persuade, or sell?</li>
      <li><b>What evidence</b> does it give? Can you trace that evidence to its source?</li>
    </ul>

    <h2>What to do</h2>
    <ol class="do">
      <li>Read 8 to 12 open sources on your broad topic. Save each one in PowerNotes with its full citation in your chosen style, and put it in a category called <b>Open / background</b>.</li>
      <li>Build a glossary of the key terms in your topic, in your own words.</li>
      <li>Note the names — people, organisations, places, events — that keep appearing.</li>
      <li>Write down the questions that start to form as you read.</li>
    </ol>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Researching the extended essay" (preliminary investigation) and "Writing your extended essay" (citation and referencing).</p>
""",
 tool=dict(id="step-3", stepLabel="Step 3 · Open sources", title="What did the open sources tell me?",
  sections=[
   {"heading":"Key terms","prompts":[
     {"id":"terms","type":"table","label":"My glossary","columns":["Key term","What it means, in my own words","Where I found it"],"rows":5,"max":20}]},
   {"heading":"Who and what keeps appearing","prompts":[
     {"id":"names","type":"long","label":"People, organisations, places and events that come up again and again:","rows":3},
     {"id":"surprise","type":"long","label":"Three things that surprised me:","rows":3}]},
   {"heading":"Judging my sources","prompts":[
     {"id":"best","type":"long","label":"Which open source was most trustworthy, and why? Use who, when, why and what evidence.","rows":3},
     {"id":"worst","type":"long","label":"Which source did I decide not to trust, and why?","rows":2}]},
   {"heading":"Questions forming","prompts":[
     {"id":"questions","type":"long","label":"Questions I now have about my topic. Start them with how, why or to what extent.","rows":4}]},
   checklist(["I have saved 8 to 12 open sources in PowerNotes, in the Open / background category.",
              "Each one has a full citation in my chosen style.",
              "I have a glossary of key terms.",
              "I have copied this thinking tool into my RRS."])
  ])
))

# ───────────────────────── STEP 4 ─────────────────────────
STEPS.append(dict(
 n=4, crumb="Step 4", title="Current sources: what is being said now",
 desc="Find recent research, reports and data on your EE topic and map the current debate.",
 lede="Find out what researchers, journalists and organisations are saying about your topic right now — and where they disagree.",
 body="""
    <h2>Why this step matters</h2>
    <p class="why">Your essay joins a conversation that is already happening. Before you can add anything, you need to know who is speaking now, what they agree on, and where they disagree.</p>
    <p>"Current" usually means roughly the last five years — but this depends on the subject. A fast-moving science topic may need sources from the last two years; a literary topic may still be shaped by criticism from twenty years ago.</p>

    <h2>Where to look</h2>
    <ul>
      <li><b>Google Scholar:</b> search your key terms from step 3, then use <b>Since</b> in the left-hand menu to limit results to recent years. Click <b>Cited by</b> under a useful article to find newer work that builds on it.</li>
      <li><b>School library databases:</b> ask the librarian which databases ASD students can use, and how to log in from home.</li>
      <li><b>Reports and data:</b> recent reports from organisations such as the World Bank, OECD, United Nations agencies and government departments, and their data portals.</li>
      <li><b>Quality journalism:</b> recent long-form reporting and analysis, which often names the researchers involved — then look up their work.</li>
    </ul>

    <h2>Reading a research article quickly</h2>
    <ol class="do">
      <li>Read the abstract. Does it actually relate to your topic?</li>
      <li>Read the introduction's last paragraph — it usually states the aim — and then the conclusion.</li>
      <li>Only then read the method and results, if the article is worth it.</li>
      <li>Look at the reference list for sources you have not yet found.</li>
    </ol>

    <h2>What to do</h2>
    <ol class="do">
      <li>Find about 10 current sources. Save each in PowerNotes with its citation, in a category called <b>Current</b>.</li>
      <li>For each, note the position it takes, or the finding it reports.</li>
      <li>Map the debate: who agrees with whom, and where do they disagree?</li>
    </ol>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Researching the extended essay" (preliminary investigation: "What has already been written about this topic? Is there a range of views or perspectives?").</p>
""",
 tool=dict(id="step-4", stepLabel="Step 4 · Current sources", title="Mapping the current debate",
  sections=[
   {"heading":"Positions","prompts":[
     {"id":"positions","type":"table","label":"Current sources and the positions they take","columns":["Source (author, year)","Its main claim or finding","Evidence it uses"],"rows":5,"max":15}]},
   {"heading":"The debate","prompts":[
     {"id":"agree","type":"long","label":"What do most current sources agree on?","rows":3},
     {"id":"disagree","type":"long","label":"Where do they disagree? Name the sources on each side.","rows":3},
     {"id":"new","type":"long","label":"What is new — something that has only been studied or reported recently?","rows":3}]},
   {"heading":"Questions forming","prompts":[
     {"id":"questions","type":"long","label":"Which questions are still unanswered, or argued about, in the current sources?","rows":3}]},
   checklist(["I have saved about 10 current sources in PowerNotes, in the Current category.",
              "I have used Google Scholar's Since filter and Cited by links.",
              "I can name at least one disagreement in my topic.",
              "I have copied this thinking tool into my RRS."])
  ])
))

# ───────────────────────── STEP 5 ─────────────────────────
STEPS.append(dict(
 n=5, crumb="Step 5", title="Historical sources: how we got here",
 desc="Trace the history of thinking on your EE topic: foundational works, earlier debates and what changed.",
 lede="Trace how thinking on your topic developed — the foundational work, the old debates, and what changed people's minds.",
 body="""
    <h2>Why this step matters</h2>
    <p class="why">Current research builds on older work. If you know the history of your topic, you can see why today's researchers ask the questions they ask — and you can spot assumptions that nobody has tested for a while.</p>

    <h2>What "historical" means in your subject</h2>
    <ul>
      <li><b>Sciences and Mathematics:</b> the classic experiments, theorems and models your topic rests on, and who first proposed them.</li>
      <li><b>Economics, Business Management and Global Politics:</b> the theories you will apply (where they came from, and what they were responding to), and earlier events or cases like yours.</li>
      <li><b>Language A and Language B:</b> how the text was received when it was published, how critics' readings have changed since, and the context the text was written in.</li>
      <li><b>Visual Arts:</b> the movements, influences and earlier artists behind the work you are studying, and how the work has been interpreted over time.</li>
    </ul>

    <h2>How to find foundational work</h2>
    <ul>
      <li>Notice which older sources are cited again and again in the current sources from step 4. Those are usually the foundational works.</li>
      <li>On Google Scholar, a very high <b>Cited by</b> number on an older article often means it shaped the field.</li>
      <li>Look for review articles or textbook chapters that summarise how thinking on a topic has developed.</li>
    </ul>

    <h2>What to do</h2>
    <ol class="do">
      <li>Find about 10 historical sources. Save each in PowerNotes with its citation, in a category called <b>Historical</b>.</li>
      <li>Build a short timeline of how ideas about your topic changed.</li>
      <li>Note one older idea that current sources now challenge.</li>
    </ol>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Writing your extended essay" (citation and referencing: "They demonstrate whether you know who the most reputable authors are for the topic").</p>
""",
 tool=dict(id="step-5", stepLabel="Step 5 · Historical sources", title="How thinking on my topic has changed",
  sections=[
   {"heading":"Timeline","prompts":[
     {"id":"timeline","type":"table","label":"Key moments in the history of my topic","columns":["Year","Work, idea or event","Why it mattered"],"rows":5,"max":15}]},
   {"heading":"Then and now","prompts":[
     {"id":"then","type":"long","label":"What did people believe about my topic 50 years ago (or when the text or artwork was made)?","rows":3},
     {"id":"changed","type":"long","label":"What changed their minds — new evidence, new methods, new events, new perspectives?","rows":3},
     {"id":"cited","type":"long","label":"Which older authors or works keep being cited by current sources?","rows":2},
     {"id":"challenge","type":"long","label":"One older idea that current sources now challenge:","rows":2}]},
   checklist(["I have saved about 10 historical sources in PowerNotes, in the Historical category.",
              "I have a timeline of how ideas about my topic developed.",
              "I have copied this thinking tool into my RRS."])
  ])
))

# ───────────────────────── STEP 6 ─────────────────────────
METHODS_ROWS = [
 ("Language A","Close textual analysis of your primary text(s): language, structure, literary devices and their effects.","The novels, poems, plays, films (screenplay) or other texts you analyse.","Literary criticism, studies of the author or genre, journal articles, literary theory. A review of existing criticism is required."),
 ("Language B","Analysis of texts originally written or spoken in the target language — as literature, as language use, or as cultural artefacts.","Texts or cultural artefacts originally in the target language.","Academic writing about the texts, the language or the culture. A good range of secondary sources is essential."),
 ("Visual Arts","Formal analysis of artworks combined with contextual analysis (historical, social, cultural). Mostly qualitative.","Artworks, artists' statements, letters, diaries, interviews.","Art history and criticism, exhibition catalogues, scholarly articles."),
 ("Biology, Chemistry, Physics","An experiment with controlled variables and a standardized method; or analysis of secondary data that used similar standardized approaches and controls.","Data you collect in the lab or field.","Peer-reviewed publications and databases. ASD expects science EEs to be built on primary (experimental) data — the IB allows secondary-data science essays, but workshop guidance is that they rarely reach the top bands."),
 ("Business Management","A case study of a real organisation, analysed with business tools and concepts.","Interviews and surveys (for example with managers, staff or customers), company documents.","Academic articles, company reports, industry analysis, quality journalism."),
 ("Economics","Applying economic theory to a real situation and testing it against evidence.","Surveys, interviews, prices or data you collect yourself.","Data banks and statistics, economic research, news reporting."),
 ("Global Politics","A literature review of key political concepts, then analysis of one or more cases.","Speeches, policies, treaties, official documents; your own data where appropriate.","Academic writing on the concepts and cases. Primary data may supplement this."),
 ("Mathematics","Theoretical: exploring mathematics beyond the syllabus. Practical: using mathematics to model or analyse an issue or a data set.","Data you collect or obtain (for practical essays).","Mathematical texts and articles. A review of the literature is mandatory."),
 ("Interdisciplinary","Methods drawn from both of your subjects, chosen so they can be integrated.","Whatever counts as primary in each of your two subjects.","Secondary research in both subjects."),
]
rows_html = "\n".join(
  '        <tr data-subject="%s"><th>%s</th><td>%s</td><td>%s</td><td>%s</td></tr>' % (html.escape(s), html.escape(s), html.escape(a), html.escape(b), html.escape(c))
  for s,a,b,c in METHODS_ROWS)

STEPS.append(dict(
 n=6, crumb="Step 6", title="Research methods in your subject",
 desc="How researchers in your EE subject answer questions: methods, primary and secondary sources, and examples.",
 lede="Every subject has its own ways of answering questions. Learn the methods your subject trusts before you write your question.",
 body="""
    <h2>Why this step matters</h2>
    <p class="why">Criterion A asks whether your research methods provide an effective framework for your essay. The question you write in step 10 has to be one that your subject's methods can actually answer.</p>
    <p>Every extended essay must include secondary research — a review of the literature. Most subjects also expect primary research. What counts as primary and secondary is different in each subject.</p>

    <h2>Methods by subject</h2>
    <p id="mine-note" class="small muted" hidden></p>
    <div class="tablewrap"><table class="info" id="methods">
      <thead><tr><th>Subject</th><th>Typical approach</th><th>Primary sources</th><th>Secondary sources</th></tr></thead>
      <tbody>
""" + rows_html + """
      </tbody></table></div>
    <p>Not offered at ASD but worth knowing: Psychology extended essays must be based on secondary sources only — collecting primary data is not permitted.</p>

    <h2>See methods in action</h2>
    <p>The best way to understand methods in your subject is to see how real essays used them. Open two sample essays in your subject and read the introduction (where the method is explained) and the examiner's comments on Criterion A.</p>
    <p><a class="btn" id="samples-link" href="../../samples/">Open sample essays</a></p>

    <h2>What to do</h2>
    <ol class="do">
      <li>Read the row for your subject in the table above.</li>
      <li>Read two sample essays in your subject: how did each student answer their question, and what did the examiner say about the method?</li>
      <li>Find about 10 sources about methods — articles in your topic that show a method you could use, or guides to a method. Save them in PowerNotes in a category called <b>Methods</b>.</li>
    </ol>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Generic guidance" (primary and secondary sources) and "Subject-specific guidance" for each subject.</p>
""",
 script="""/* highlight the subject chosen in step 1 */
(function(){
  var path = EETools.read("step-1","pathway") || "";
  var s = path==="Interdisciplinary (two subjects)" ? "Interdisciplinary (two subjects)" : (path==="Subject-focused (one subject)" ? (EETools.read("step-1","subject")||"") : "");
  if(!s) return;
  var map = {"Biology":"Biology, Chemistry, Physics","Chemistry":"Biology, Chemistry, Physics","Physics":"Biology, Chemistry, Physics","Interdisciplinary (two subjects)":"Interdisciplinary"};
  var key = map[s] || s;
  var row = document.querySelector('#methods tr[data-subject="'+key+'"]');
  if(row){ row.classList.add("mine");
    var n = document.getElementById("mine-note"); n.hidden=false; n.textContent = "Your subject from step 1 is highlighted.";
  }
  var link = document.getElementById("samples-link");
  if(link && s && s!=="Another subject"){
    var subj = s==="Interdisciplinary (two subjects)" ? "Interdisciplinary" : s;
    link.href = "../../samples/?subject="+encodeURIComponent(subj);
    link.textContent = "Open sample essays in "+subj;
  }
})();""",
 tool=dict(id="step-6", stepLabel="Step 6 · Research methods in your subject", title="Methods I could use",
  sections=[
   {"heading":"My subject","prompts":[
     {"id":"subject","type":"text","label":"My subject (from step 1):","prefill":"__PREFILL_SUBJECT__"},
     {"id":"primary","type":"long","label":"In my subject, what counts as a primary source for my topic?","rows":2},
     {"id":"secondary","type":"long","label":"What counts as a secondary source?","rows":2}]},
   {"heading":"Learning from sample essays","prompts":[
     {"id":"samples","type":"table","label":"Two sample essays in my subject","columns":["Sample (subject and letter)","How the student answered the question (method)","What the examiner said about it"],"rows":2,"max":4}]},
   {"heading":"Methods for my topic","prompts":[
     {"id":"methods","type":"long","label":"Two or three methods I could use on my topic, and what each would show me:","rows":4},
     {"id":"practical","type":"long","label":"What would each method need — equipment, access to people, texts, data, time? Is it realistic at school?","rows":3}]},
   checklist(["I have read the methods row for my subject.",
              "I have read two sample essays in my subject.",
              "I have saved about 10 methods sources in PowerNotes, in the Methods category.",
              "I have copied this thinking tool into my RRS."])
  ])
))

# ───────────────────────── STEP 7 ─────────────────────────
STEPS.append(dict(
 n=7, crumb="Step 7", title="Collect 40 sources in PowerNotes",
 desc="Collect and categorise 40 sources for your EE in PowerNotes, then look for the patterns that will shape your question.",
 lede="Bring your reading together: 40 sources, organised so you can see what your topic is really about.",
 body="""
    <h2>Why this step matters</h2>
    <p class="why">Forty sources is more than you will cite — and that is the point. A wide collection shows you the shape of your topic: the themes that keep returning, the arguments that matter, and the gaps. In step 9 you will narrow these 40 to the 20 best.</p>

    <h2>Organise PowerNotes</h2>
    <p>You already have four categories from steps 3 to 6. Keep them, and add theme categories as patterns appear.</p>
    <div class="kv">
      <div class="panel"><h3>Open / background</h3><p>From step 3. Orientation and key terms.</p></div>
      <div class="panel"><h3>Current</h3><p>From step 4. Recent research and debate.</p></div>
      <div class="panel"><h3>Historical</h3><p>From step 5. Foundational work.</p></div>
      <div class="panel"><h3>Methods</h3><p>From step 6. How your question could be answered.</p></div>
    </div>
    <p>For every source, check that PowerNotes has a full citation in your chosen style, and add a one-line note on why the source matters.</p>

    <h2>Check your collection</h2>
    <ul>
      <li><b>Spread:</b> no single category should hold more than about half your sources.</li>
      <li><b>Quality:</b> a good share of your sources should be scholarly — peer-reviewed articles, academic books, or data from reputable organisations.</li>
      <li><b>Perspectives:</b> do your sources disagree with each other anywhere? If every source says the same thing, look for the other side.</li>
      <li><b>Records:</b> every source has a complete citation in your chosen style.</li>
    </ul>

    <h2>Then step back</h2>
    <p>Read your one-line notes from top to bottom. Which themes keep coming up? Which sources do you keep going back to? Where do you feel most curious? Those answers point to the narrower topic you will choose in step 8.</p>
    <p class="src-note">Source: IB <i>Extended essay guide</i> (first assessment 2027), "Researching the extended essay" (preliminary investigation and changing direction).</p>
""",
 tool=dict(id="step-7", stepLabel="Step 7 · Collect 40 sources", title="What my 40 sources are telling me",
  sections=[
   {"heading":"Count","note":"Enter how many sources you have in each PowerNotes category.","prompts":[
     {"id":"n_open","type":"number","label":"Open / background","min":0,"max":99},
     {"id":"n_current","type":"number","label":"Current","min":0,"max":99},
     {"id":"n_hist","type":"number","label":"Historical","min":0,"max":99},
     {"id":"n_methods","type":"number","label":"Methods","min":0,"max":99},
     {"id":"total","type":"total","label":"Total sources:","of":["n_open","n_current","n_hist","n_methods"],"target":40,"warnShare":0.5}]},
   {"heading":"Patterns","prompts":[
     {"id":"themes","type":"long","label":"Themes that keep coming up across my sources:","rows":3},
     {"id":"top5","type":"table","label":"The five sources I keep going back to","columns":["Source (author, year)","Why I keep going back to it"],"rows":5,"max":5},
     {"id":"missing","type":"long","label":"What is missing from my collection — a perspective, a type of source, a time period, a place?","rows":3}]},
   {"heading":"What my topic is really about","prompts":[
     {"id":"topicnow","type":"text","label":"My broad topic at step 1 was:","prefill":"__PREFILL_TOPIC__"},
     {"id":"really","type":"long","label":"In one or two sentences: what is my topic really about now?","rows":3}]},
   checklist(["I have 40 sources in PowerNotes.",
              "Every source has a full citation in my chosen style and a one-line note.",
              "No single category holds more than about half my sources.",
              "I have copied this thinking tool into my RRS."])
  ])
))

def build():
    for s in STEPS:
        d = os.path.join(ROOT, "step-%d" % s["n"])
        os.makedirs(d, exist_ok=True)
        page_title = s["title"] if s["n"]==0 else "Step %d: %s" % (s["n"], s["title"])
        out = TEMPLATE.format(page_title=html.escape(page_title), desc=html.escape(s["desc"]), n=s["n"],
                              crumb=html.escape(s["crumb"]), title=html.escape(s["title"]).replace("APA or MLA","APA or MLA"),
                              lede=s["lede"], body=s["body"].rstrip(), script=s.get("script",""), tool=tool_js(s["tool"]))
        open(os.path.join(d, "index.html"), "w").write(out)
        print("wrote", os.path.relpath(os.path.join(d,"index.html"), os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")))

if __name__ == "__main__":
    build()
