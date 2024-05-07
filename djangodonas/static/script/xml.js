document.getElementById('register-btn').addEventListener('click', function() {
    // Obtener valores de los inputs
    const email = document.getElementById('email-input').value;
    const username = document.getElementById('username-input').value;
    const password = document.getElementById('password-input').value;
    const confirmPassword = document.getElementById('confirm-password-input').value;

    const xmlDoc = document.implementation.createDocument(null, 'registration');
    const registrationElement = xmlDoc.getElementsByTagName('registration')[0];

    const emailElement = xmlDoc.createElement('email');
    emailElement.textContent = email;

    const usernameElement = xmlDoc.createElement('username');
    usernameElement.textContent = username;

    const passwordElement = xmlDoc.createElement('password');
    passwordElement.textContent = password;

    const confirmPasswordElement = xmlDoc.createElement('confirmPassword');
    confirmPasswordElement.textContent = confirmPassword;

    registrationElement.appendChild(emailElement);
    registrationElement.appendChild(usernameElement);
    registrationElement.appendChild(passwordElement);
    registrationElement.appendChild(confirmPasswordElement);

    console.log(new XMLSerializer().serializeToString(xmlDoc));
});
