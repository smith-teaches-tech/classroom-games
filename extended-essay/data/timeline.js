/* EE Central: the ASD dates for one cohort. Edit this one file each year; pages carry no dates.
   key: used by pages that show a single date (data-when="key").
   you: what the supervisor does at that point (shown on teachers/role/). Leave "" if nothing. */
window.EE_TIMELINE = {
  cohort: "Class of 2028",
  note: "Deadlines are fixed. Year 2 dates (from August 2027) are provisional.",
  items: [
    {key:"alloc",   when:"Thu Dec 3",       what:"Supervisors allocated",                         you:"Optional 10-minute check-in before winter break."},
    {key:"topic",   when:"Thu Dec 17",      what:"Student has a topic and 3 to 5 starter sources", you:""},
    {key:"annbib",  when:"Thu Feb 4",       what:"Annotated bibliography due",                    you:""},
    {key:"s1",      when:"Feb 7 to 25",     what:"First reflection session (during Ramadan)",     you:"Hold the session. Fill in the RPF."},
    {key:"rq",      when:"Thu Mar 4",       what:"Research question approved",                    you:"Approve the research question."},
    {key:"outline", when:"Thu Apr 8",       what:"Outline due",                                   you:"Oral feedback at a check-in."},
    {key:"intro",   when:"Thu Apr 22",      what:"Introduction and literature review due",        you:""},
    {key:"s2",      when:"Thu Jun 3",       what:"Interim reflection session",                    you:"Hold the session. Oral feedback on the introduction. Fill in the RPF."},
    {key:"draft",   when:"Sun Aug 1",       what:"Full draft due",                                you:"Written comments on the draft during in-service week."},
    {key:"final",   when:"Sun Sep 5",       what:"Final essay due (clean copy)",                  you:"Read the final essay before the viva voce."},
    {key:"s3",      when:"Sep 6 to 16",     what:"Viva voce (final reflection session)",          you:"Hold the session. Fill in the RPF."},
    {key:"rs",      when:"Sun Sep 19",      what:"Reflective statement written in class",         you:""},
    {key:"pg",      when:"Tue Sep 21",      what:"Predicted grades due",                          you:"Send your predicted grade to the EE coordinator."},
    {key:"results", when:"Thu Sep 30",      what:"Grades released",                               you:""}
  ]
};
/* Fill any element with data-when="key" with that item's date. */
(function(){
  function fill(){
    var map = {}; (window.EE_TIMELINE.items||[]).forEach(function(i){ map[i.key]=i.when; });
    document.querySelectorAll("[data-when]").forEach(function(el){ var w = map[el.getAttribute("data-when")]; if(w) el.textContent = w; });
  }
  if(document.readyState === "loading") document.addEventListener("DOMContentLoaded", fill); else fill();
})();
