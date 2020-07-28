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

    $(".pendiente-item").click(function (e) { 
        e.preventDefault();
        
        var titulo = $(this).children().children('.mb-1').text();
        titulo += "-"
        titulo += $(this).children().children('.text-muted').text();
        $('#tituloModal').text(titulo);        
        
        $('.modal-body').empty();

        var pedidos = $(this).children('p').clone().appendTo($('.modal-body'));
        
        pedidos.each(function() {
            if($( this ).hasClass( "pedido-Pendiente" )){
                icon = '<span style="font-size: 20px;" class="material-icons aling-icon">access_time</span>';
            } else{
                icon = '<span style="font-size: 20px;" class="material-icons aling-icon; background: #2fb191;">check</span>';                
            }
            $(this).prepend(icon);
          })

        console.log(pedidos)
    });
});