/* Extended Essay hub — fills in the step header and previous/next links on a step page.
   The page sets <body data-step="N"> and includes data/steps.js before this file. */
(function(){
  var n = parseInt(document.body.getAttribute("data-step"),10);
  var steps = window.EE_STEPS || [], phases = window.EE_PHASES || [];
  var me = steps.filter(function(s){return s.n===n;})[0];
  if(!me) return;
  var phase = phases.filter(function(p){return p.id===me.phase;})[0];

  var head = document.getElementById("stepno");
  if(head) head.innerHTML = '<span class="pill">'+(n===0 ? "Start" : "Step "+n+" of "+(window.EE_STEPS[window.EE_STEPS.length-1].n))+'</span>'+(phase?phase.name:"");

  var nav = document.getElementById("stepnav");
  if(!nav) return;
  var prev = steps.filter(function(s){return s.n===n-1;})[0];
  var next = steps.filter(function(s){return s.n===n+1;})[0];
  function link(s, cls, word){
    if(!s) return '<span></span>';
    var label = s.n===0 ? s.title : "Step "+s.n+": "+s.title;
    if(!s.live) return '<span class="'+cls+' soon"><a aria-disabled="true"><small>'+word+' · coming soon</small>'+label+'</a></span>';
    return '<a class="'+cls+'" href="../step-'+s.n+'/"><small>'+word+'</small>'+label+'</a>';
  }
  nav.innerHTML = link(prev,"prev","← Previous") + link(next,"next","Next →");
})();
