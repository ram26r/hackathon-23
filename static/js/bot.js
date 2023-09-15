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
    // Example: You can use AJAX or fetch to send the user message to the server
    fetch('/api/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
  const botResponses = data.responses;

  botResponses.forEach(response => {
    if (response.hasOwnProperty('text')) {
      // Handle text response
      const textResponse = response.text;
      addMessageToChat(textResponse, 'Chatbot');
    } else if (response.hasOwnProperty('image')) {
        // Handle image response
        const imageResponse = response.image;

        // Create an <img> element and set its source to the base64-encoded image data
        const imgElement = document.createElement('img');
        imgElement.src = `data:image/png;base64,${imageResponse}`;

        // Append the image to the chat or wherever you want to display it
        addImageToChat(imgElement, 'Chatbot');
    } else {
      // Handle other response types or custom payloads
      // Extract and display the relevant information from the response
      // Add appropriate code based on the response structure
    }
  });
})
.catch(error => {
  console.error('Error:', error);
});

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
