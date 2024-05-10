function toggleActiveClass(panel) {
    const itemDonuts = panel.querySelectorAll('.item-donut');

    itemDonuts.forEach(item => {
        item.classList.toggle('activate');
    });

    // panel.classList.toggle('rotate');

}