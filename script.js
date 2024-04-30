function sendMessage() {
  var sound = document.getElementById("messageSound");
  sound.play();

  var userInput = document.getElementById("user-input").value.trim();
  if (userInput !== "") {
    appendMessage("user", userInput);
    document.getElementById("user-input").value = "";
    fetchResponse(userInput);
  }
}

function appendMessage(sender, message) {
  var chatContainer = document.getElementById("chat-container");
  var messageContainer = document.createElement("div");
  var messageElement = document.createElement("div");
  var profilePicture = document.createElement("img");

  messageContainer.classList.add("message-container");
  messageElement.textContent = message;

  if (sender === "bot") {
    messageElement.classList.add("bot-message");
    profilePicture.src = "MICA_chathead4.png"; // iset MICA profile picture
    profilePicture.classList.add("profile-picture");
    messageContainer.appendChild(profilePicture);
  } else {
    messageElement.classList.add("user-message");
    messageElement.textContent = "" + message; 
  }

  messageContainer.appendChild(messageElement);
  chatContainer.appendChild(messageContainer);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function fetchResponse(message) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/get_response", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          var data = JSON.parse(xhr.responseText);
          appendBotMessage(data.response, data.chathead);
      }
  };
  xhr.send(JSON.stringify({ message: message }));
}


// Function to append bot message to chat container
function appendBotMessage(message, chathead) {
  var chatContainer = document.getElementById("chat-container");
  var messageContainer = document.createElement("div");
  var messageElement = document.createElement("div");
  var profilePicture = document.createElement("img");

  messageContainer.classList.add("message-container");
  messageElement.textContent = message;
  messageElement.classList.add("bot-message");

  // Create profile picture for bot message
  profilePicture.src = chathead;
  profilePicture.classList.add("profile-picture");

  // Append profile picture and message to message container
  messageContainer.appendChild(profilePicture);
  messageContainer.appendChild(messageElement);

  // Append message container to chat container
  chatContainer.appendChild(messageContainer);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}







document.addEventListener("DOMContentLoaded", function() {
  const texts = ["Your health, our priority.", "Healthcare made easy, chat with us!", "Wellness at your fingertips.","Medical Information Chat Assistant"];
  let index = 0;
  const changingTextElement = document.getElementById("changingText");

  function changeText() {
    changingTextElement.textContent = texts[index];
    index = (index + 1) % texts.length
  }

  // Call the function initially and every 2 seconds thereafter
  setInterval(changeText, 4000); // Call every 2 seconds
});
