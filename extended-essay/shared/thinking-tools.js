/* ═══════════════════════════════════════════════════════════════
   Extended Essay hub — thinking tools engine
   One script draws every thinking tool on every step page.

   A thinking tool is private brainstorming, not an assignment.
   - Answers save automatically in this browser (localStorage), per tool.
   - "Copy for Google Docs" copies the questions and answers as clean
     formatted text, ready to paste into the student's RRS Google Doc.
   - Nothing is sent anywhere.

   Usage on a page:
     <div data-tool="step-1"></div>
     <script src="../../shared/thinking-tools.js"></script>
     <script>EETools.define({ id:"step-1", title:"…", sections:[ … ] });</script>

   Prompt types:
     text      one line            {id, type:"text", label, hint, placeholder}
     long      paragraph           {id, type:"long", label, hint, rows}
     choice    pick one            {id, type:"choice", label, options:[…]}
     multi     pick any            {id, type:"multi", label, options:[…]}
     number    a number            {id, type:"number", label, min, max}
     table     rows × columns      {id, type:"table", label, columns:[…], rows:3, max:12}
     checklist tick list           {id, type:"checklist", label, items:[…]}
     total     sum of number ids   {id, type:"total", label, of:[ids], target, warnShare}
   Any prompt can have showIf:{id, equals} to appear only after a choice.
   ═══════════════════════════════════════════════════════════════ */
(function(){
  var PREFIX = "ee-tt:";
  var tools = {};

  function load(id){
    try{ return JSON.parse(localStorage.getItem(PREFIX+id) || "{}") || {}; }catch(e){ return {}; }
  }
  function store(id, data){
    try{ localStorage.setItem(PREFIX+id, JSON.stringify(data)); return true; }catch(e){ return false; }
  }
  function esc(s){ return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];}); }
  function el(tag, attrs, html){
    var n = document.createElement(tag);
    if(attrs) for(var k in attrs){ if(k==="class") n.className=attrs[k]; else n.setAttribute(k, attrs[k]); }
    if(html!=null) n.innerHTML = html;
    return n;
  }

  /* ── public: read another tool's answer (e.g. step 6 reads the subject chosen in step 1) ── */
  function read(toolId, fieldId){ var d = load(toolId); return fieldId ? d[fieldId] : d; }
  function hasAnswers(toolId){
    var d = load(toolId);
    return Object.keys(d).some(function(k){
      var v = d[k];
      if(Array.isArray(v)) return v.some(function(r){ return r && (typeof r==="string" ? r.trim() : Object.keys(r).some(function(c){ return String(r[c]||"").trim(); })); });
      return v!=null && String(v).trim()!=="";
    });
  }

  function define(def){
    tools[def.id] = def;
    var mount = document.querySelector('[data-tool="'+def.id+'"]');
    if(!mount){ return; }
    render(def, mount);
  }

  function render(def, mount){
    var data = load(def.id);
    var canSave = store(def.id, data);   // probe storage once
    mount.classList.add("tt");
    mount.innerHTML = "";

    var head = el("div",{class:"tt-head"});
    head.appendChild(el("p",{class:"tt-kicker"},"Thinking tool"));
    head.appendChild(el("h2",null,esc(def.title)));
    if(def.intro) head.appendChild(el("p",{class:"tt-intro"},def.intro));
    head.appendChild(el("p",{class:"tt-privacy"}, canSave
      ? "Private to you. Your answers save automatically in this browser on this device only — nobody else sees them and nothing is submitted. Use <b>Copy for Google Docs</b> to keep them in your RRS."
      : "Your browser is not letting this page save answers (private browsing can do this). You can still type — just copy everything into your RRS Google Doc before you leave."));
    mount.appendChild(head);

    var form = el("div",{class:"tt-body"});
    mount.appendChild(form);

    var saveTimer = null, status;
    function save(){
      /* write straight away so nothing is lost if the student leaves the page mid-sentence;
         only the "Saved" message waits */
      var ok = store(def.id, data);
      clearTimeout(saveTimer);
      saveTimer = setTimeout(function(){
        if(ok){ status.textContent = "Saved in this browser"; status.classList.add("ok"); }
      }, 300);
      refreshConditionals(); refreshTotals();
    }

    var conditionals = [], totals = [];

    (def.sections||[]).forEach(function(sec){
      var s = el("section",{class:"tt-sec"});
      if(sec.heading) s.appendChild(el("h3",null,esc(sec.heading)));
      if(sec.note) s.appendChild(el("p",{class:"tt-note"},sec.note));
      (sec.prompts||[]).forEach(function(p){
        var w = buildPrompt(p, data, save, def.id);
        if(p.showIf) conditionals.push([w, p.showIf]);
        if(p.type==="total") totals.push([w, p]);
        s.appendChild(w);
      });
      form.appendChild(s);
    });

    function refreshConditionals(){
      conditionals.forEach(function(c){
        var v = data[c[1].id];
        var show = Array.isArray(v) ? v.indexOf(c[1].equals)>-1 : v===c[1].equals;
        c[0].hidden = !show;
      });
    }
    function refreshTotals(){
      totals.forEach(function(t){
        var p = t[1], sum = 0, maxPart = 0;
        p.of.forEach(function(k){ var n = parseInt(data[k],10); if(!isNaN(n)){ sum+=n; if(n>maxPart) maxPart=n; } });
        var msg = "<b>"+sum+"</b>"+(p.target?" of "+p.target:"");
        var note = "";
        if(p.target && sum>=p.target) note = " — target reached.";
        if(p.warnShare && sum>0 && maxPart/sum > p.warnShare) note += " One category holds more than "+Math.round(p.warnShare*100)+"% of your sources — spread out a little.";
        t[0].querySelector(".tt-totalval").innerHTML = msg + '<span class="tt-totalnote">'+note+'</span>';
      });
    }
    refreshConditionals(); refreshTotals();

    /* toolbar */
    var bar = el("div",{class:"tt-bar"});
    var copyBtn = el("button",{type:"button",class:"btn tt-copy"},"Copy for Google Docs");
    var clearBtn = el("button",{type:"button",class:"btn tt-clear"},"Clear my answers");
    status = el("span",{class:"tt-status","aria-live":"polite"}, canSave && hasAnswers(def.id) ? "Saved in this browser" : "");
    bar.appendChild(copyBtn); bar.appendChild(clearBtn); bar.appendChild(status);
    mount.appendChild(bar);

    copyBtn.addEventListener("click", function(){
      var out = buildExport(def, data);
      copyRich(out.html, out.text).then(function(ok){
        status.classList.toggle("ok", ok);
        status.textContent = ok
          ? "Copied. Open your RRS Google Doc and paste (Ctrl+V, or ⌘V on a Mac)."
          : "Copy didn't work in this browser — select the answers on the page and copy them by hand.";
      });
    });

    var armed = false, armTimer;
    clearBtn.addEventListener("click", function(){
      if(!armed){
        armed = true; clearBtn.textContent = "Click again to clear everything"; clearBtn.classList.add("armed");
        armTimer = setTimeout(function(){ armed=false; clearBtn.textContent="Clear my answers"; clearBtn.classList.remove("armed"); }, 4000);
        return;
      }
      clearTimeout(armTimer);
      try{ localStorage.removeItem(PREFIX+def.id); }catch(e){}
      render(def, mount);
    });
  }

  function field(p){
    var w = el("div",{class:"tt-q tt-"+p.type});
    if(p.label) w.appendChild(el(p.type==="choice"||p.type==="multi"||p.type==="checklist"||p.type==="table" ? "p" : "label",
      p.type==="text"||p.type==="long"||p.type==="number" ? {class:"tt-label","for":"f-"+p.id} : {class:"tt-label"}, p.label));
    if(p.hint) w.appendChild(el("p",{class:"tt-hint"},p.hint));
    return w;
  }

  function buildPrompt(p, data, save, toolId){
    var w = field(p);
    if(p.type==="text" || p.type==="number"){
      var i = el("input",{id:"f-"+p.id, type:p.type==="number"?"number":"text"});
      if(p.placeholder) i.placeholder = p.placeholder;
      if(p.min!=null) i.min = p.min; if(p.max!=null) i.max = p.max;
      if(p.type==="number") i.inputMode = "numeric";
      i.value = data[p.id]!=null ? data[p.id] : (p.prefill ? (p.prefill()||"") : "");
      if(p.prefill && data[p.id]==null && i.value){ data[p.id]=i.value; }
      i.addEventListener("input", function(){ data[p.id]=i.value; save(); });
      w.appendChild(i);
    }
    else if(p.type==="long"){
      var t = el("textarea",{id:"f-"+p.id, rows:p.rows||4});
      if(p.placeholder) t.placeholder = p.placeholder;
      t.value = data[p.id]||"";
      t.addEventListener("input", function(){ data[p.id]=t.value; save(); });
      w.appendChild(t);
    }
    else if(p.type==="choice" || p.type==="multi" || p.type==="checklist"){
      var multi = p.type!=="choice";
      var items = p.options || p.items;
      var cur = data[p.id]!=null ? data[p.id] : (p.prefill ? p.prefill() : (multi?[]:""));
      if(p.prefill && data[p.id]==null && cur && cur.length){ data[p.id]=cur; }
      var box = el("div",{class:"tt-opts", role: multi?"group":"radiogroup"});
      items.forEach(function(opt, n){
        var id = "f-"+p.id+"-"+n;
        var lab = el("label",{class:"tt-opt","for":id});
        var inp = el("input",{type: multi?"checkbox":"radio", id:id, name:"f-"+p.id, value:opt});
        if(multi ? (cur||[]).indexOf(opt)>-1 : cur===opt) inp.checked = true;
        inp.addEventListener("change", function(){
          if(multi){
            var arr = (data[p.id]||[]).slice();
            if(inp.checked){ if(arr.indexOf(opt)<0) arr.push(opt); } else { arr = arr.filter(function(x){return x!==opt;}); }
            data[p.id] = arr;
          } else data[p.id] = opt;
          save();
        });
        lab.appendChild(inp); lab.appendChild(el("span",null,opt));
        box.appendChild(lab);
      });
      w.appendChild(box);
    }
    else if(p.type==="table"){
      var rows = Array.isArray(data[p.id]) ? data[p.id] : [];
      var min = p.rows||3;
      while(rows.length<min) rows.push({});
      data[p.id] = rows;
      var wrap = el("div",{class:"tt-tablewrap"});
      var table = el("table",{class:"tt-table"});
      var thead = "<thead><tr>"+p.columns.map(function(c){return "<th scope=\"col\">"+esc(c)+"</th>";}).join("")+"</tr></thead>";
      table.innerHTML = thead;
      var tbody = el("tbody");
      table.appendChild(tbody);
      function addRow(r, idx){
        var tr = el("tr");
        p.columns.forEach(function(c, ci){
          var td = el("td",{"data-col":c});
          var ta = el("textarea",{rows:2, "aria-label": c+", row "+(idx+1)});
          ta.value = r["c"+ci]||"";
          ta.addEventListener("input", function(){ r["c"+ci]=ta.value; save(); });
          td.appendChild(ta); tr.appendChild(td);
        });
        tbody.appendChild(tr);
      }
      rows.forEach(addRow);
      wrap.appendChild(table);
      w.appendChild(wrap);
      var more = el("button",{type:"button",class:"btn tt-addrow"},"+ Add a row");
      more.addEventListener("click", function(){
        if(rows.length >= (p.max||20)) { more.disabled = true; return; }
        var r = {}; rows.push(r); addRow(r, rows.length-1); save();
        if(rows.length >= (p.max||20)) more.disabled = true;
      });
      w.appendChild(more);
    }
    else if(p.type==="total"){
      w.appendChild(el("p",{class:"tt-totalval"},""));
    }
    return w;
  }

  /* ── export: questions as headings, answers as text, tables as tables ── */
  function buildExport(def, data){
    var html = [], text = [];
    var today = new Date().toLocaleDateString(undefined,{year:"numeric",month:"long",day:"numeric"});
    html.push("<h2>"+esc(def.copyTitle||def.title)+"</h2>");
    html.push("<p><i>"+esc(def.stepLabel||"")+(def.stepLabel?" · ":"")+"copied "+esc(today)+"</i></p>");
    text.push((def.copyTitle||def.title).toUpperCase());
    text.push((def.stepLabel?def.stepLabel+" · ":"")+"copied "+today, "");
    var blank = "<p style=\"color:#888\"><i>(not answered yet)</i></p>";

    (def.sections||[]).forEach(function(sec){
      if(sec.heading){ html.push("<h3>"+esc(sec.heading)+"</h3>"); text.push(sec.heading.toUpperCase()); }
      (sec.prompts||[]).forEach(function(p){
        if(p.showIf){
          var cv = data[p.showIf.id];
          var show = Array.isArray(cv) ? cv.indexOf(p.showIf.equals)>-1 : cv===p.showIf.equals;
          if(!show) return;
        }
        var label = stripTags(p.label||"");
        var v = data[p.id];
        if(p.type==="total"){
          var sum=0; p.of.forEach(function(k){ var n=parseInt(data[k],10); if(!isNaN(n)) sum+=n; });
          html.push("<p><b>"+esc(label)+"</b> "+sum+(p.target?" of "+p.target:"")+"</p>");
          text.push(label+" "+sum+(p.target?" of "+p.target:""), "");
          return;
        }
        html.push("<p><b>"+esc(label)+"</b></p>");
        text.push(label);
        if(p.type==="table"){
          var rows = (v||[]).filter(function(r){ return Object.keys(r).some(function(k){ return String(r[k]||"").trim(); }); });
          if(!rows.length){ html.push(blank); text.push("(not answered yet)",""); return; }
          var t = "<table border=\"1\" style=\"border-collapse:collapse\"><tr>"+p.columns.map(function(c){return "<th style=\"padding:4px 8px;text-align:left\">"+esc(c)+"</th>";}).join("")+"</tr>";
          rows.forEach(function(r){
            t += "<tr>"+p.columns.map(function(c,ci){ return "<td style=\"padding:4px 8px;vertical-align:top\">"+esc(r["c"+ci]||"")+"</td>"; }).join("")+"</tr>";
            text.push("- "+p.columns.map(function(c,ci){ return c+": "+(r["c"+ci]||""); }).join(" | "));
          });
          html.push(t+"</table>"); text.push("");
        }
        else if(p.type==="multi" || p.type==="checklist"){
          var items = p.options || p.items, sel = v||[];
          if(p.type==="multi" && !sel.length){ html.push(blank); text.push("(not answered yet)",""); return; }
          var list = p.type==="checklist" ? items : sel;
          html.push("<ul>"+list.map(function(o){ return "<li>"+(p.type==="checklist"?(sel.indexOf(o)>-1?"☑ ":"☐ "):"")+esc(o)+"</li>"; }).join("")+"</ul>");
          list.forEach(function(o){ text.push((p.type==="checklist"?(sel.indexOf(o)>-1?"[x] ":"[ ] "):"- ")+o); });
          text.push("");
        }
        else {
          var s = v==null ? "" : String(v).trim();
          if(!s){ html.push(blank); text.push("(not answered yet)",""); return; }
          s.split(/\n+/).forEach(function(line){ html.push("<p>"+esc(line)+"</p>"); text.push(line); });
          text.push("");
        }
      });
    });
    return { html: html.join(""), text: text.join("\n") };
  }
  function stripTags(s){ var d=document.createElement("div"); d.innerHTML=s; return d.textContent||""; }

  function copyRich(html, text){
    if(navigator.clipboard && window.ClipboardItem && window.isSecureContext){
      try{
        var item = new ClipboardItem({
          "text/html": new Blob([html],{type:"text/html"}),
          "text/plain": new Blob([text],{type:"text/plain"})
        });
        return navigator.clipboard.write([item]).then(function(){return true;}, function(){ return legacyCopy(html); });
      }catch(e){ return Promise.resolve(legacyCopy(html)); }
    }
    return Promise.resolve(legacyCopy(html));
  }
  function legacyCopy(html){
    var d = document.createElement("div");
    d.contentEditable = "true"; d.innerHTML = html;
    d.style.position="fixed"; d.style.left="-9999px"; d.style.top="0";
    document.body.appendChild(d);
    var r = document.createRange(); r.selectNodeContents(d);
    var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
    var ok = false; try{ ok = document.execCommand("copy"); }catch(e){}
    sel.removeAllRanges(); d.remove();
    return ok;
  }

  window.EETools = { define: define, read: read, hasAnswers: hasAnswers, _export: function(id){ return buildExport(tools[id], load(id)); } };
})();
