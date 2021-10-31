function stopAnim(){
    $(".animationHeader").fadeOut( 1600, "linear" );
    $("#content").fadeIn(1600, "linear");
}

setTimeout(function() { stopAnim(); }, 5000);








