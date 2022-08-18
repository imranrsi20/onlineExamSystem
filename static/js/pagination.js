const galleryItems = document.querySelector(".gallery-items").children;
console.log(galleryItems)
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const page = document.querySelector(".page-num");

const maxItem = 2;
let index = 1;
const pagination = Math.ceil(galleryItems.length/maxItem);
console.log(pagination)
prev.addEventListener("click",function (){
    index--;
    check();
    showItem();
})
next.addEventListener("click",function (){
    index++;
    check();
    showItem();
})

function check(){
    if(index==pagination){
        next.classList.add(".hide");
    }
    else{
        next.classList.remove(".hide")
    }
    if(index==1){
        prev.classList.add(".hide");
    }
    else{
        prev.classList.remove(".hide");
    }
}

function showItem(){
    for(let i=0;i<galleryItems.length;i++){
        galleryItems[i].classList.remove("show");
        galleryItems[i].classList.add("hide");

        if(i>=(index*maxItem)-maxItem && i<index*maxItem){
            galleryItems[i].classList.remove("hide");
            galleryItems[i].classList.add("show");
        }
        page.innerHTML = index;
    }

}

window.onload = function (){
    showItem();
    check();
}