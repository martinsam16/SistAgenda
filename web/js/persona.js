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

    
    eel.expose(AlertaJs); 
    function AlertaJs(x) {
        alert(x)
    }

}); 