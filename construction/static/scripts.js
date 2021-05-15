function createtransactions(){
    document.getElementById("createtransactionmodal").style.display = "flex";

}

function xls_modal(){
    document.getElementById("xls_modal").style.display = "flex";

}

function close_xls_modal(){
    document.getElementById("xls_modal").style.display = "none";

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


