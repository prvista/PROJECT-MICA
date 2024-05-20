import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import difflib
import speech_recognition as sr
import datetime

# Define your dataset and other variables here...
dataset = [
    (["Home"], "Home Page👋", None, [""]),
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
    (["What is MICA?"], "I am MICA or Medical Information Chat Assistant. I assist users with healthcare-related inquiries and provide valuable information and assistance.", "./dist/components/img/MICA-lightblue_logo.png", [""]),
    (["Hi"], "Hello! How can I help you?👋", "z-img/MICA_hello.png", [""]),
    (["Hello"], "Hello! How can I help you?👋", "z-img/MICA_hello.png", [""]),
]

fallback_response = "I'm sorry, I'm not trained to answer that question."

# Define global variables to store appointment, symptom tracking, and symptom checking details
global appointment_details
appointment_details = {}

global symptom_tracking_details
symptom_tracking_details = {}

global symptom_checking_details
symptom_checking_details = {}

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
    },
    {
        "symptoms": ["headache", "head pain"],
        "conditions": [
            {
                "condition": "Headache",
                "recommendation": "It seems like you might have a headache. Rest in a quiet, dark room and consider taking pain relief medication.",
                "medications": ["Paracetamol", "Ibuprofen"]
            }
        ]
    },
    {
        "symptoms": ["cough", "chest congestion"],
        "conditions": [
            {
                "condition": "Bronchitis",
                "recommendation": "You may have bronchitis. Consider taking cough suppressants, drinking plenty of fluids, and using a humidifier.",
                "medications": ["Cough suppressants", "Antibiotics (if bacterial infection)"]
            }
        ]
    },
    {
        "symptoms": ["shortness of breath", "difficulty breathing"],
        "conditions": [
            {
                "condition": "Asthma",
                "recommendation": "It seems like you might be experiencing asthma symptoms. Use your inhaler as prescribed and seek medical attention if symptoms worsen.",
                "medications": ["Inhaler (bronchodilator)", "Steroids"]
            }
        ]
    },
    {
        "symptoms": ["fatigue", "weakness"],
        "conditions": [
            {
                "condition": "Anemia",
                "recommendation": "You may be experiencing symptoms of anemia. Increase your iron intake through diet or supplements, and get plenty of rest.",
                "medications": ["Iron supplements", "Vitamin B12 supplements"]
            }
        ]
    },
    {
        "symptoms": ["stomach pain", "abdominal discomfort"],
        "conditions": [
            {
                "condition": "Gastritis",
                "recommendation": "It seems like you might have gastritis. Avoid spicy or acidic foods, eat smaller meals, and consider over-the-counter antacids.",
                "medications": ["Antacids", "Proton pump inhibitors"]
            }
        ]
    },
    {
        "symptoms": ["vomiting", "nausea"],
        "conditions": [
            {
                "condition": "Gastroenteritis",
                "recommendation": "Based on your symptoms, you may have gastroenteritis. Stay hydrated with clear fluids and avoid solid foods until symptoms subside.",
                "medications": ["Antiemetics", "Electrolyte solutions"]
            }
        ]
    },
    {
        "symptoms": ["diarrhea", "loose stools"],
        "conditions": [
            {
                "condition": "Diarrhea",
                "recommendation": "It seems like you might have diarrhea. Drink plenty of fluids to stay hydrated and consider over-the-counter medications to manage symptoms.",
                "medications": ["Antidiarrheal medication", "Oral rehydration salts"]
            }
        ]
    },
    {
        "symptoms": ["joint pain", "swelling"],
        "conditions": [
            {
                "condition": "Arthritis",
                "recommendation": "You may be experiencing symptoms of arthritis. Apply ice packs, rest the affected joint, and consider over-the-counter pain relievers.",
                "medications": ["Nonsteroidal anti-inflammatory drugs (NSAIDs)", "Corticosteroids"]
            }
        ]
    },
    {
        "symptoms": ["rash", "itchy skin"],
        "conditions": [
            {
                "condition": "Allergic Reaction",
                "recommendation": "Based on your symptoms, you may be having an allergic reaction. Avoid allergens if known, take antihistamines, and apply soothing lotions.",
                "medications": ["Antihistamines", "Topical corticosteroids"]
            }
        ]
    },
    {
        "symptoms": ["back pain", "lower back pain"],
        "conditions": [
            {
                "condition": "Muscle Strain",
                "recommendation": "It seems like you might have strained your back muscles. Apply ice packs, rest, and consider over-the-counter pain relievers.",
                "medications": ["Acetaminophen", "Nonsteroidal anti-inflammatory drugs (NSAIDs)"]
            }
        ]
    },
    {
        "symptoms": ["dizziness", "lightheadedness"],
        "conditions": [
            {
                "condition": "Vertigo",
                "recommendation": "Based on your symptoms, you may be experiencing vertigo. Avoid sudden movements, rest, and consult a healthcare professional.",
                "medications": ["Antihistamines", "Anti-nausea medications"]
            }
        ]
    },
    {
        "symptoms": ["difficulty swallowing", "painful swallowing"],
        "conditions": [
            {
                "condition": "Esophagitis",
                "recommendation": "You may have esophagitis. Avoid spicy or acidic foods, eat smaller meals, and consider over-the-counter antacids.",
                "medications": ["Antacids", "Proton pump inhibitors"]
            }
        ]
    },
    {
        "symptoms": ["frequent urination", "painful urination"],
        "conditions": [
            {
                "condition": "Urinary Tract Infection (UTI)",
                "recommendation": "It seems like you might have a urinary tract infection (UTI). Drink plenty of fluids, avoid irritants, and consider over-the-counter pain relievers.",
                "medications": ["Antibiotics", "Urinary analgesics"]
            }
        ]
    },
    {
        "symptoms": ["irregular heartbeat", "heart palpitations"],
        "conditions": [
            {
                "condition": "Arrhythmia",
                "recommendation": "You may be experiencing symptoms of arrhythmia. Avoid stimulants, get plenty of rest, and consult a healthcare professional for further evaluation.",
                "medications": ["Beta-blockers", "Calcium channel blockers"]
            }
        ]
    },
    {
        "symptoms": ["chest pain", "pressure in chest"],
        "conditions": [
            {
                "condition": "Heart Attack",
                "recommendation": "Based on your symptoms, you may be experiencing a heart attack. Call emergency services immediately and seek medical attention.",
                "medications": ["Aspirin", "Nitroglycerin"]
            }
        ]
    },
    {
        "symptoms": ["blood in stool", "rectal bleeding"],
        "conditions": [
            {
                "condition": "Hemorrhoids",
                "recommendation": "It seems like you might have hemorrhoids. Increase fiber intake, drink plenty of fluids, and consider over-the-counter hemorrhoid creams.",
                "medications": ["Hemorrhoid creams", "Stool softeners"]
            }
        ]
    },
    {
        "symptoms": ["muscle weakness", "fatigue"],
        "conditions": [
            {
                "condition": "Muscle Weakness",
                "recommendation": "You may be experiencing muscle weakness. Ensure adequate nutrition, rest, and consider physical therapy.",
                "medications": ["Vitamin supplements", "Calcium supplements"]
            }
        ]
    },
    {
        "symptoms": ["swollen lymph nodes", "tender lymph nodes"],
        "conditions": [
            {
                "condition": "Lymphadenitis",
                "recommendation": "Based on your symptoms, you may have lymphadenitis. Apply warm compresses, take over-the-counter pain relievers, and see a doctor if symptoms persist.",
                "medications": ["Pain relievers", "Antibiotics"]
            }
        ]
    },
    {
        "symptoms": ["memory loss", "confusion"],
        "conditions": [
            {
                "condition": "Dementia",
                "recommendation": "It seems like you might be experiencing symptoms of dementia. Consult a healthcare professional for evaluation and management.",
                "medications": ["Cholinesterase inhibitors", "Memantine"]
            }
        ]
    },
    {
        "symptoms": ["seizures", "convulsions"],
        "conditions": [
            {
                "condition": "Epilepsy",
                "recommendation": "You may be experiencing seizures due to epilepsy. Follow your prescribed seizure management plan and seek medical advice.",
                "medications": ["Antiepileptic drugs", "Benzodiazepines"]
            }
        ]
    },
    {
        "symptoms": ["vision changes", "blurred vision"],
        "conditions": [
            {
                "condition": "Vision Impairment",
                "recommendation": "It seems like you might have vision impairment. Schedule an eye examination with an optometrist or ophthalmologist for evaluation.",
                "medications": ["Eyeglasses", "Contact lenses"]
            }
        ]
    },
    {
        "symptoms": ["hair loss", "bald patches"],
        "conditions": [
            {
                "condition": "Alopecia",
                "recommendation": "Based on your symptoms, you may have alopecia. Consult a dermatologist for evaluation and management options.",
                "medications": ["Minoxidil", "Corticosteroid injections"]
            }
        ]
    },
    {
        "symptoms": ["unexplained weight loss", "loss of appetite"],
        "conditions": [
            {
                "condition": "Malnutrition",
                "recommendation": "It seems like you might be experiencing malnutrition. Ensure a balanced diet with adequate calorie intake and consider nutritional supplements.",
                "medications": ["Multivitamins", "Nutritional supplements"]
            }
        ]
    },
    {
        "symptoms": ["excessive thirst", "frequent urination"],
        "conditions": [
            {
                "condition": "Diabetes",
                "recommendation": "You may have diabetes. Monitor blood sugar levels, follow a diabetic diet, and consult a healthcare professional for management.",
                "medications": ["Insulin", "Oral antidiabetic drugs"]
            }
        ]
    },
    {
        "symptoms": ["mood swings", "irritability"],
        "conditions": [
            {
                "condition": "Mood Disorders",
                "recommendation": "Based on your symptoms, you may have a mood disorder. Seek counseling or psychiatric evaluation for diagnosis and management.",
                "medications": ["Antidepressants", "Mood stabilizers"]
            }
        ]
    },
    {
        "symptoms": ["frequent headaches", "migraine attacks"],
        "conditions": [
            {
                "condition": "Migraine",
                "recommendation": "It seems like you might be experiencing migraines. Identify triggers, manage stress, and consider preventive medications.",
                "medications": ["Triptans", "Beta-blockers"]
            }
        ]
    },
    {
        "symptoms": ["excessive sweating", "night sweats"],
        "conditions": [
            {
                "condition": "Hyperhidrosis",
                "recommendation": "You may have hyperhidrosis. Use antiperspirants, wear breathable clothing, and consult a dermatologist for treatment options.",
                "medications": ["Antiperspirants", "Iontophoresis"]
            }
        ]
    },
    {
        "symptoms": ["excessive hunger", "weight gain"],
        "conditions": [
            {
                "condition": "Hypothyroidism",
                "recommendation": "Based on your symptoms, you may have hypothyroidism. Get thyroid function tests done and consult an endocrinologist for management.",
                "medications": ["Levothyroxine", "Liothyronine"]
            }
        ]
    }
]


symptom_dataset += [
    {
        "symptoms": ["severe abdominal pain", "bloody stool"],
        "conditions": [
            {
                "condition": "Crohn's Disease",
                "recommendation": "It seems like you might have Crohn's disease. Follow a low-fiber diet, take anti-inflammatory medications, and consult a gastroenterologist for management.",
                "medications": ["Corticosteroids", "Immunomodulators"]
            }
        ]
    },
    {
        "symptoms": ["excessive thirst", "frequent urination"],
        "conditions": [
            {
                "condition": "Diabetes Mellitus",
                "recommendation": "Based on your symptoms, you may have diabetes mellitus. Monitor blood sugar levels, follow a balanced diet, and take insulin or oral medications as prescribed.",
                "medications": ["Insulin", "Metformin"]
            }
        ]
    },
    {
        "symptoms": ["sudden chest pain", "shortness of breath"],
        "conditions": [
            {
                "condition": "Myocardial Infarction (Heart Attack)",
                "recommendation": "It seems like you might be experiencing a heart attack. Call emergency services immediately, chew aspirin if available, and wait for medical assistance.",
                "medications": ["Aspirin", "Thrombolytics"]
            }
        ]
    },
    {
        "symptoms": ["difficulty speaking", "facial drooping"],
        "conditions": [
            {
                "condition": "Stroke",
                "recommendation": "Based on your symptoms, you may be having a stroke. Call emergency services immediately and note the time of symptom onset for timely treatment.",
                "medications": ["Tissue plasminogen activator (tPA)", "Antiplatelet drugs"]
            }
        ]
    },
    {
        "symptoms": ["swelling in legs", "shortness of breath"],
        "conditions": [
            {
                "condition": "Pulmonary Embolism",
                "recommendation": "It seems like you might have a pulmonary embolism. Seek immediate medical attention, keep calm, and avoid physical exertion.",
                "medications": ["Anticoagulants", "Thrombolytics"]
            }
        ]
    },
    {
        "symptoms": ["confusion", "hallucinations"],
        "conditions": [
            {
                "condition": "Delirium",
                "recommendation": "Based on your symptoms, you may have delirium. Ensure a calm environment, address underlying causes, and seek medical evaluation.",
                "medications": ["Antipsychotics", "Sedatives"]
            }
        ]
    },
    {
        "symptoms": ["painful urination", "lower abdominal pain"],
        "conditions": [
            {
                "condition": "Bladder Infection",
                "recommendation": "It seems like you might have a bladder infection. Drink plenty of water, use antibiotics as prescribed, and avoid irritants like caffeine.",
                "medications": ["Antibiotics", "Urinary analgesics"]
            }
        ]
    },
    {
        "symptoms": ["weight loss", "fatigue"],
        "conditions": [
            {
                "condition": "Hyperthyroidism",
                "recommendation": "You may have hyperthyroidism. Follow up with an endocrinologist, take antithyroid medications, and consider radioactive iodine therapy or surgery.",
                "medications": ["Antithyroid medications", "Beta blockers"]
            }
        ]
    },
    {
        "symptoms": ["difficulty sleeping", "daytime sleepiness"],
        "conditions": [
            {
                "condition": "Sleep Apnea",
                "recommendation": "Based on your symptoms, you may have sleep apnea. Use a CPAP machine, maintain a healthy weight, and avoid alcohol and sedatives.",
                "medications": ["Continuous positive airway pressure (CPAP)", "Oral appliances"]
            }
        ]
    },
    {
        "symptoms": ["blood in urine", "pain in the side or back"],
        "conditions": [
            {
                "condition": "Kidney Stones",
                "recommendation": "It seems like you might have kidney stones. Stay hydrated, manage pain with NSAIDs, and consult a urologist for further evaluation and treatment.",
                "medications": ["NSAIDs", "Alpha blockers"]
            }
        ]
    },
    {
        "symptoms": ["persistent cough", "chest pain"],
        "conditions": [
            {
                "condition": "Pneumonia",
                "recommendation": "Based on your symptoms, you may have pneumonia. Rest, stay hydrated, and use antibiotics as prescribed by a healthcare provider.",
                "medications": ["Antibiotics", "Antipyretics"]
            }
        ]
    },
    {
        "symptoms": ["mood swings", "loss of interest"],
        "conditions": [
            {
                "condition": "Depression",
                "recommendation": "It seems like you might have depression. Seek therapy, consider antidepressant medications, and maintain a support network.",
                "medications": ["Selective serotonin reuptake inhibitors (SSRIs)", "Serotonin-norepinephrine reuptake inhibitors (SNRIs)"]
            }
        ]
    },
    {
        "symptoms": ["difficulty swallowing", "unexplained weight loss"],
        "conditions": [
            {
                "condition": "Esophageal Cancer",
                "recommendation": "You may have esophageal cancer. Consult an oncologist for diagnosis and treatment options, which may include surgery, chemotherapy, and radiation therapy.",
                "medications": ["Chemotherapy", "Targeted therapy"]
            }
        ]
    },
    {
        "symptoms": ["pain in the lower abdomen", "irregular menstruation"],
        "conditions": [
            {
                "condition": "Polycystic Ovary Syndrome (PCOS)",
                "recommendation": "Based on your symptoms, you may have PCOS. Manage symptoms with lifestyle changes, hormonal contraceptives, and metformin.",
                "medications": ["Oral contraceptives", "Metformin"]
            }
        ]
    },
    {
        "symptoms": ["memory loss", "difficulty finding words"],
        "conditions": [
            {
                "condition": "Alzheimer's Disease",
                "recommendation": "It seems like you might have Alzheimer's disease. Consult a neurologist for evaluation, consider cognitive enhancers, and plan for long-term care.",
                "medications": ["Cholinesterase inhibitors", "Memantine"]
            }
        ]
    }
]



# Initialize the global variable for symptom checking details
symptom_checking_details = {}








# Function to handle symptom tracking
def handle_symptom_tracking(self, message):
    global symptom_tracking_details

    if 'track symptoms' in message.lower() or 'start tracking symptoms' in message.lower():
        if symptom_tracking_details:
            response_data = {
                'response': "You already have a symptom tracking session in progress. Would you like to continue?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        else:
            symptom_tracking_details['stage'] = 'description'
            response_data = {
                'response': "Sure! Let's start tracking your symptoms. Please describe your symptoms.",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
    elif symptom_tracking_details:
        stage = symptom_tracking_details.get('stage')

        if stage == 'description':
            symptom_tracking_details['description'] = message
            symptom_tracking_details['stage'] = 'severity'
            response_data = {
                'response': "Got it. How severe are your symptoms on a scale from 1 to 10?",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
        elif stage == 'severity':
            symptom_tracking_details['severity'] = message
            response_data = {
                'response': "Thank you for the information. Your symptoms have been recorded.",
                'chathead': 'MICA_chathead4.png',
                'image': None,
                'medicine_recommendation': []
            }
            # Reset symptom_tracking_details for the next tracking request
            symptom_tracking_details = {}
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











# Function to handle scheduling appointments
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
        elif "track symptoms" in message.lower() or symptom_tracking_details:
            handle_symptom_tracking(self, message)
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
