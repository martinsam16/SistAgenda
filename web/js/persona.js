$(function () {
    var codper;
    eel.expose(Limpiar);
    function Limpiar(){
        $('#NOMPER').val('');
        $('#APEPER').val('');
        $('#DNIPER').val('');
        $('#USRPER').val('');
        $('#DOMPER').val('');
    }

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

    $("#btnreg").click(
        function () {
        eel.RegPerr($("#NOMPER").val(), $("#APEPER").val(), $("#DNIPER").val(), $("#USRPER").val() + "@" + $("#DOMPER").val());
        Limpiar();
        }
    );

    $("#btnclear").click(
        function(){
            Limpiar();
            codper = "";
        }
        
    );

    $("#btnshow").click(
        function () {
            $("#tabla").empty();
            d += cabecera;
            eel.ShowPer();
        }
    )

    $("#btnelim").click(
        function(){
            eel.ElimPer(codper);
            codper = "";
            Limpiar();
        }
    );

    /*
        document.querySelector("table").addEventListener("click", function (event) {
            console.log(event.target.innerText);
        }, false);
    */
    eel.expose(LlenarInpt)
    function LlenarInpt(cod, nom, ape, dni, corr) {
        codper=cod;
        $('#NOMPER').val(nom);
        $('#APEPER').val(ape);
        $('#DNIPER').val(dni);
        var separado = corr.split("@");
        $('#USRPER').val(separado[0]);
        $('#DOMPER').val(separado[1]);

    }

    $(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip();
        });
     });
function rellenar(x) {
    eel.llenar(x);
}
