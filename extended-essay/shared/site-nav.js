/* Extended Essay hub: the one navigation bar for the whole site.
   To change the links, edit SECTIONS below. Every page loads this file straight after <body>.
   The bar also remembers the last step a student opened, so subject guides, sample essays and
   other reference pages can show a "Back to Step N" link. */
(function(){
  var me = document.currentScript;
  var base = new URL("../", me.src).href;
  var rel = location.href.split(/[?#]/)[0].replace(base, "");
  var fromTeachers = new URLSearchParams(location.search).get("from") === "teachers";

  var STUDENT = [
    ["Steps", "students/", /^students\/(step-\d+\/)?(index\.html)?$/],
    ["Subject guides", "subjects/", /^subjects\//],
    ["Sample essays", "samples/", /^samples\//],
    ["Criteria", "students/criteria/", /^students\/criteria\//],
    ["Integrity and AI", "students/integrity/", /^students\/integrity\//]
  ];
  var TEACHER = [
    ["Teacher home", "teachers/", /^teachers\/(index\.html)?$/],
    ["RPF and Criterion E", "teachers/rpf/", /^teachers\/rpf\//],
    ["Sample essays", "samples/?from=teachers", /^samples\//]
  ];
  var isHub = rel === "" || rel === "index.html";
  var isTeacher = /^teachers\//.test(rel) || fromTeachers;
  var items = isHub ? [] : (isTeacher ? TEACHER : STUDENT);

  var KEY = "ee-last-step", stepMatch = rel.match(/^students\/step-(\d+)\//), last = null;
  try{
    if(stepMatch) localStorage.setItem(KEY, stepMatch[1]);
    last = localStorage.getItem(KEY);
  }catch(e){}

  var links = items.map(function(it){
    var on = it[2].test(rel);
    return '<a href="'+base+it[1]+'"'+(on?' aria-current="page"':'')+'>'+it[0]+'</a>';
  }).join("");

  var bar = document.createElement("header");
  bar.className = "sitebar";
  bar.innerHTML = '<div class="sitebar-in">'
    + '<a class="mark" href="'+base+'" title="Extended Essay home">EE</a>'
    + '<nav aria-label="Extended Essay">'+links+'</nav>'
    + '<a class="guide-link" href="'+base+'guide/ee-guide-2027.pdf" target="_blank" rel="noopener" title="Open the official IB Extended essay guide (first assessment 2027) in a new tab">Official IB Guide (PDF)</a>'
    + '</div>';
  me.parentNode.insertBefore(bar, me);

  /* "Back to Step N" on reference pages only, once a student has opened a step */
  var isReference = !isTeacher && !isHub && /^(subjects|samples|students\/(criteria|integrity))\//.test(rel);
  if(isReference && last !== null){
    var back = document.createElement("div");
    back.className = "sitebar-back";
    back.innerHTML = '<div class="sitebar-in"><a href="'+base+'students/step-'+last+'/" id="ee-back">← Back to '+(last==="0"?"Start here":"Step "+last)+'</a></div>';
    bar.appendChild(back);
    /* add the step title once data/steps.js is available, if this page loads it */
    var s = document.createElement("script");
    s.src = base+"data/steps.js";
    s.onload = function(){
      var st = (window.EE_STEPS||[]).filter(function(x){return String(x.n)===last;})[0];
      var a = document.getElementById("ee-back");
      if(st && a) a.textContent = "← Back to "+(st.n===0?st.title:"Step "+st.n+": "+st.title);
      setHeight();
    };
    document.head.appendChild(s);
  }

  function setHeight(){ document.documentElement.style.setProperty("--bar-h", bar.offsetHeight+"px"); }
  setHeight();
  addEventListener("resize", setHeight);
})();
