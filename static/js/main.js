$(window).ready(function () {
    $('#mail-link').attr('href', 'mailto:co' + 'ntact@lu' + 'cas.hild.def'.substring(0, 12 - 1));
    $('.modal-close').click(() => $('.modal').css('display', 'none'));
    initNewsletterModal()
})

function showModal(title, content) {
    $('.modal').css('display', 'table');
    $('.modal-title').text(title);
    $('.modal-body').html(content);
}

function initNewsletterModal() {
    // Value not set yet
    if (localStorage.getItem('visited') == null) {
        localStorage.setItem('visited', '0');
    }

    localStorage.setItem('visited', parseInt(localStorage.getItem('visited')) + 1);

    if (localStorage.getItem('visited') == 2 || (localStorage.getItem('visited') == 10 && !localStorage.getItem('subscribedNewsletter'))) {
        setTimeout(() => {
            showModal('Abonniere meinen Newsletter', `
      <p>Möchtest Du auf dem Laufendem bleiben? Du wirst maximal einmal im Monat eine E-Mail mit meinen neusten Artikel erhalten. Außerdem erfährst Du, welche Artikel ich diesen Monat gelesen und mir besonders gut gefallen haben.</p>
      <form id="newsletter-modal-form" onSubmit="return submitNewsletterModalForm()">
        <div id="newsletter-modal-alert" class="alert" style="display: none;">
          <span class="closebtn" onclick="$(this).parent().fadeOut(500);">&times;</span>
          <p></p>
        </div>

        <div class="newsletter-modal-spinner">
          <div class="bounce1"></div>
          <div class="bounce2"></div>
          <div class="bounce3"></div>
        </div>

        <input id="newsletter-modal-source" name="source" value="blog-modal" type="hidden">
        <input id="newsletter-modal-mail" name="mail" placeholder="Deine Mail" required="" type="text"><br>
        <button id="newsletter-modal-button" type="submit">Abonnieren</button>
      </form>`);
        }, 3000);
    }
}
