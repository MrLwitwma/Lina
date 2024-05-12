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
        let class_id = generateUserId() + generateUserId() + generateUserId();
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(sender);
        messageDiv.setAttribute('id', class_id);
        if (sender === 'ai' && message.includes("```")) {
            // Replace '<' with '&lt;' only inside the specific ``` block
            message = message.replace(/```([\s\S]*?)```/g, function(match, codeContent) {
                codeContent = codeContent.replace(/</g, '&lt;');
                return "<pre><code id='code'>" + codeContent + "</code></pre>";
            });
        }
        messageDiv.innerHTML = message; // Allow HTML responses to work
        if (sender === 'ai'){
            messageDiv.innerHTML += `<div id="bottom-options"><span class="copy-button" title="Copy" data-code="${class_id}"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-md"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 3.5C10.8954 3.5 10 4.39543 10 5.5H14C14 4.39543 13.1046 3.5 12 3.5ZM8.53513 3.5C9.22675 2.3044 10.5194 1.5 12 1.5C13.4806 1.5 14.7733 2.3044 15.4649 3.5H17.25C18.9069 3.5 20.25 4.84315 20.25 6.5V18.5C20.25 20.1569 19.1569 21.5 17.25 21.5H6.75C5.09315 21.5 3.75 20.1569 3.75 18.5V6.5C3.75 4.84315 5.09315 3.5 6.75 3.5H8.53513ZM8 5.5H6.75C6.19772 5.5 5.75 5.94772 5.75 6.5V18.5C5.75 19.0523 6.19772 19.5 6.75 19.5H17.25C18.0523 19.5 18.25 19.0523 18.25 18.5V6.5C18.25 5.94772 17.8023 5.5 17.25 5.5H16C16 6.60457 15.1046 7.5 14 7.5H10C8.89543 7.5 8 6.60457 8 5.5Z" fill="currentColor"></path></svg></span>`;
        }
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