from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from difflib import SequenceMatcher

# Define the dataset with keywords and corresponding responses
dataset = [
    (["fever"], "Apply a cold compress and take fever-reducing medication like paracetamol."),
    (["headache"], "Rest in a quiet, dark room and take over-the-counter pain relievers like ibuprofen."),
    (["hospital", "nearest hospital"], "You can search for nearby hospitals using online maps or call emergency services for assistance."),
    (["COVID-19", "symptoms of COVID-19"], "Common symptoms include fever, cough, and difficulty breathing. If you suspect you have COVID-19, seek medical advice immediately."),
    (["common cold", "prevent the common cold"], "Wash your hands frequently, avoid close contact with sick individuals, and maintain a healthy lifestyle with a balanced diet and regular exercise."),
    (["sprained ankle", "ice for a sprained ankle"], "Apply ice to the affected area and elevate it to reduce swelling. Rest and avoid putting weight on the ankle."),
    (["prevent COVID-19", "prevention measures for COVID-19"], "To prevent COVID-19, practice good hygiene by washing your hands frequently, wearing masks in public places, practicing social distancing, and getting vaccinated when available."),
    (["updates COVID-19", "status or update for COVID-19"], "For the latest updates on COVID-19, refer to reliable sources such as the World Health Organization (WHO) or your local health department."),
    (["Hi"], "Hello! How can I help you?"),
    (["Hello"], "Hi! How can I help you?")
]

# Define a fallback response for unmatched queries
fallback_response = "I'm sorry, I'm not trained to answer that question."

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
        response = generate_response(message)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Include the chathead image in the JSON response
        chathead_image = 'MICA_chathead4.png'  # Path to the chathead image
        response_data = {
            'response': response,
            'chathead': chathead_image
        }
        self.wfile.write(json.dumps(response_data).encode())

def generate_response(message):
    # Initialize variables to track maximum score and corresponding response
    max_score = 0
    best_response = fallback_response
    
    # Iterate over the dataset to find the best matching response
    for keywords, response in dataset:
        # Calculate the similarity score for each keyword in the keyword set
        keyword_scores = [SequenceMatcher(None, message.lower(), keyword.lower()).ratio() for keyword in keywords]
        
        # Calculate the average score for the keyword set
        avg_score = sum(keyword_scores) / len(keywords)
        
        # If the average score is greater than the current maximum score, update the maximum score and response
        if avg_score > max_score:
            max_score = avg_score
            best_response = response
    
    # If the maximum score is below a certain threshold, return the fallback response
    if max_score < 0.6:  # Adjust this threshold as needed
        return fallback_response
    
    return best_response

    # Calculate similarity score for each keyword set
    scores = {}
    for keywords, response in dataset:
        max_score = max(SequenceMatcher(None, message.lower(), keyword.lower()).ratio() for keyword in keywords)
        scores[max_score] = response
    
    # Select the response with the highest similarity score
    max_score = max(scores.keys())
    
    # If the maximum score is below a certain threshold, return the fallback response
    if max_score < 0.6:  # Adjust this threshold as needed
        return fallback_response
    
    response = scores[max_score]
    return response

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
