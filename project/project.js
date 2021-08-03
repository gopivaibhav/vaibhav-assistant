function news(){
    eel.trail()
}


function addText(msg){
    var data=document.getElementById("content");
    data.innerHTML+="<br>"+msg;
}
eel.expose(addText);

function toggle(c){
    var manual=document.getElementById(c);
    if(manual.style.display=='absolute'){
        manual.style.display='none'   
    }else{
        manual.style.display='block'
    }
    console.log(manual.style)
}

function Show() {
    let manual = document.getElementById("min");
    
    let btn=document.getElementById("man")
    if (btn.innerText=="Manual") {
        manual.style.display = "block";
        btn.innerText="Close";
        manual.style.animationName="wohoo";
        manual.style.animationDuration=".5s";
    } else {
        btn.innerText="Manual"
        manual.style.animationName="yesss";
        manual.style.animationDuration=".5s";
        
    }
    console.log(btn.innerText)
}
