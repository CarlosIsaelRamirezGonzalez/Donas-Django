document.addEventListener('DOMContentLoaded', function() {
    const donutCards = document.querySelectorAll('.donut-card');

    donutCards.forEach(card => {
        card.addEventListener('click', function() {
            this.classList.toggle('active');
        });
    });
});    