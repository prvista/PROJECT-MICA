function sendMessage() {
  var sound = document.getElementById("messageSound");
  sound.play(); // Play the sound

  var userInput = document.getElementById("user-input").value.trim();
  if (userInput !== "") {
    appendMessage("user", userInput);
    document.getElementById("user-input").value = "";
    fetchResponse(userInput);
  }
}






function appendMessage(sender, message, imageUrl) {
  var chatContainer = document.getElementById("chat-container");
  var messageContainer = document.createElement("div");
  var messageElement = document.createElement("div");
  var profilePicture = document.createElement("img"); // Create a new img element for the profile picture
  var timeElement = document.createElement("div"); // Create a new div element for the time

  messageContainer.classList.add("message-container");
  messageElement.textContent = message;

  if (sender === "bot") {
    messageElement.classList.add("bot-message");
    if (imageUrl) {
      var image = document.createElement("img");
      image.src = imageUrl;
      messageContainer.appendChild(messageElement);
      messageContainer.appendChild(image); // Appending image below the message
    } else {
      messageContainer.appendChild(messageElement); // Append message only if no image
    }
    // Add the current time below the bot's message
    timeElement.textContent = getCurrentTime();
    timeElement.classList.add("message-time");
    messageContainer.appendChild(timeElement);
  } else {
    messageElement.classList.add("user-message");
    messageContainer.appendChild(messageElement);
    // Add the profile picture below the user's message
    profilePicture.src = "MICA_chathead4.png"; // Set the profile picture source
    profilePicture.classList.add("profile-picture");
    messageContainer.appendChild(profilePicture); // Append the profile picture
  }

  chatContainer.appendChild(messageContainer);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Function to get the current time
function getCurrentTime() {
  var now = new Date();
  var hours = now.getHours();
  var minutes = now.getMinutes();
  var ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12;
  hours = hours ? hours : 12; // Handle midnight
  minutes = minutes < 10 ? "0" + minutes : minutes; // Add leading zero to minutes
  var timeString = hours + ":" + minutes + " " + ampm;
  return timeString;
}








function fetchResponse(message) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/get_response", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      var data = JSON.parse(xhr.responseText);
      appendBotMessage(data.response, data.image);
    }
  };
  xhr.send(JSON.stringify({ message: message }));
}





function appendBotMessage(message, imageUrl) {
  appendMessage("bot", message, imageUrl);
}






document.addEventListener("DOMContentLoaded", function() {
  const texts = ["Your health, our priority.", "Healthcare made easy, chat with us!", "Wellness at your fingertips.", "Medical Information Chat Assistant"];
  let index = 0;
  const changingTextElement = document.getElementById("changingText");

  function changeText() {
    changingTextElement.textContent = texts[index];
    index = (index + 1) % texts.length;
  }

  function handleKeyPress(event) {
    if (event.key === "Enter") {
      sendMessage(); // Call sendMessage function when Enter key is pressed
    }
  }

  function handlePromptClick(prompt) {
    document.getElementById("user-input").value = prompt;
    sendMessage(); // Automatically send the message when a prompt is clicked
  }

  // Add event listener to input field
  var userInput = document.getElementById("user-input");
  userInput.addEventListener("keypress", handleKeyPress);

  // Add event listener to prompt items
  var promptItems = document.getElementsByClassName("prompt-item");
  for (var i = 0; i < promptItems.length; i++) {
    promptItems[i].addEventListener("click", function() {
      handlePromptClick(this.textContent);
    });
  }

  // Call the function initially and every 2 seconds thereafter
  setInterval(changeText, 4000); // Call every 4 seconds
});
