$(document).ready(function () {
    $('.product-item').click(function (e) { 

        if($('.order-list:last-child').hasClass('product-item')){
            $('.order-list:last-child').remove();
        }
        $(this).clone().appendTo('.order-list');

        
    });
});