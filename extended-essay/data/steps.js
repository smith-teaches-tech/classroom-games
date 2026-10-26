/* Extended Essay hub — the student steps.
   Used by students/index.html (the path) and by every step page (step header + previous/next links).
   To make a step live: build students/step-N/index.html, then set live:true here.
   Dates are NOT stored here — each year's dates belong in data/timeline.js (to come). */

window.EE_PHASES = [
  {id:"explore",  name:"Explore",                 blurb:"Find a subject and a topic, and read widely around it."},
  {id:"narrow",   name:"Narrow",                  blurb:"Turn a broad topic into a research question."},
  {id:"write",    name:"Research and write",      blurb:"Collect your data and build the essay, section by section."},
  {id:"after",    name:"After submission",        blurb:"The viva voce and your reflective statement."}
];

window.EE_STEPS = [
  {n:0,  phase:"explore", live:true,  title:"Start here",                                   blurb:"What the EE is, how this site works, and setting up your RRS."},
  {n:1,  phase:"explore", live:true,  title:"Choose a subject and a broad topic",           blurb:"Pick what you care about, choose your pathway, and check the subject fits."},
  {n:2,  phase:"explore", live:true,  title:"Choose your citation style: APA or MLA",       blurb:"Decide before you collect a single source."},
  {n:3,  phase:"explore", live:true,  title:"Open sources: get the background",             blurb:"Encyclopedias, reputable news and organisations — learn the key terms."},
  {n:4,  phase:"explore", live:true,  title:"Current sources: what is being said now",      blurb:"Recent research and debate on your topic."},
  {n:5,  phase:"explore", live:true,  title:"Historical sources: how we got here",          blurb:"Foundational work and how thinking on your topic has changed."},
  {n:6,  phase:"explore", live:true,  title:"Research methods in your subject",             blurb:"How researchers in your subject answer questions."},
  {n:7,  phase:"explore", live:true,  title:"Collect your sources in PowerNotes",            blurb:"Reach the source target for your subject, categorise, and see what your topic is really about."},

  {n:8,  phase:"narrow",  live:true, title:"Narrow your topic and write a broad question", blurb:"From a broad topic to a working question."},
  {n:9,  phase:"narrow",  live:true, title:"Annotated bibliography",                       blurb:"Annotate your key sources, cover different perspectives, and find the gap in the research."},
  {n:10,  phase:"narrow",  live:true, title:"Your research question and the parts of a paper", blurb:"A focused question and how papers in your subject are built. First reflection session follows."},

  {n:11, phase:"write",   live:false, title:"Ethics check",                                 blurb:"Before you collect any data."},
  {n:12, phase:"write",   live:false, title:"Outline your essay",                           blurb:"Plan the structure your subject expects. Talk it through with your supervisor."},
  {n:13, phase:"write",   live:false, title:"Introduction and literature review",           blurb:"Context, your research question, your method, and what has already been written."},
  {n:14, phase:"write",   live:false, title:"Collect your data",                            blurb:"Experiments, surveys, interviews, texts or artworks — recorded properly. Interim reflection session follows."},
  {n:15, phase:"write",   live:false, title:"Analysis and the body",                        blurb:"Findings, analysis, discussion and evaluation."},
  {n:16, phase:"write",   live:false, title:"Write the conclusion",                         blurb:"Answer your question. Your full draft goes to your supervisor for written feedback."},
  {n:17, phase:"write",   live:false, title:"Works cited and bibliography",                 blurb:"Every source, in your chosen style."},
  {n:18, phase:"write",   live:false, title:"Format the essay",                             blurb:"Title page, contents, headings, word count — the final check.",
     extras:[["EE Formatting Game","../ee-formatting/"],["Table of Contents Pages","../table-of-contents-pages/"]]},

  {n:19, phase:"after",   live:false, title:"Viva voce and reflective statement",           blurb:"The final reflection session and your 500-word statement."}
];
