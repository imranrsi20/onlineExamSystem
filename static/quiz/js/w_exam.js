console.log("hello world")
const url=window.location.href
const quizBox=document.getElementById('quiz-box')
const scoreBox=document.getElementById('score-box')
const resultBox=document.getElementById('result-box')
$.ajax({
   type: 'GET',
   url: `${url}data`,

   success:function (resp){
       //console.log(resp)
       const data=resp.data
       //console.log(data)
       data.forEach(el =>{
           for(const[question,answers] of Object.entries(el)){
               //console.log(question)
               //console.log(answers)
               quizBox.innerHTML+=`
               
               <div class="question">
                    <b>${question}</b>
               </div>
               `

                   quizBox.innerHTML+=`
                   <div class="answer">
                       <textarea class="ans" name="${question}" value="" style="height: 200px;width: 400px;"></textarea>
                       
                   </div>
                   `

           }
       })
   },
    error:function (error){
       console.log(error)
    },
});





const quizForm=document.getElementById('quiz-form')
const csrf=document.getElementsByName('csrfmiddlewaretoken')


const sendData = ()=>{
    const elements=[...document.getElementsByClassName('ans')]
    const data={}
    data['csrfmiddlewaretoken']=csrf[0].value
    elements.forEach(el=>{

            data[el.name]=el.value

    })

    $.ajax({
        type:'POST',
        url: `${url}save/`,
        data:data,
        success:function (resp){
            //console.log(resp)
            //const result = resp.results
            //console.log(result)
            quizForm.classList.add('not-visible')

        },
        error:function (error){
            console.log(error)
        },
    })
}

quizForm.addEventListener('submit',e=>{
    e.preventDefault()
    sendData()
})


