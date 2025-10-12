"""
Flask API for sentiment analysis - participants need to integrate ML models.
"""

from flask import Flask, request, jsonify
from typing import Dict, List
import sys
import os

# Add src to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.sentiment_analyzer import SentimentAnalyzer
from preprocessing.text_cleaner import TextCleaner

app = Flask(__name__)

# Initialize components - participants can enhance
analyzer = SentimentAnalyzer()
text_cleaner = TextCleaner()

# TODO for participants: Add model training endpoint
# TODO for participants: Add model persistence (save/load)
# TODO for participants: Add model evaluation endpoints


@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint - API information.
    
    TODO for participants:
    - Add API documentation
    - Add model status information
    - Add usage examples
    """
    return jsonify({
        "message": "Sentiment Analysis API",
        "status": "running",
        "endpoints": {
            "predict": "/predict",
            "predict_batch": "/predict_batch",
            "health": "/health"
        }
    })


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    
    TODO for participants:
    - Add model status check
    - Add database connectivity check
    - Add performance metrics
    """
    return jsonify({
        "status": "healthy",
        "model_trained": False,  # TODO: Check if model is trained
        "version": "1.0.0"
    })


@app.route('/predict', methods=['POST'])
def predict_sentiment():
    """
    Predict sentiment for a single text.
    
    Expected JSON:
    {
        "text": "I love this product!"
    }
    
    TODO for participants:
    - Implement actual ML prediction
    - Add input validation
    - Add error handling
    - Add response caching
    - Add rate limiting
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Text field is required"}), 400
            
        text = data['text']
        
        if not text or not text.strip():
            return jsonify({"error": "Text cannot be empty"}), 400
        
        # Clean the text
        cleaned_text = text_cleaner.clean_text(text)
        
        # TODO: Participants need to implement actual prediction
        # result = analyzer.predict(cleaned_text)
        
        # Placeholder response - participants need to replace
        result = {
            "original_text": text,
            "cleaned_text": cleaned_text,
            "sentiment": "neutral",  # TODO: Get from ML model
            "confidence": 0.5,       # TODO: Get from ML model
            "model_info": analyzer.get_model_info()
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    """
    Predict sentiment for multiple texts.
    
    Expected JSON:
    {
        "texts": ["I love this!", "This is terrible!", "It's okay."]
    }
    
    TODO for participants:
    - Implement batch prediction
    - Add batch size limits
    - Add progress tracking for large batches
    - Optimize for performance
    """
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({"error": "Texts field is required"}), 400
            
        texts = data['texts']
        
        if not texts or not isinstance(texts, list):
            return jsonify({"error": "Texts must be a non-empty list"}), 400
        
        if len(texts) > 100:  # TODO: Make configurable
            return jsonify({"error": "Batch size too large (max 100)"}), 400
        
        # Clean the texts
        cleaned_texts = text_cleaner.clean_texts(texts)
        
        # TODO: Participants need to implement actual batch prediction
        # results = analyzer.predict_batch(cleaned_texts)
        
        # Placeholder response - participants need to replace
        results = []
        for i, (original, cleaned) in enumerate(zip(texts, cleaned_texts)):
            results.append({
                "index": i,
                "original_text": original,
                "cleaned_text": cleaned,
                "sentiment": "neutral",  # TODO: Get from ML model
                "confidence": 0.5        # TODO: Get from ML model
            })
        
        return jsonify({
            "results": results,
            "total_processed": len(texts),
            "model_info": analyzer.get_model_info()
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/train', methods=['POST'])
def train_model():
    """
    Train the sentiment analysis model.
    
    Expected JSON:
    {
        "texts": ["I love this!", "This is terrible!"],
        "labels": ["positive", "negative"]
    }
    
    TODO for participants:
    - Implement model training
    - Add training data validation
    - Add training progress tracking
    - Add model evaluation after training
    - Add training metrics endpoint
    """
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data or 'labels' not in data:
            return jsonify({"error": "Texts and labels fields are required"}), 400
            
        texts = data['texts']
        labels = data['labels']
        
        if len(texts) != len(labels):
            return jsonify({"error": "Texts and labels must have the same length"}), 400
        
        if len(texts) < 10:
            return jsonify({"error": "At least 10 training samples required"}), 400
        
        # Clean the training texts
        cleaned_texts = text_cleaner.clean_texts(texts)
        
        # TODO: Participants need to implement actual training
        # analyzer.train(cleaned_texts, labels)
        
        # Placeholder response - participants need to replace
        return jsonify({
            "message": "Training completed (placeholder)",
            "samples_trained": len(texts),
            "model_info": analyzer.get_model_info()
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/model/info', methods=['GET'])
def model_info():
    """
    Get information about the current model.
    
    TODO for participants:
    - Return detailed model information
    - Add model performance metrics
    - Add training history
    - Add model configuration
    """
    try:
        info = analyzer.get_model_info()
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/model/evaluate', methods=['POST'])
def evaluate_model():
    """
    Evaluate model performance on test data.
    
    Expected JSON:
    {
        "texts": ["I love this!", "This is terrible!"],
        "labels": ["positive", "negative"]
    }
    
    TODO for participants:
    - Implement model evaluation
    - Calculate accuracy, precision, recall, F1
    - Add confusion matrix
    - Add detailed performance metrics
    """
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data or 'labels' not in data:
            return jsonify({"error": "Texts and labels fields are required"}), 400
        
        # TODO: Participants need to implement actual evaluation
        # metrics = analyzer.evaluate(data['texts'], data['labels'])
        
        # Placeholder response - participants need to replace
        return jsonify({
            "message": "Evaluation completed (placeholder)",
            "accuracy": 0.0,
            "precision": 0.0,
            "recall": 0.0,
            "f1_score": 0.0
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # TODO for participants:
    # - Add configuration management
    # - Add logging
    # - Add error handling
    # - Add API documentation
    # - Add authentication/authorization
    # - Add rate limiting
    # - Add monitoring and metrics
    
    print("Starting Sentiment Analysis API...")
    print("TODO: Participants need to implement ML models!")
    print("Available endpoints:")
    print("- POST /predict - Single text prediction")
    print("- POST /predict_batch - Batch text prediction")
    print("- POST /train - Train the model")
    print("- GET /model/info - Model information")
    print("- POST /model/evaluate - Evaluate model performance")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
