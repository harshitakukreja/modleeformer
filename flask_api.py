# Flask app
from flask import Flask, request
app = Flask(__name__)

from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="harshitakukreja/modlee_transformer")

# Endpoint to handle inference requests
@app.route('/predict', methods=['POST']) 
def predict():
    # Get input text from request
    text = request.json['text']
    return classifier(text)

if __name__ == '__main__':
   app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)