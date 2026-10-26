/* Extended Essay hub — the student steps.
   Used by students/index.html (the path) and by every step page (step header + previous/next links).
   To make a step live: build students/step-N/index.html, then set live:true here.
   Dates are NOT stored here — each year's dates belong in data/timeline.js (to come). */

window.EE_PHASES = [
  {id:"explore",  name:"Explore",                 blurb:"Find a subject and a topic, then read widely about your topic."},
  {id:"narrow",   name:"Narrow",                  blurb:"Turn a broad topic into a research question."},
  {id:"write",    name:"Research and write",      blurb:"Collect your data and write your essay one section at a time."},
  {id:"after",    name:"After submission",        blurb:"Your viva voce and your reflective statement."}
];

window.EE_STEPS = [
  {n:0,  phase:"explore", live:true,  title:"Start here",                                   blurb:"What the EE is, how this site works, and how to set up your RRS."},
  {n:1,  phase:"explore", live:true,  title:"Choose a subject and a broad topic",           blurb:"Pick what interests you, choose your pathway (one subject or interdisciplinary), and check that the subject fits."},
  {n:2,  phase:"explore", live:true,  title:"Choose your citation style: APA or MLA",       blurb:"Decide on a style before you collect any sources."},
  {n:3,  phase:"explore", live:true,  title:"Open sources: get the background",             blurb:"Use encyclopedias, trusted news sites and organisations to learn the main terms of your topic."},
  {n:4,  phase:"explore", live:true,  title:"Current sources: what is being said now",      blurb:"Find recent research and debate on your topic."},
  {n:5,  phase:"explore", live:true,  title:"Historical sources: how we got here",          blurb:"Early, important work on your topic, and how ideas about your topic have changed."},
  {n:6,  phase:"explore", live:true,  title:"Research methods in your subject",             blurb:"How researchers in your subject answer questions."},
  {n:7,  phase:"explore", live:true,  title:"Collect your sources in PowerNotes",            blurb:"Reach the source target for your subject, sort your sources into categories, and see what your topic is really about."},

  {n:8,  phase:"narrow",  live:true, title:"Narrow your topic and write a broad question", blurb:"Go from a broad topic to a working question (a first draft of your question)."},
  {n:9,  phase:"narrow",  live:true, title:"Annotated bibliography",                       blurb:"Annotate your main sources, include different points of view, and find the gap in the research (something other researchers haven't covered yet)."},
  {n:10,  phase:"narrow",  live:true, title:"Your research question and the parts of a paper", blurb:"Write a focused research question and learn how papers in your subject are built. Your first reflection session (a meeting with your supervisor) comes after this step."},

  {n:11, phase:"write",   live:false, title:"Ethics check",                                 blurb:"Check your research is ethical before you collect any data."},
  {n:12, phase:"write",   live:false, title:"Outline your essay",                           blurb:"Plan the structure your subject expects. Talk your outline through with your supervisor."},
  {n:13, phase:"write",   live:false, title:"Introduction and literature review",           blurb:"Context, your research question, your method, and what has already been written."},
  {n:14, phase:"write",   live:false, title:"Collect your data",                            blurb:"Experiments, surveys, interviews, texts or artworks. Record your data properly. Your interim (middle) reflection session comes after this step."},
  {n:15, phase:"write",   live:false, title:"Analysis and the body",                        blurb:"Findings, analysis, discussion and evaluation."},
  {n:16, phase:"write",   live:false, title:"Write the conclusion",                         blurb:"Answer your research question. Then give your full draft to your supervisor for written feedback."},
  {n:17, phase:"write",   live:false, title:"Works cited and bibliography",                 blurb:"List every source in your chosen citation style."},
  {n:18, phase:"write",   live:false, title:"Format the essay",                             blurb:"The final check: title page, contents page, headings and word count.",
     extras:[["EE Formatting Game","../ee-formatting/"],["Table of Contents Pages","../table-of-contents-pages/"]]},

  {n:19, phase:"after",   live:false, title:"Viva voce and reflective statement",           blurb:"Your final reflection session and your 500-word reflective statement."}
];
