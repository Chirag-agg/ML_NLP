from typing import Dict, List, Optional, Union


class SentimentAnalyzer:
    """Basic sentiment analyzer - participants need to implement ML models."""
    
    def __init__(self) -> None:
        """Initialize the sentiment analyzer."""
        # TODO: Participants can add model initialization here
        # Examples: self.model = None, self.vectorizer = None, etc.
        pass
        
    def train(self, texts: List[str], labels: List[str]) -> None:
        """
        Train the sentiment analysis model.
        
        Args:
            texts: List of training texts
            labels: List of corresponding sentiment labels
            
        TODO for participants:
        - Implement model training logic
        - Add data preprocessing
        - Choose and train ML model (Naive Bayes, SVM, Neural Network, etc.)
        - Store trained model for predictions
        """
        # Function body - participants need to implement
        pass
        
    def predict(self, text: str) -> Dict[str, Union[str, float]]:
        """
        Predict sentiment for a single text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with 'sentiment' and 'confidence' keys
            
        TODO for participants:
        - Implement prediction logic
        - Return sentiment (positive/negative/neutral)
        - Return confidence score (0.0 to 1.0)
        - Handle edge cases (empty text, etc.)
        """
        # Function body - participants need to implement
        return {"sentiment": "neutral", "confidence": 0.5}
        
    def predict_batch(self, texts: List[str]) -> List[Dict[str, Union[str, float]]]:
        """
        Predict sentiment for multiple texts.
        
        Args:
            texts: List of texts to analyze
            
        Returns:
            List of dictionaries with sentiment predictions
            
        TODO for participants:
        - Implement batch prediction for efficiency
        - Process multiple texts at once
        - Return list of prediction dictionaries
        """
        # Function body - participants need to implement
        return [{"sentiment": "neutral", "confidence": 0.5} for _ in texts]
        
    def get_model_info(self) -> Dict[str, str]:
        """
        Get information about the current model.
        
        Returns:
            Dictionary containing model information
            
        TODO for participants:
        - Return model type, training status, accuracy, etc.
        - Add model metadata
        """
        # Function body - participants need to implement
        return {"model_type": "not_implemented", "status": "untrained"}


# TODO for participants - Additional features to implement:
# - Model evaluation and metrics
# - Hyperparameter tuning
# - Cross-validation
# - Model persistence (save/load)
# - Different ML algorithms (SVM, Random Forest, Neural Networks)
# - Feature engineering
# - Model comparison tools
# - Real-time prediction API
# - Batch processing optimization
