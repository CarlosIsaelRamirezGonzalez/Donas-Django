document.addEventListener('DOMContentLoaded', function() {
    const popup = document.querySelector('.donuts-popup'); 
    const buyBtn = document.querySelectorAll('.buy-btn');
    const confirmBtn = document.querySelector('.donuts-popup-confirm');
    const closeBtn = document.getElementById('close-donuts-popup');

    closeBtn.addEventListener('click', function() {
        closeBtn.classList.remove('active');
    });

    buyBtn.forEach(buy => {
        buy.addEventListener('click', function() {
            popup.classList.add('active');
        });
    });
    
    confirmBtn.addEventListener('click', function() {
        popup.classList.remove('active');
    });

});
