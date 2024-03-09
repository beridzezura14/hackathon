const btnReg = document.querySelector(".btn-reg");

const formFirst = document.querySelector(".form-first");
const formSecond = document.querySelector(".form-second");
const btnReg1 = document.querySelector("#btn-reg1");

btnReg1.addEventListener("click", function(e){
    e.preventDefault()
    const text = document.querySelector("#text").value;
    const email = document.querySelector("#email").value;
    const pass = document.querySelector("#pass").value;

    const text1 = document.querySelector("#text").value;
    const pass1 = document.querySelector("#pass").value;

    // personName = text
    // password = pass

    if(text.length > 0 && email.includes('@') && email.includes('.') && pass.length > 4){
        console.log("first step");
       }


    if(text === text1 && pass === pass1){
        formFirst.style.display = "none"
        formSecond.style.display = "none"
    }

})