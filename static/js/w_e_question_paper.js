 window.onload = initiall;
         var saveansButton;
         var btn_end;
         function initiall(){
             btn_end = document.getElementById('submitanswer')
             btn_end.style.display="none";
             saveansButton = document.getElementById('save_ans');
             saveansButton.onclick = saveans;
         }
         function saveans(){
             var Ans = $('#ans').val();
             var q = document.getElementById('qt').innerText;
             var s = document.getElementById('subject').innerText;
             var btn_sub=document.getElementById('save_ans')

             btn_sub.disabled=true;
             btn_end.style.display="block";
             var req = new XMLHttpRequest();
             var url ='/saveans?ans='+s+','+q+','+Ans;
             req.open("GET",url,true);
             req.send()
         }