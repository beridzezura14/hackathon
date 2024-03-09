

const btnReg = document.querySelector(".btn-reg");

const formFirst = document.querySelector(".form-first");
const formSecond = document.querySelector(".form-second");
const btnReg1 = document.querySelector("#btn-reg1");



btnReg.addEventListener("click", function(e){
    const text = document.querySelector("#text").value;
    const email = document.querySelector("#email").value;
    const pass = document.querySelector("#pass").value;
    e.preventDefault()

    if(text.length > 0 && email.includes('@') && email.includes('.') && pass.length > 4){
            formFirst.style.display = "none"
            formSecond.style.display = "block"
       }


})
btnReg1.addEventListener("click", function(e){
    e.preventDefault()

    const text1 = document.querySelector("#text").value;
    const pass1 = document.querySelector("#pass").value;

    if(btnReg.text === text1 && btnReg.pass === pass1){
        console.log("hello");
    }

})