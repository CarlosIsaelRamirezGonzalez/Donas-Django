window.addEventListener('DOMContentLoaded', (event) => {
    const messages = document.querySelectorAll('.message');
    let topOffset = 5; // Initial top offset in percentage

    messages.forEach((message, index) => {
        if (index === 0) {
            message.style.top = `${topOffset}%`;
        } else {
            const previousMessage = messages[index - 1];
            const previousMessageHeight = previousMessage.offsetHeight;
            const previousTop = parseFloat(previousMessage.style.top);

            topOffset = previousTop + (previousMessageHeight / window.innerHeight) * 100 + 1; // Adding 1% for margin
            message.style.top = `${topOffset}%`;
        }
    });
});