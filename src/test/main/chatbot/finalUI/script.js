// Function to add a new message to the chat history
function addMessageToChat(message, sender) {
    const chatHistory = document.getElementById('chat-history');
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message';

    // Add CSS class based on the message sender
    if (sender === 'User') {
        messageContainer.classList.add('user-message');
    } else {
        messageContainer.classList.add('system-message');
    }

    messageContainer.innerHTML = message;
    chatHistory.appendChild(messageContainer);
    chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to the bottom of the chat history
}

// Function to handle user input and send it to the chatbot
function handleUserInput() {
    const userInput = document.getElementById('chatMessageInput');
    const message = userInput.value.trim();
    if (message !== '') {
        addMessageToChat(message, 'User');
        // Send the message to the chatbot backend/API and handle the response
        // Example: You can make an AJAX request or use a chatbot framework/client library
        // Here, we'll just simulate a response after a delay
        setTimeout(function() {
            const response = 'This is the chatbot response';
            addMessageToChat(response, 'Chatbot');
        }, 1000);
        userInput.value = '';
    }
}

// Add event listener to the send button
document.getElementById('send-btn').addEventListener('click', handleUserInput);

// Add event listener to handle Enter key press in the input field
document.getElementById('chatMessageInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        handleUserInput();
    }
});
