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
                <form id="newsletter-modal-form" onSubmit="return subscribedToNewsletter()" action="https://app.mailerlite.com/webforms/submit/s4t1t7" data-code="s4t1t7" method="post" target="_blank">
                    <input type="email" name="fields[email]" placeholder="E-Mail" autocomplete="email" x-autocompletetype="email">
                    <input type="hidden" name="ml-submit" value="1">
                    <button id="newsletter-button" type="submit">Abonnieren</button>
                </form>`);
        }, 3000);
    }
}
