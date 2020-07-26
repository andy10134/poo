$(document).ready(function () {
    $('#items-number').val("");    
    $('#total').val("");   

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

        var total = parseInt($('#total').val());
        var precio = parseInt($(this).children('.badge-success').children('.price').text());
        
        if( $('#total').val() != "" ){
            $('#total').val( total + precio);
        } else{
            $('#total').val(precio);
            $('#final-price').text("");
        }

        $('#final-price').text($('#total').val());
       
    });
});