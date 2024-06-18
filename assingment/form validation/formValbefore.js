function checkData(){
    let uid=document.getElementById("userid").value
    if(uid.trim()===""){
        document.getElementById("uiderror").innerHTML="user id is required"
        document.getElementById("uiderror").style.color="red"
    }
    else if(!uid.trim().match('^[a-z A-Z]{3,10}$')){
        document.getElementById("uiderror").innerHTML="user id must be in proper format"
        document.getElementById("uiderror").style.color="red"
    }
    else
    {
        document.getElementById("uiderror").innerHTML=""
    }


    
}

function Data(){
    let upass=document.getElementById("passid").value
    if(upass.trim()===""){
        document.getElementById("upasserror").innerHTML="password is required"
        document.getElementById("upasserror").style.color="red"
    }
    else if(!upass.trim().match('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\\W)(?!.*\\s).{8,16}$')){
        document.getElementById("upasserror").innerHTML="password must be in proper format"
        document.getElementById("upasserror").style.color="red"
    }
    else
    {
        document.getElementById("upasserror").innerHTML=""
    }
}
function number(){
    let unum=document.getElementById("numid").value
    if(unum.trim()===""){
        document.getElementById("unumerror").innerHTML="number is required"
        document.getElementById("unumerror").style.color="red"
    }
    else if(!unum.trim().match('^[0-9]{8,10}$')){
        document.getElementById("unumerror").innerHTML="number must be in proper format"
        document.getElementById("unumerror").style.color="red"
    }
    else
    {
        document.getElementById("unumerror").innerHTML=""
    }
}
function email(){
    let uemail=document.getElementById("emailid").value
    if(uemail.trim()===""){
        document.getElementById("uemailerror").innerHTML="email is required"
        document.getElementById("uemailerror").style.color="red"
    }
    else if(!uemail.trim().match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')){
        document.getElementById("uemailerror").innerHTML="email must be in proper format"
        document.getElementById("uemailerror").style.color="red"
    }
    else
    {
        document.getElementById("uemailerror").innerHTML=""
    }
}

function validateForm() {
    const radios = document.getElementsByName('gender');
    let formValid = false;

    for (let i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            formValid = true;
            break;
        }
    }

    if (!formValid) {
        alert('Please select your gender.');
        return false;
    }

    return true;
}