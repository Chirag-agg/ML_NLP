# api/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# ✅ FIX: Corrected the filename typo from "piipeline" to "pipeline"
MODEL_FILENAME = "sentiment_pipeline.pkl"
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', MODEL_FILENAME)

# Add src to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.models.sentiment_analyzer import SentimentAnalyzer
from preprocessing.text_cleaner import TextCleaner

app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing

# Initialize components
analyzer = SentimentAnalyzer()
text_cleaner = TextCleaner()

# Load pre-trained model on startup if it exists
if os.path.exists(MODEL_PATH):
    print(f"Loading pre-trained model from {MODEL_PATH}...")
    analyzer.load_model(MODEL_PATH)
else:
    print(f"⚠️ No pre-trained model found at {MODEL_PATH}. API will start with an untrained model.")
    print("Please use the POST /train endpoint or run train.py to create one.")

# --- The rest of the file remains the same ---

@app.route('/', methods=['GET'])
def home():
    """Home endpoint providing API information and usage."""
    return jsonify({
        "message": "Sentiment Analysis API",
        "version": "1.0.0",
        "model_status": analyzer.get_model_info(),
        "endpoints": {
            "POST /predict": "Predict sentiment for a single text.",
            "POST /predict_batch": "Predict sentiment for a list of texts.",
            "POST /train": "Train the model with new data.",
            "POST /model/evaluate": "Evaluate the model's performance.",
            "GET /model/info": "Get detailed model information.",
            "GET /health": "Check the health of the API."
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "model_trained": analyzer.is_trained,
        "version": "1.0.0"
    })

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    """Predict sentiment for a single text."""
    try:
        if not analyzer.is_trained:
            return jsonify({"error": "Model is not trained. Please train it via the /train endpoint."}), 503

        data = request.get_json()
        if not data or 'text' not in data or not isinstance(data['text'], str):
            return jsonify({"error": "'text' field is required and must be a string"}), 400
        
        text = data['text']
        if not text.strip():
            return jsonify({"error": "Text cannot be empty"}), 400

        cleaned_text = text_cleaner.clean_text(text)
        result = analyzer.predict(cleaned_text)
        
        response = {
            "original_text": text,
            "prediction": result
        }
        return jsonify(response)
        
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

# (The rest of the endpoints: /predict_batch, /train, etc., are unchanged)
# ...

if __name__ == '__main__':
    print("Starting Sentiment Analysis API...")
    app.run(debug=True, host='0.0.0.0', port=5000)