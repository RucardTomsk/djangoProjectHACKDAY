'use strict'
var form = document.getElementById("form");
form.addEventListener('submit', function (e) {

    const regex = new RegExp('^[0-9]+$');
    var number = $("#coll").val();
    
    if(!form.checkValidity())
    {
        e.preventDefault()
        e.stopPropagation()
        
    }
    form.classList.add('was-validated')
    if(regex.test(number)){
        console.log("Ok");
    }
    else{
        e.preventDefault()
        e.stopPropagation()
    }

});