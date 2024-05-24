document.addEventListener('DOMContentLoaded', function() {
    const popup = document.querySelector('.donuts-popup'); 
    const buyBtns = document.querySelectorAll('.buy-btn');
    const closeBtn = document.getElementById('close-donuts-popup');
    const donutIdInput = document.getElementById('donut-id-input');
    const popupForm = document.getElementById('popup-form');

    closeBtn.addEventListener('click', function() {
        popup.classList.remove('active');
    });

    buyBtns.forEach(buyBtn => {
        buyBtn.addEventListener('click', function(event) {
            const donutCard = event.currentTarget.closest('.donut-card');
            const donutId = donutCard.dataset.donutId;
            
            // Set the donut ID in the hidden input field
            donutIdInput.value = donutId;
            
            // Update the form action with the correct donut ID
            popupForm.action = popupForm.action.replace('0', donutId);
            
            popup.classList.add('active');
        });
    });

    closeBtn.addEventListener('click', function() {
        popup.classList.remove('active');
    });
});
