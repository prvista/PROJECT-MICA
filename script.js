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





function appendMessage(sender, message, imageUrl) {
  var chatContainer = document.getElementById("chat-container");
  var messageContainer = document.createElement("div");
  var messageElement = document.createElement("div");
  var profilePicture = document.createElement("img"); 
  var timeElement = document.createElement("div")

  messageContainer.classList.add("message-container");
  messageElement.textContent = message;

  if (sender === "bot") {
      messageElement.classList.add("bot-message");
      if (imageUrl) {
          var image = document.createElement("img");
          image.src = imageUrl;
          messageContainer.appendChild(messageElement);
          messageContainer.appendChild(image); 
      } else {
          messageContainer.appendChild(messageElement); 
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
      messageContainer.appendChild(profilePicture); 
  }

  chatContainer.appendChild(messageContainer);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}









function getCurrentTime() {
  var now = new Date();
  var hours = now.getHours();
  var minutes = now.getMinutes();
  var ampm = hours >= 12 ? "PM" : "AM";
  hours = hours % 12;
  hours = hours ? hours : 12; 
  minutes = minutes < 10 ? "0" + minutes : minutes;
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
          if (data.appointment_prompt) {
              // Show appointment message with inputs
              var chatContainer = document.getElementById("chat-container");
              var messageContainer = document.createElement("div");
              messageContainer.classList.add("message-container", "bot-message");
              messageContainer.innerHTML = `
                  <div class="message">${data.response}</div>
                  <label for="appointment-date">Choose a date:</label>
                  <input type="date" id="appointment-date" name="appointment-date">
                  <label for="appointment-time">Choose a time:</label>
                  <input type="time" id="appointment-time" name="appointment-time">
                  <button onclick="scheduleAppointment()">Schedule Appointment</button>
              `;
              chatContainer.appendChild(messageContainer);
          } else {
              // Regular chat message
              appendBotMessage(data.response, data.image);
              displayMedicineRecommendation(data.medicine_recommendation); 
              speakBotMessage(data.response); 
          }
      }
  };
  xhr.send(JSON.stringify({ message: message }));
}









function appendBotMessage(message, imageUrl) {
  appendMessage("bot", message, imageUrl);
}










function displayMedicineRecommendation(medicines) {
  var medicineRecommendationContent = document.getElementById("medicine-recommendation-content");
  medicineRecommendationContent.innerHTML = ""; // Clear previous recommendations
  if (medicines && medicines.length > 0) {
    medicines.forEach(function (medicine, index) {
      var medicineElement = document.createElement("div");
      medicineElement.textContent = medicine;
      medicineRecommendationContent.appendChild(medicineElement);
      
      // Add small space between medicine recommendations, except for the last one
      if (index < medicines.length - 1) {
        medicineRecommendationContent.appendChild(document.createTextNode(" "));
      }
    });
  } else {
    medicineRecommendationContent.textContent = "No medicine recommendation available.";
  }
}




function startSpeechRecognition() {
  var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
  recognition.lang = 'en-US';

  recognition.onstart = function() {
    console.log('Speech recognition started...');
  };

  recognition.onresult = function(event) {
    var transcript = event.results[0][0].transcript;
    console.log('Transcript:', transcript);
    appendMessage("user", transcript);
    fetchResponse(transcript);
  };

  recognition.onerror = function(event) {
    console.error('Speech recognition error:', event.error);
  };

  recognition.onend = function() {
    console.log('Speech recognition ended.');
  };

  recognition.start();
}




function speakBotMessage(message) {
  // Remove emoji from the message
  var textOnlyMessage = message.replace(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g, '');

  var speech = new SpeechSynthesisUtterance(textOnlyMessage);
  speechSynthesis.speak(speech);
}

function handleKeyPress(event) {
  if (event.key === "Enter") {
      sendMessage(); // Call sendMessage function when Enter key is pressed
  }
}

function handlePromptClick(prompt) {
  document.getElementById("user-input").value = prompt;
  sendMessage(); 
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

// Add event listener to microphone button
var micButton = document.getElementById("mic-button");
micButton.addEventListener("click", function() {
  startSpeechRecognition(); 
});

setInterval(changeText, 4000); 


function displayMedicineRecommendation(medicines) {
  var medicineRecommendationContent = document.getElementById("medicine-recommendation-content");
  var recoBadge = document.getElementById("reco-badge");
  medicineRecommendationContent.innerHTML = ""; // Clear previous recommendations

  if (medicines && medicines.length > 0) {
    medicines.forEach(function (medicine, index) {
      var medicineElement = document.createElement("div");
      medicineElement.textContent = medicine;
      medicineRecommendationContent.appendChild(medicineElement);
      
      // Add small space between medicine recommendations, except for the last one
      if (index < medicines.length - 1) {
        medicineRecommendationContent.appendChild(document.createTextNode(" "));
      }
    });
    recoBadge.textContent = medicines.length; // Update badge count
  } else {
    medicineRecommendationContent.textContent = "No medicine recommendation available.";
    recoBadge.textContent = "0"; // Reset badge count
  }
}
