$(document).ready(function () {
    $('.product-item').click(function (e) { 

        $('.null-item').fadeOut();

        $(this).clone().appendTo('.order-list');

        
    });
});