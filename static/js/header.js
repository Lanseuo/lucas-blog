$(window).ready(function() {
  $(window).scroll(function(event) {
    $('nav').css('position', 'fixed');
    if ($(window).scrollTop() > 100) {
      $('nav').addClass('visible');
      $('#header-content h1').addClass('go-to-navbar');
    } else {
      $('nav').removeClass('visible');
      $('#header-content h1').removeClass('go-to-navbar');
    }
  });
});
