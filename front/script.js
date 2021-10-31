function stopAnim(){
    $(".animationHeader").fadeOut( 1600, "linear" );
    $("#content").fadeIn(1600, "linear");
}

setTimeout(function() { stopAnim(); }, 5000);


(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
    .forEach(function (form) {
    form.addEventListener('submit', function (e) {
        e.preventDefault()
        e.stopPropagation()
        const regex = new RegExp('^[0-9]+$');
        var collHave = $("#collHave").val();
        var collSave = $("#collSave").val();
        $(".invalid-back").css("display", "none");
        if (!form.checkValidity()) {
            
        }

        form.classList.add('was-validated')

        if(regex.test(collHave)){
            if(regex.test(collSave)){
                
            }
            else{
                document.getElementById("collSave").setCustomValidity('invalid')
            }
        }
        else{
            document.getElementById("collHave").setCustomValidity('invalid')
        }
    }, false)
    })
})()




