$(document).ready(function () {
    $('#items-number').val("");    

    $('.product-item').click(function (e) { 

        $('.null-item').slideUp();
        $(this).clone().appendTo('.order-list');

        var itemsPedidos = $('#items-number').val();
        var itemNuevo = $(this).children('.d-none').text();
        
        if( $('#items-number').val() != "" ){
            $('#items-number').val( itemsPedidos + "," + itemNuevo);
        } else{
            $('#items-number').val(itemNuevo);
        }
    });
});