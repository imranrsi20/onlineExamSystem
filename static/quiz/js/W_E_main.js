console.log("hello imran, i am working....")
const modalBtns=[...document.getElementsByClassName('modal-button')]
const modalBody=document.getElementById('modal-body-confirm')
const startBtn=document.getElementById('start-button')
const url=window.location.href
modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click', ()=>{
    const pk=modalBtn.getAttribute('data-pk')
    const subject=modalBtn.getAttribute('data-subject')
    const numquestions=modalBtn.getAttribute('data-questions')
    const scoretopass=modalBtn.getAttribute('data-pass')
    const time=modalBtn.getAttribute('data-time')


    modalBody.innerHTML=`
    <div class="h5 mb-3">Are you sure,you want to begin "<b>${subject}</b>"?</div>
    <div class="text-muted">
        <ul>
            <li>number of questions: <b>${numquestions}</b></li>
            <li>Score to pass: <b>${scoretopass}%</b></li>
            <li>Time: <b>${time} min</b></li>
        </ul>
        
    </div>`
   
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    });
    

}));