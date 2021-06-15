function news(){
    eel.trail()
}


function addText(msg){
    var data=document.getElementById("content");
    data.innerHTML+="<br>"+msg;
}
eel.expose(addText);