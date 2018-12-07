$(function () {
    
    $("#btnreg").click(function () {
        eel.RegPer($("#NOMPER").val(), $("#APEPER").val(), $("#DNIPER").val());
        $('#NOMPER').val('');
        $('#APEPER').val('');
        $('#DNIPER').val('');
    });
    
    $("#btnshow").click(
        function () {
            eel.ShowPer();
        }
    );

    /*
    eel.expose(say_hello_js);               // Expose this function to Python
    function say_hello_js(x) {
        console.log("Hello from " + x);
    }
    say_hello_js("Javascript World!");
    */
}); 