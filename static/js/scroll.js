$(window).on("load", function() {
    setTimeout(function() {$('html, body').animate({
       scrollTop: $("#jumbo-header").offset().top + $("#jumbo-header").outerHeight(true) - 200},
       200,
       "swing"
    )},
    1000);
});
