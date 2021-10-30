(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
    .forEach(function (form) {
    form.addEventListener('submit', function (e) {
        const regex = new RegExp('^[0-9]+$');
        var number = $("#coll").val();
        if (!form.checkValidity()) {
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
    }, false)
    })
})()




