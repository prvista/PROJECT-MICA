import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import difflib
import speech_recognition as sr

# Define your dataset and other variables here...
dataset = [
    (["About"], "About Page👋", None, [""]),
    (["Demo"], "Demo Page👋", None, [""]),
    (["Health Tips"], "Health Tips Page👋", None, [""]),
    (["Advance Chatting"], "Advance Chatting Page👋", None, [""]),
    (["fever"], "Apply a cold compress and take fever-reducing medication like paracetamol.", None, ["Paracetamol", "Ibuprofen (Advil)", "Aspirin (Bayer)"]),
    (["hospital", "nearest hospital"], "You can search for nearby hospitals using online maps or call emergency services for assistance. The nearest hospital in your location is Doctors Hospital.", "z-img/spc-doctors.jpg", [""]),
    (["COVID-19", "symptoms of COVID-19"], "Common symptoms include fever, cough, and difficulty breathing. If you suspect you have COVID-19, seek medical advice immediately.", None, [""]),
    (["common cold", "prevent the common cold"], "Wash your hands frequently, avoid close contact with sick individuals, and maintain a healthy lifestyle with a balanced diet and regular exercise.", None, [""]),
    (["sprained ankle", "ice for a sprained ankle"], "Apply ice to the affected area and elevate it to reduce swelling. Rest and avoid putting weight on the ankle.", "z-img/sprained-ankle.jpg", [""]),
    (["prevent COVID-19", "prevention measures for COVID-19"], "To prevent COVID-19, practice good hygiene by washing your hands frequently, wearing masks in public places, practicing social distancing, and getting vaccinated when available.", None, [""]),
    (["updates COVID-19", "status or update for COVID-19"], "For the latest updates on COVID-19, refer to reliable sources such as the World Health Organization (WHO) or your local health department.", None, [""]),
    (["What is MICA?"], "I am MICA or Medical Information Chat Assistant. I assist users with healthcare-related inquiries and provide valuable information and assistance.", "MICA-dila.png", [""]),
    (["Hi"], "Hello! How can I help you?👋", "z-img/MICA_hello.png", [""]),
    (["Hello"], "Hello! How can I help you?👋", "z-img/MICA_hello.png", [""]),
]

fallback_response = "I'm sorry, I'm not trained to answer that question."

# Define a global variable to store appointment details
global appointment_details
appointment_details = {}

# Function to generate response based on user input
def generate_response(message):
    # Initialize variables to track maximum score and corresponding response
    best_response = fallback_response
    best_image = None
    medicine_recommendation = []

    # Iterate over the dataset to find the best matching response
    for keywords, response, img, medicines in dataset:
        # Check for exact matches first
        if any(keyword.lower() in message.lower() for keyword in keywords):
            best_response = response
            best_image = img
            medicine_recommendation = medicines
            break

        # If no exact matches, check for partial matches using fuzzy matching
        for keyword in keywords:
            if difflib.SequenceMatcher(None, keyword.lower(), message.lower()).ratio() >= 0.7:
                best_response = response
                best_image = img
                medicine_recommendation = medicines
                break

    # Split medicine recommendations into separate lines if there are line breaks
    medicine_recommendation = [medicine.split('\n') for medicine in medicine_recommendation]

    return best_response, best_image, medicine_recommendation

# Function to handle scheduling appointments
def handle_appointment_scheduling(self, message):
    global appointment_details

    if 'schedule an appointment' in message.lower() or 'book an appointment' in message.lower():
        # Check if an appointment is already in progress
        if appointment_details:
            # Appointment already in progress, ask for confirmation
            response_data = {
                'response': "You already have an appointment in progress. Would you like to cancel it?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        else:
            # Start scheduling a new appointment
            appointment_details['stage'] = 'date'
            response_data = {
                'response': "Sure! Let's schedule an appointment. What date would you like to schedule it for?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
    elif appointment_details:
        # Handle subsequent stages of appointment scheduling
        stage = appointment_details.get('stage')

        if stage == 'date':
            appointment_details['date'] = message
            appointment_details['stage'] = 'time'
            response_data = {
                'response': "Got it! What time would you prefer?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        elif stage == 'time':
            appointment_details['time'] = message
            appointment_details['stage'] = 'reason'
            response_data = {
                'response': "Okay! What's the reason for the appointment?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        elif stage == 'reason':
            appointment_details['reason'] = message
            # Appointment finalized, you can add the logic for saving the appointment here
            response_data = {
                'response': f"Your appointment has been scheduled for {appointment_details['date']} at {appointment_details['time']} for {appointment_details['reason']}. We'll see you then!",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
            # Reset appointment_details for the next scheduling request
            appointment_details = {}
    else:
        response_data = {
            'response': "I'm sorry, I didn't understand that. Could you please repeat?",
            'chathead': 'MICA_chathead4.png',
            'image': None,
            'medicine_recommendation': []
        }

    # Send the JSON response
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(response_data).encode())

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
            elif self.path.endswith('.gif'):
                mimetype = 'image/gif'
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

        if 'audio' in data:
            # Speech-to-text conversion
            audio_data = data['audio']
            recognizer = sr.Recognizer()
            with sr.AudioData(audio_data) as audio_file:
                try:
                    text = recognizer.recognize_google(audio_file)
                    message = text.strip()
                except sr.UnknownValueError:
                    message = ""
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    message = ""
        else:
            message = data['message']

        if "schedule an appointment" in message.lower() or "book an appointment" in message.lower() or appointment_details:
            handle_appointment_scheduling(self, message)
        else:
            response, image_path, medicine_recommendation = generate_response(message)
            chathead_image = 'MICA_chathead4.png'  # Path to the chathead image
            response_data = {
                'response': response,
                'chathead': chathead_image,
                'image': image_path,
                'medicine_recommendation': medicine_recommendation
            }

            # Send the JSON response with the bot's text response and image path to the client
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()
