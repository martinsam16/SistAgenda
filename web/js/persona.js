$(function () {

    eel.expose(Limpiar)
    function Limpiar(){
        $('#NOMPER').val('');
        $('#APEPER').val('');
        $('#DNIPER').val('');
        $('#USRPER').val('');
        $('#DOMPER').val('');
    }

    $("#btnreg").click(
        function () {
        eel.RegPerr($("#NOMPER").val(), $("#APEPER").val(), $("#DNIPER").val(), $("#USRPER").val() + "@" + $("#DOMPER").val());
        Limpiar;
        }
    );
    
    eel.expose(consoleJs);
    function consoleJs(x) {
        console.log(x);
    }

    eel.expose(AlertaJs);
    function AlertaJs(x) {
        alert(x)
    }
    var d = "";
    var cabecera = '<thead>' +
        '<tr>' +
        '<th>CÓDIGO</th>' +
        '<th>NOMBRES</th>' +
        '<th>APELLIDOS</th>' +
        '<th>DNI</th>' +
        '<th>E-MAIL</th>' +
        '</tr>' +
        '</thead>';

    eel.expose(LlenarTbl);
    function LlenarTbl(cod, nom, ape, dni, corr) {
        d += '<tbody>' +
            '<tr id="' + cod + '" onclick="rellenar(' + cod + ')">' +
            '<td>' + cod + '</td>' +
            '<td>' + nom + '</td>' +
            '<td>' + ape + '</td>' +
            '<td>' + dni + '</td>' +
            '<td>' + corr + '</td>' +
            '</tr>' +
            '</tbody>';
        $("#tabla").append(d);
        d = "";
    }

    $("#btnclear").click(
        function(){
            console.log("aaaa");
            Limpiar;
            
        }            
    );

    $("#btnedit").click(
        function(){
            console.log("ahah");
        }
        
    );

    $("#btnshow").click(
        function () {
            $("#tabla").empty();
            d += cabecera;
            eel.ShowPer();
            console.log("Show");
        }
    )
    /*
        document.querySelector("table").addEventListener("click", function (event) {
            console.log(event.target.innerText);
        }, false);
    */
    eel.expose(LlenarInpt)
    function LlenarInpt(nom, ape, dni, corr) {
        $('#NOMPER').val(nom);
        $('#APEPER').val(ape);
        $('#DNIPER').val(dni);
        var separado = corr.split("@");
        $('#USRPER').val(separado[0]);
        $('#DOMPER').val(separado[1]);

    }

    

});
function rellenar(x) {
    eel.llenar(x)

}
