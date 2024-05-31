import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import difflib
import speech_recognition as sr
import random
import datetime


dataset = [
    (["Home"], "Home Page👋", None, []),
    (["About"], "About Page👋", None, []),
    (["Demo"], "Demo Page👋", None, []),
    (["Health Tips"], "Health Tips Page👋", None, []),
    (["Advance Chatting"], "Advance Chatting Page👋", None, []),
    (["fever"], "Apply a cold compress and take fever-reducing medication like paracetamol.", None, ["Paracetamol", "Ibuprofen (Advil)", "Aspirin (Bayer)"]),
    (["hospital", "nearest hospital"], "You can search for nearby hospitals using online maps or call emergency services for assistance. The nearest hospital in your location is Doctors Hospital.", "z-img/spc-doctors.jpg", []),
    (["COVID-19", "symptoms of COVID-19"], "Common symptoms include fever, cough, and difficulty breathing. If you suspect you have COVID-19, seek medical advice immediately.", None, []),
    (["common cold", "prevent the common cold"], "Wash your hands frequently, avoid close contact with sick individuals, and maintain a healthy lifestyle with a balanced diet and regular exercise.", None, []),
    (["sprained ankle", "ice for a sprained ankle"], "Apply ice to the affected area and elevate it to reduce swelling. Rest and avoid putting weight on the ankle.", "z-img/sprained-ankle.jpg", []),
    (["prevent COVID-19", "prevention measures for COVID-19"], "To prevent COVID-19, practice good hygiene by washing your hands frequently, wearing masks in public places, practicing social distancing, and getting vaccinated when available.", None, []),
    (["updates COVID-19", "status or update for COVID-19"], "For the latest updates on COVID-19, refer to reliable sources such as the World Health Organization (WHO) or your local health department.", None, []),
    (["What is MICA?"], "I am MICA or Medical Information Chat Assistant. I assist users with healthcare-related inquiries and provide valuable information and assistance.", "./dist/components/img/MICA-lightblue_logo.png", [""]),
    (["Hi"], "Hello! How can I help you?👋", "z-img/MICA_hello.png", [""]),
    (["Hello"], "Hello! How can I help you?👋", "z-img/MICA_hello.png", [""]),
]

fallback_response = "I'm sorry, I'm not trained to answer that question."


global appointment_details
appointment_details = {}

global symptom_checking_details
symptom_checking_details = {}

global quiz_details
quiz_details = {}




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











symptom_dataset = [
    {
        "symptoms": ["fever", "high temperature"],
        "conditions": [
            {
                "condition": "Fever",
                "recommendation": "It seems like you might have a fever. Consider taking fever-reducing medication and staying hydrated.",
                "medications": ["Paracetamol", "Ibuprofen"]
            }
        ]
    },
    {   
        "symptoms": ["sore throat", "throat pain"],
        "conditions": [
            {
                "condition": "Sore Throat",
                "recommendation": "It seems like you might have a sore throat. Drink warm liquids, use throat lozenges, and consider taking pain relief medication.",
                "medications": ["Throat Lozenges", "Paracetamol"]
            }
        ]
    },
    {
        "symptoms": ["runny nose", "nasal congestion"],
        "conditions": [
            {
                "condition": "Cold",
                "recommendation": "Based on your description, it seems like you might have a cold. Rest, drink plenty of fluids, and consider taking over-the-counter cold medication.",
                "medications": ["Over-the-counter cold medication"]
            }
        ]
    }
]

symptom_checking_details = {}




def handle_appointment_scheduling(self, message):
    global appointment_details

    if 'schedule an appointment' in message.lower() or 'book an appointment' in message.lower():
        if appointment_details:
            response_data = {
                'response': "You already have an appointment in progress. Would you like to cancel it?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        else:
            appointment_details['stage'] = 'date'
            response_data = {
                'response': "Sure! Let's schedule an appointment. What date would you like to schedule it for?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
    elif appointment_details:
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
            response_data = {
                'response': f"Your appointment has been scheduled for {appointment_details['date']} at {appointment_details['time']} for {appointment_details['reason']}. We'll see you then!",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
            appointment_details = {}
    else:
        response_data = {
            'response': "I'm sorry, I didn't understand that. Could you please repeat?",
            'chathead': 'MICA_chathead4.png',
            'image': None,
            'medicine_recommendation': []
        }

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(response_data).encode())













def handle_symptom_checking(self, message):
    global symptom_checking_details

    if 'check symptoms' in message.lower():
        if symptom_checking_details:
            response_data = {
                'response': "You already have a symptom checking session in progress. Would you like to continue?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        else:
            symptom_checking_details['stage'] = 'describe'
            response_data = {
                'response': "Sure! Let's check your symptoms. Please describe your symptoms.",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
    elif symptom_checking_details:
        stage = symptom_checking_details.get('stage')

        if stage == 'describe':
            symptom_checking_details['description'] = message
            symptom_checking_details['stage'] = 'duration'
            response_data = {
                'response': "Got it. How long have you been experiencing these symptoms?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        elif stage == 'duration':
            symptom_checking_details['duration'] = message
            symptom_checking_details['stage'] = 'intensity'
            response_data = {
                'response': "Thanks. On a scale from 1 to 10, how intense are your symptoms?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        elif stage == 'intensity':
            symptom_checking_details['intensity'] = message
            description = symptom_checking_details['description'].lower()

            # Analyze symptoms using the expanded dataset
            recommendation = "I'm not sure what the issue might be. Please seek medical advice."
            medications = []
            for entry in symptom_dataset:
                if any(symptom in description for symptom in entry['symptoms']):
                    recommendation = entry['conditions'][0]['recommendation']
                    medications = entry['conditions'][0]['medications']
                    break

            response_data = {
                'response': recommendation,
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': medications
            }
            # Reset symptom_checking_details for the next checking request
            symptom_checking_details = {}
    else:
        response_data = {
            'response': "I'm sorry, I didn't understand that. Could you please repeat?",
            'chathead': 'MICA_chathead4.png',
            'image': None,
            'medicine_recommendation': []
        }

    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(response_data).encode())





    











quiz_dataset = [
    {
        "question": "\nWhat is the normal body temperature in Celsius?\n",
        "options": ["\nA) 36°C", "B) 37°C", "C) 38°C\n"],
        "answer": "B) 37°C"
    },
    {
        "question": "\nWhat vitamin is produced when a person is exposed to sunlight?\n",
        "options": ["A) Vitamin A", "B) Vitamin B", "C) Vitamin D"],
        "answer": "C) Vitamin D"
    },
    {
        "question": "\nHow often should you brush your teeth?\n",
        "options": ["A) Once a day", "B) Twice a day", "C) Three times a day"],
        "answer": "B) Twice a day"
    },
    {
        "question": "\nWhat is a common symptom of dehydration?\n",
        "options": ["A) Headache", "B) Dizziness", "C) Dry mouth"],
        "answer": "A) Headache"
    },
    {
        "question": "\nWhat is the main function of red blood cells?\n",
        "options": ["A) Fight infections", "B) Transport oxygen", "C) Clot blood"],
        "answer": "B) Transport oxygen"
    },
    {
        "question": "\nWhich of the following is a symptom of the flu?\n",
        "options": ["A) Runny nose", "B) Sore throat", "C) Fever"],
        "answer": "C) Fever"
    },
    {
        "question": "\nHow many hours of sleep are recommended for adults?\n",
        "options": ["A) 4-5 hours", "B) 6-7 hours", "C) 7-9 hours"],
        "answer": "C) 7-9 hours"
    },
    {
        "question": "\nWhat is the primary cause of Type 1 diabetes?\n",
        "options": ["A) Obesity", "B) Genetics", "C) Virus"],
        "answer": "B) Genetics"
    },
    {
        "question": "\nWhich organ is affected by hepatitis?\n",
        "options": ["A) Heart", "B) Liver", "C) Kidneys"],
        "answer": "B) Liver"
    },
    {
        "question": "\nWhat is the recommended daily intake of water for an average adult?\n",
        "options": ["A) 1-2 liters", "B) 2-3 liters", "C) 3-4 liters"],
        "answer": "B) 2-3 liters"
    }
]

def generate_quiz():
    quiz = random.sample(quiz_dataset, 5)
    return quiz

def handle_quiz(self, message):
    global quiz_details

    if 'health quiz' in message.lower():
        quiz_details['quiz'] = generate_quiz()
        quiz_details['current_question'] = 0
        quiz_details['score'] = 0
        question = quiz_details['quiz'][0]['question']
        options = quiz_details['quiz'][0]['options']
        response_data = {
            'response': f"Question 1: {question}\n\nOptions: {', '.join(options)}",
            'chathead': 'MICA_chathead4.png',
            'image': None,
            'medicine_recommendation': []
        }
    elif quiz_details:
        current_question = quiz_details['current_question']
        quiz = quiz_details['quiz']
        user_answer = message.strip().upper()  # Convert answer to uppercase for consistency
        correct_answer = quiz[current_question]['answer'].split(')')[0].strip().upper()  # Extract the correct answer (A, B, or C)

        if user_answer == correct_answer:
            quiz_details['score'] += 1
            feedback = "Correct!"
        else:
            feedback = f"Wrong. The correct answer is: {quiz[current_question]['answer']}"

        current_question += 1

        if current_question < len(quiz):
            quiz_details['current_question'] = current_question
            question = quiz[current_question]['question']
            options = quiz[current_question]['options']
            response_data = {
    'response': f"{feedback}\n\nQuestion {current_question + 1}: {question}\nOptions: {', '.join(options)}",
    'chathead': 'MICA_chathead4.png',
    'image': None,
    'medicine_recommendation': []
}

        else:
            score = quiz_details['score']
            total_questions = len(quiz)
            response_data = {
                'response': f"{feedback}\n\nQuiz finished! Your score: {score} over {total_questions}. Congratulations!👏",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': ["You're great! Keep it up!👏"]
            }
            quiz_details = {}
    else:
        response_data = {
            'response': "I'm sorry, I didn't understand that. Could you please repeat?",
            'chathead': 'MICA_chathead4.png',
            'image': None,
            'medicine_recommendation': []
        }

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
                mimetype = 'video/jpg'
            elif self.path.endswith('.gif'):
                mimetype = 'image/.gif'
            elif self.path.endswith('\n'):
                mimetype = 'text/html'
            else:
                raise Exception('Unknown file type')

            with open(self.path[1:], 'rb') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            print(f'Error: {e}')
            self.send_error(404, 'File Not Found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        if 'audio' in data:
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
        elif "check symptoms" in message.lower() or symptom_checking_details:
            handle_symptom_checking(self, message)
        elif "health quiz" in message.lower() or quiz_details:
            handle_quiz(self, message)
        else:
            response, image_path, medicine_recommendation = generate_response(message)
            chathead_image = 'MICA_chathead4.png'
            response_data = {
                'response': response,
                'chathead': chathead_image,
                'image': image_path,
                'medicine_recommendation': medicine_recommendation
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()

