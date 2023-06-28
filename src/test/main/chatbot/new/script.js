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

  const messageText = messageContainer.innerText;
  const messageLength = messageText.length;

  const maxWidth = 300; // Define the maximum width for the message box
  const minWidth = 20; // Define the minimum width for the message box
  const characterWidth = 10; // Define an approximate width per character

  const calculatedWidth = Math.min(maxWidth, minWidth + messageLength * characterWidth);
  messageContainer.style.width = calculatedWidth + 'px';
}

// Function to handle user input and send the message
function handleUserInput() {
  const userInput = document.getElementById('user-input');
  const message = userInput.value;
  if (message.trim() !== '') {
    addMessageToChat(message, 'User');
    // Call the chatbot API or perform desired actions with the user message
    // Example: You can call a chatbot API here to get the response
    // Once you receive the response, call addMessageToChat(response, 'Chatbot');
    setTimeout(function() {
            const response = 'This is the chatbot response';
            addMessageToChat(response, 'Chatbot');
        }, 1000);
    userInput.value = ''; // Clear the input field
  }
}

// Event listener for the send button
const sendButton = document.getElementById('send-btn');
sendButton.addEventListener('click', handleUserInput);

// Event listener for Enter key press in the input field
const userInput = document.getElementById('user-input');
userInput.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    handleUserInput();
  }
});
