$(window).on("scroll", check_if_in_view);

function check_if_in_view() {
  var $elements = $(".animate-element");

  var window_height = $(window).height();
  var window_top = $(window).scrollTop();
  var window_bottom = window_height + window_top;

  if (window_top > (window_height / 5.0)) {
    $(".divider:first").css({
      "transition": "1.2s ease",
      "width": "75%"
    })
  }

  if (window_top > (window_height / 4.0)) {
    $("header").addClass("inview");
  }


  $.each($elements, function() {
    var $element = $(this);
    var element_height = $element.outerHeight();
    var element_top = $element.offset().top;
    var element_bottom = element_height + element_top;
    var element_mid = (element_top + element_bottom) / 2.0;
    var trigger = (element_mid + element_bottom) / 2.0;

    if (trigger <= window_bottom) {
      $element.addClass("slide");
    }

  })

}
