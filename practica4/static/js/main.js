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
        
        var pedido = $(this).children().children('.mb-1').text();
        var mesa = $(this).children().children('.text-muted').text();
        $('#tituloModal').text(pedido);        
        $('#tituloMesa').text(mesa);        

        $('.modal-body').empty();

        var pedidos = $(this).children('p').clone().appendTo($('.modal-body'));
        
        pedidos.each(function( index ) {
            if($( this ).hasClass( "pedido-Pendiente" )){
                icon = '<span style="font-size: 20px;" class="material-icons aling-icon">access_time</span>';
                estado = 'Pendiente'
            } else{
                icon = '<span style="font-size: 20px;" class="material-icons aling-icon">check</span>';                
                estado = 'Listo'
            }
            $(this).addClass('pendiente-item-form');
            $(this).prepend(icon);
            $(this).append(' - ' + estado);
            var idPedido = $(this).children('.id-item').text()

            if($( this ).hasClass( "pedido-Pendiente" )){
                $(this).append('<div class="custom-control custom-checkbox text-muted float-right"><input type="checkbox" name="id-items" value="'+ idPedido +'" class="custom-control-input" id="customCheck'+ index +'"><label class="custom-control-label" for="customCheck'+ index +'">Listo</label></div>');
            } 
        });
        
   
    });

    $( "input[type='checkbox']" ).prop( "checked", function( val ) {
        console.log(val);
    });
});