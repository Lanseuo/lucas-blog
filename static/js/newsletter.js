$(document).ready(function () {
  // Newsletter form
  $('#newsletter-form').on('submit', function (event) {

    // Hide (old) alert boxes
    $('#newsletter-success').hide();
    $('#newsletter-error').hide();
    $('#newsletter-success p').text('');
    $('#newsletter-error p').text('');

    $('.newsletter-spinner').show();

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
          $('.newsletter-spinner').hide();
          $('#newsletter-alert').css('border', '3px solid rgb(218, 13, 61)');
          $('#newsletter-alert p').text(data.error);
        } else if (data.success == 'subscribed') {
          localStorage.setItem('subscribedNewsletter', true);
          $('.newsletter-spinner').hide();
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

function submitNewsletterModalForm() {
  // Hide (old) alert boxes
  $('#newsletter-modal-success').hide();
  $('#newsletter-modal-error').hide();
  $('#newsletter-modal-success p').text('');
  $('#newsletter-modal-error p').text('');

  $('.newsletter-modal-spinner').show();

  // Post data to api
  $.ajax({
      data: {
        source: $('#newsletter-modal-source').val(),
        mail: $('#newsletter-modal-mail').val(),
      },
      type: 'POST',
      url: 'https://lanseuo.herokuapp.com/newsletter/subscribe',
    })

    .done(function (data) {
      if (data.error) {
        $('.newsletter-modal-spinner').hide();
        $('#newsletter-modal-alert').css('border', '3px solid rgb(218, 13, 61)');
        $('#newsletter-modal-alert p').text(data.error);
      } else if (data.success == 'subscribed') {
        localStorage.setItem('subscribedNewsletter', true);
        $('.newsletter-modal-spinner').hide();
        $('#newsletter-modal-alert').css('border', '3px solid rgb(66, 181, 131)');
        $('#newsletter-modal-alert p').append('Vielen Dank fürs Anmelden!');

        // Clear input fields
        $('#newsletter-modal-mail').val('');
      }
      $('#newsletter-modal-alert').fadeIn(500);
      $('#newsletter-modal-alert').css('display', 'block');
    });

  return false;
}
