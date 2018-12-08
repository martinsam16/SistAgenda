$(function () {

    $("#btnreg").click(function () {
        eel.RegPerr($("#NOMPER").val(), $("#APEPER").val(), $("#DNIPER").val(), $("#USRPER").val() + "@" + $("#DOMPER").val());
        $('#NOMPER').val('');
        $('#APEPER').val('');
        $('#DNIPER').val('');
        $('#USRPER').val('');
        $('#DOMPER').val('');
    });

    eel.expose(consoleJs);
    function consoleJs(x) {
        console.log(x);
    }

    eel.expose(AlertaJs);
    function AlertaJs(x) {
        alert(x)
    }
    var d="";
    var cabecera = '<thead>'+
        '<tr>' +
        '<th>CÓDIGO</th>' +
        '<th>NOMBRES</th>' +
        '<th>APELLIDOS</th>' +
        '<th>DNI</th>' +
        '<th>E-MAIL</th>' +
        '</tr>'+
        '</thead>';

    eel.expose(LlenarTbl);
    function LlenarTbl(cod,nom,ape,dni,corr){
         d += '<tr>' +
                    '<td>' + cod + '</td>' +
                    '<td>' + nom + '</td>' +
                    '<td>' + ape + '</td>' +
                    '<td>' + dni + '</td>' +
                    '<td>' + corr + '</td>' +
             '</tr>';
         $("#tabla").append(d);
         d="";
    }
    $("#btnshow").click(
        function () {
            $("#tabla").empty();
            d+=cabecera;
            eel.ShowPer();
        }
    );

}); 