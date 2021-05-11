function createtransactions(){
    document.getElementById("createtransactionmodal").style.display = "flex";

}

function closecreatetransactions(){
    document.getElementById("createtransactionmodal").style.display = "none";

}

function filtermodal(){
    document.getElementById("filtermodal").style.display = "flex";

}

function closefiltermodal(){
    document.getElementById("filtermodal").style.display = "none";

}

var i;
window.onload = function(){
    i=0;
    console.log("loaded");
}



function showmenu(){

    if (i==0){
    document.getElementById("menu").style.display="flex";
    console.log(i);
    i=1;
    }
    else{
        document.getElementById("menu").style.display="none";
        console.log(i);
        i=0;
    }
}


