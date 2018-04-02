$(document).ready(function () {
  // Newsletter form
  $('#newsletter-form').on('submit', function (event) {

    // Hide (old) alert boxes
    $('#newsletter-success').hide();
    $('#newsletter-error').hide();
    $('#newsletter-success p').text('');
    $('#newsletter-error p').text('');

    // Post data to api
    $.ajax({
        data: {
          source: $('#newsletter-source').val(),
          mail: $('#newsletter-mail').val(),
        },
        type: 'POST',
        url: 'https://lanseuo.herokuapp.com/newsletter/subscribe',
      })

      .done(function (data) {
        if (data.error) {
          $('#newsletter-alert').css('border', '3px solid rgb(218, 13, 61)');
          $('#newsletter-alert p').text(data.error);
        } else if (data.success == 'subscribed') {
          $('#newsletter-alert').css('border', '3px solid rgb(66, 181, 131)');
          $('#newsletter-alert p').append('Vielen Dank fürs Anmelden!');

          // Clear input fields
          $('#newsletter-mail').val('');
        }
        $('#newsletter-alert').fadeIn(500);
        $('#newsletter-alert').css('display', 'block');
      });

    event.preventDefault();
  });

  // Close alert if button (x) is pressed
  $('.closebtn').click(function () {
    $(this).parent().fadeOut(500);
  });
});
