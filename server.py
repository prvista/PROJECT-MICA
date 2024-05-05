import json
import pyttsx3
from http.server import BaseHTTPRequestHandler, HTTPServer
import difflib

# Define your dataset and other variables here...
dataset = [
    (["fever"], "Apply a cold compress and take fever-reducing medication like paracetamol.", None),
    (["headache"], "Biogesic 😘😘😘", "z-img/biogesic.jpg"),
    (["hospital", "nearest hospital"], "You can search for nearby hospitals using online maps or call emergency services for assistance. The nearest hospital in your location is Doctors Hospital.", "z-img/spc-doctors.jpg"),
    (["COVID-19", "symptoms of COVID-19"], "Common symptoms include fever, cough, and difficulty breathing. If you suspect you have COVID-19, seek medical advice immediately.", None),
    (["common cold", "prevent the common cold"], "Wash your hands frequently, avoid close contact with sick individuals, and maintain a healthy lifestyle with a balanced diet and regular exercise.", None),
    (["asthma", "prevent the asthma"], "tite", None),
    (["sprained ankle", "ice for a sprained ankle"], "Apply ice to the affected area and elevate it to reduce swelling. Rest and avoid putting weight on the ankle.", "z-img/sprained-ankle.jpg"),
    (["prevent COVID-19", "prevention measures for COVID-19"], "To prevent COVID-19, practice good hygiene by washing your hands frequently, wearing masks in public places, practicing social distancing, and getting vaccinated when available.", None),
    (["updates COVID-19", "status or update for COVID-19"], "For the latest updates on COVID-19, refer to reliable sources such as the World Health Organization (WHO) or your local health department.", None),
    (["What is MICA?"], "I am MICA or Medical Information Chat Assistant. I assist users with healthcare-related inquiries and provides valuable information and assistance.", "MICA-dila.png"),
    (["Hi"], "Hello! How can I help you?👋", "z-img/MICA_hello.png"),
    (["Hello"], "Hi! How can I help you?👋", "z-img/MICA_hello.png"),
]

fallback_response = "I'm sorry, I'm not trained to answer that question."

def respond(response):
    # Print the bot's response
    try:
        print("Bot:", response)
    except UnicodeEncodeError:
        # Handle UnicodeEncodeError by replacing the problematic characters
        response = response.encode('ascii', 'ignore').decode('ascii')
        print("Bot:", response)
    
    # Speak the response using text-to-speech with a female voice
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Selecting another female voice
    female_voices = [voice for voice in voices if "female" in voice.name.lower()]
    if female_voices:
        engine.setProperty('voice', female_voices[1].id)  # Change the index to select another female voice
    engine.say(response)
    engine.runAndWait()

def generate_response(message):
    # Initialize variables to track maximum score and corresponding response
    best_response = fallback_response
    best_image = None
    
    # Iterate over the dataset to find the best matching response
    for keywords, response, img in dataset:
        # Check for exact matches first
        if any(keyword.lower() in message.lower() for keyword in keywords):
            best_response = response
            best_image = img
            break
        
        # If no exact matches, check for partial matches
        for keyword in keywords:
            if difflib.SequenceMatcher(None, keyword.lower(), message.lower()).ratio() >= 0.7:
                best_response = response
                best_image = img
                break
    
    return best_response, best_image

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            if self.path.endswith('.html'):
                mimetype = 'text/html'
            elif self.path.endswith('.css'):
                mimetype = 'text/css'
            elif self.path.endswith('.js'):
                mimetype = 'application/javascript'
            elif self.path.endswith('.png'):
                mimetype = 'image/png'
            elif self.path.endswith('.jpg'):
                mimetype = 'image/jpg'
            else:
                raise Exception('Unknown file type')
                
            # Open and read the file
            with open(self.path[1:], 'rb') as file:
                content = file.read()
                
            # Set response code and headers
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            
            # Send the content of the file
            self.wfile.write(content)
        except Exception as e:
            print(f'Error: {e}')
            self.send_error(404, 'File Not Found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        message = data['message']
        response, image_path = generate_response(message)

        # Send the JSON response with the bot's text response and image path to the client
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Include the chathead image and image path in the JSON response
        chathead_image = 'MICA_chathead4.png'  # Path to the chathead image
        response_data = {
            'response': response,
            'chathead': chathead_image,
            'image': image_path
        }
        self.wfile.write(json.dumps(response_data).encode())

        # Speak the bot's response using text-to-speech
        respond(response)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
