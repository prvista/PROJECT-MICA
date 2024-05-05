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
  } else {
    messageElement.classList.add("user-message");
    messageContainer.appendChild(messageElement);
  }

  chatContainer.appendChild(messageContainer);
  chatContainer.scrollTop = chatContainer.scrollHeight;

  // Add the profile picture below the user's message
  if (sender === "user") {
    profilePicture.src = "MICA_chathead4.png"; // Set the profile picture source
    profilePicture.classList.add("profile-picture");
    messageContainer.appendChild(profilePicture); // Append the profile picture

    // Position the profile picture to the right of the user's message
    profilePicture.style.float = "right";
    profilePicture.style.marginTop = "5px"; // Adjust margin as needed
    profilePicture.style.width = "30px"; // Set the width of the profile picture
    profilePicture.style.height = "30px"; // Set the height of the profile picture
  }
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
  const texts = ["Your health, our priority.", "Healthcare made easy, chat with us!", "Wellness at your fingertips.","Medical Information Chat Assistant"];
  let index = 0;
  const changingTextElement = document.getElementById("changingText");

  function changeText() {
    changingTextElement.textContent = texts[index];
    index = (index + 1) % texts.length
  }

  function handleKeyPress(event) {
    if (event.key === "Enter") {
      sendMessage(); // Call sendMessage function when Enter key is pressed
    }
  }

  // Add event listener to input field
  var userInput = document.getElementById("user-input");
  userInput.addEventListener("keypress", handleKeyPress);

  // Call the function initially and every 2 seconds thereafter
  setInterval(changeText, 4000); // Call every 2 seconds
});
