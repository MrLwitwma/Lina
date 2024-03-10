document.addEventListener('DOMContentLoaded', () => {
    const chatDisplay = document.getElementById('chat');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send');

    sendButton.addEventListener('click', sendMessage);

    userInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
            event.preventDefault(); // Prevent the default form submission behavior
        }
    });

    function loading_message() {
        const loaderDiv = document.createElement('div');
        loaderDiv.classList.add('loader');
        chatDisplay.appendChild(loaderDiv);
    }
    
    function loaded_message() {
        const loaders = chatDisplay.querySelectorAll('.loader');
        loaders.forEach(loader => {
            loader.parentNode.removeChild(loader);
        });
    }  

    async function sendMessage() {
        const userMessage = userInput.value;
        userInput.value = '';
        if (userMessage.trim() !== '') {
            const userId = getOrCreateUserId(); // Get or create user ID
            displayMessage(`<b style="font-size:16px"> User </b><br>${escapeHTML(userMessage)}`, 'user');
            loading_message();
            const response = await fetch('/get_response', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `user_id=${userId}&user_input=${encodeURIComponent(userMessage)}`
            });
            const responseData = await response.json();
            displayMessage(responseData.response, 'ai'); // Allow HTML responses to work
            loaded_message();
        }
    }

    function escapeHTML(html) {
        const div = document.createElement('div');
        div.textContent = html;
        return div.innerHTML;
    }

    function scrollToBottom() {
        chatDisplay.scrollTop = chatDisplay.scrollHeight;
    }

    function displayMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(sender);
        messageDiv.innerHTML = message; // Allow HTML responses to work
        chatDisplay.appendChild(messageDiv);

        // Scroll to the bottom after adding a new message
        scrollToBottom();
    }
});

function getOrCreateUserId() {
    let userId = getCookie('user_id');
    if (!userId) {
        userId = generateUserId();
        setCookie('user_id', userId, 365); // Set the user ID cookie to expire in 365 days
    }
    return userId;
}

function generateUserId() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    const length = 8;
    let result = '';
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

function setCookie(name, value, days) {
    let expires = '';
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for(let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1, cookie.length);
        }
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}