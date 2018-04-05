$(window).ready(function() {
  let headerTitle = $('#header-content h1 a').text();
  console.log(headerTitle);

  $(window).scroll(function(event) {
    $('nav').css('position', 'fixed');
    if ($(window).scrollTop() > 100) {
      $('nav').addClass('visible');
      $('#header-content h1').addClass('go-to-navbar');
      $('#header-content h1 a').text('Lucas Blog');
    } else {
      $('nav').removeClass('visible');
      $('#header-content h1').removeClass('go-to-navbar');
      $('#header-content h1 a').text(headerTitle);
    }
  });
});
