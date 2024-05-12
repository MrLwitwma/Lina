document.addEventListener('click', function() {
    // Get all buttons with class 'copy-button'
    var buttons = document.querySelectorAll('.copy-button');
    
    // Add click event listener to each button
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Get the code value from the data attribute of the button
            var code = button.getAttribute('data-code');
            
            // Get the corresponding div using the code value as the ID
            let div = document.getElementById(code);


            textData = div.textContent
            console.log(textData)

            // Use the Clipboard API to copy the selected text to the clipboard
            navigator.clipboard.writeText(textData)
                .then(function() {
                    showComplete(button);
                })
                .catch(function(err) {
                    console.error('Unable to copy text to clipboard', err);
                    alert('Unable to copy text to clipboard.');
                });
        });
    });
});

function showComplete(div){
    const temp = div.innerHTML
    div.innerHTML = `<svg fill="#000000" height="14px" width="14px" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 490 490" xml:space="preserve"><polygon points="452.253,28.326 197.831,394.674 29.044,256.875 0,292.469 207.253,461.674 490,54.528 "/></svg>`
    setTimeout(function(){
        div.innerHTML = temp
    }, 600)
}