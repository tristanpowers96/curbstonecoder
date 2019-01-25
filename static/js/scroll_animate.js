$(document).ready(function() {

  $(".tab").click(function() {
    if (!$(this).hasClass("hover")) {
      $(this).toggleClass("hover");
    }
  })

  $(".tab").hover(function() {
    $(this).toggleClass("hover");
  })

  $(".content-box").hover(function() {
    $(this).toggleClass("hover");
  })

  $(".tab-item").hover(function() {
    $(this).toggleClass("hover");
  })

  $(window).on("scroll", check_if_in_view);

  function check_if_in_view() {
    var $elements = $(".animate-element");

    var window_height = $(window).height();
    var window_top = $(window).scrollTop();
    var window_bottom = window_height + window_top;

    if (window_top > (window_height / 5.0)) {
      $(".divider:first").addClass("inview");
    }

    if (window_top > (window_height / 4.0)) {
      $("header").addClass("inview");
      $(".info").addClass("slide");
      $(".info .animate-element").addClass("slide");
    }

    $.each($elements, function() {
      var $element = $(this);
      var element_height = $element.outerHeight();
      var element_top = $element.offset().top;
      var element_bottom = element_height + element_top;
      var element_mid = (element_top + element_bottom) / 2.0;
      var trigger = (element_mid + element_bottom) / 2.0;

      if (trigger <= window_bottom) {
        var height = $(".info .animate-element.slide").outerHeight();
        $(".info").css({"height": height + 20});
        $element.addClass("slide");
      }

    })

  }
})
