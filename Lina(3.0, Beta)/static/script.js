// Don't delete any files from the external JS files
document.addEventListener('DOMContentLoaded', () => {
    const chatDisplay = document.getElementById('chat');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send');

    let isSubmitting = false; // Flag to track form submission state

    sendButton.addEventListener('click', () => {
        if (!isSubmitting) {
            sendMessage();
            disableSubmission();
        }
    });
    
    userInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            if (!isSubmitting) {
                event.preventDefault(); // Prevent the default form submission behavior
                sendMessage();
                disableSubmission();
            }
        }
    });

    function loadingMessage() {
        const loaderDiv = document.createElement('div');
        loaderDiv.classList.add('loader');
        chatDisplay.appendChild(loaderDiv);
        isSubmitting = true
    }
    
    function loadedMessage() {
        const loaders = chatDisplay.querySelectorAll('.loader');
        loaders.forEach(loader => {
            loader.parentNode.removeChild(loader);
        });
        isSubmitting = false
    }  


    async function sendMessage() {
        const userMessage = userInput.value;
        userInput.value = '';
        if (userMessage.trim() !== '') {
            const userId = getOrCreateUserId(); // Get or create user ID
            processData(userMessage, userId);
            displayMessage(`<b style="font-size:16px">User</b><br> ${escapeHTML(userMessage)}`, 'user');
            displayMessage('', 'ai')
            loadingMessage();
            let response = await fetch('/get_response', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `user_id=${userId}&user_input=${encodeURIComponent(userMessage)}&continue_prompt=${false}&generative=${generative}`
            });
            let unfinishedchat = userMessage + ' ---'


            if (!generative){
                let responseData = await response.json();
                let responseMessage = responseData.response;
                appendMessageToChat(responseMessage)
            }

            while (generative) {
                let responseData = await response.json();
                let responseMessage = responseData.response;

                responseMessage = responseMessage.replace('<linebreak>', '\n')
                // console.log(responseMessage)

                unfinishedchat += responseMessage.replace('<b>Lina</b><br>', '') + ' '
                if (responseMessage.includes('---')) {
                    appendMessageToChat(responseMessage.replace('---', ''));
                    break;
                } else {
                    appendMessageToChat(responseMessage);
                    response = await fetch('/get_response', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: `user_id=${userId}&user_input=${encodeURIComponent(unfinishedchat)}&continue_prompt=${true}`
                    });
                }
            }
            loadedMessage();
        }
    }

    function escapeHTML(html) {
        const div = document.createElement('div');
        div.textContent = html;
        return div.innerHTML;
    }


    function displayMessage(message, sender) {
        const messageDiv = document.createElement('pre');
        messageDiv.classList.add(sender);
        messageDiv.innerHTML = message; // Allow HTML responses to work
        chatDisplay.appendChild(messageDiv);
        // Scroll to the bottom after adding a new message
        scrollToBottom();
    }

    let replacing = false
    function appendMessageToChat(message) {
        const preElements = chatDisplay.getElementsByTagName('pre');
        const newestPreElement = preElements[preElements.length - 1];
    

        if (!generative){
            if (message.includes("```")) {
                // Replace '<' with '&lt;' only inside the specific ``` block
                message = message.replace(/```([\s\S]*?)```/g, function(match, codeContent) {
                    codeContent = codeContent.replace(/</g, '&lt;');
                    return "<code id='code'>" + codeContent + "</code>";
                });
            }
        }
        

        if (replacing) {
            // Replace content inside <code> element
            const codeElement = newestPreElement.querySelector('#code');
            if (message.includes("/```")) {
                replacing = false;
                message = message.replace('/```', '')
            } if (codeElement) {
                codeElement.textContent += message + ' ';
            }
        } else {
            if (message.includes("```")) {
                replacing = true;
                message = message.replace("```", "<code id='code'>");
            }
            newestPreElement.innerHTML = newestPreElement.innerHTML + message + ' ';
        }

        scrollToBottom();
    }
    

    function scrollToBottom() {
        chatDisplay.scrollTop = chatDisplay.scrollHeight;
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