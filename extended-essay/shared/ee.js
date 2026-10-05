/* Extended Essay hub — shared theme toggle.
   Uses the same storage key as the classroom-games homepage ("sst-theme"),
   so a light/dark choice made anywhere on the site carries over.
   Include in <head> so the saved theme applies before first paint. */
(function(){
  var root=document.documentElement;
  try{var saved=localStorage.getItem("sst-theme"); if(saved) root.dataset.theme=saved;}catch(e){}
  if(!root.dataset.theme) root.dataset.theme="dark";
  document.addEventListener("DOMContentLoaded",function(){
    var btn=document.getElementById("themeBtn");
    if(!btn) return;
    function paint(){btn.textContent=root.dataset.theme==="light"?"☾":"☀";
      btn.setAttribute("aria-label",root.dataset.theme==="light"?"Switch to dark theme":"Switch to light theme");}
    paint();
    btn.addEventListener("click",function(){
      var next=root.dataset.theme==="light"?"dark":"light";
      root.dataset.theme=next; paint();
      try{localStorage.setItem("sst-theme",next);}catch(e){}
    });
  });
})();
