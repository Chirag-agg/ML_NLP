# src/models/sentiment_analyzer.py

import joblib
from typing import Dict, List, Union, Optional

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

class SentimentAnalyzer:
    """A complete sentiment analyzer using a machine learning pipeline."""
    
    def __init__(self) -> None:
        """Initialize the sentiment analyzer."""
        self.pipeline: Optional[Pipeline] = None
        self.is_trained: bool = False
        self.training_accuracy: float = 0.0

    def _map_labels(self, labels: List[str]) -> List[int]:
        """Maps string labels to integers."""
        # Simple mapping, can be made more robust
        return [1 if label.lower() == 'positive' else 0 for label in labels]

    def train(self, texts: List[str], labels: List[str]) -> float:
        """Trains the model and returns the accuracy on the training data."""
        print("Starting model training...")
        
        int_labels = self._map_labels(labels)
        
        self.pipeline = Pipeline([
            ('vectorizer', TfidfVectorizer(max_features=10000, ngram_range=(1, 2))),
            ('classifier', LogisticRegression(max_iter=1000, random_state=42))
        ])
        
        self.pipeline.fit(texts, int_labels)
        self.is_trained = True
        
        predictions = self.pipeline.predict(texts)
        self.training_accuracy = accuracy_score(int_labels, predictions)
        print(f"✅ Model training complete. Training Accuracy: {self.training_accuracy:.4f}")
        return self.training_accuracy
        
    def predict(self, text: str) -> Dict[str, Union[str, float]]:
        """Predicts sentiment for a single text."""
        if not self.is_trained or not self.pipeline:
            raise RuntimeError("Model is not trained. Please train the model before making predictions.")
            
        probabilities = self.pipeline.predict_proba([text])[0]
        prediction_index = self.pipeline.predict([text])[0]
        
        sentiment = "Positive" if prediction_index == 1 else "Negative"
        confidence = probabilities[prediction_index]
        
        return {"sentiment": sentiment, "confidence": float(f"{confidence:.4f}")}

    def predict_batch(self, texts: List[str]) -> List[Dict[str, Union[str, float]]]:
        """Predicts sentiment for a list of texts."""
        if not self.is_trained or not self.pipeline:
            raise RuntimeError("Model is not trained.")

        probabilities = self.pipeline.predict_proba(texts)
        predictions = self.pipeline.predict(texts)
        
        results = []
        for i, pred_index in enumerate(predictions):
            sentiment = "Positive" if pred_index == 1 else "Negative"
            confidence = probabilities[i][pred_index]
            results.append({"sentiment": sentiment, "confidence": float(f"{confidence:.4f}")})
        return results

    def evaluate(self, texts: List[str], labels: List[str]) -> Dict[str, float]:
        """Evaluates the model on test data."""
        if not self.is_trained or not self.pipeline:
            raise RuntimeError("Model is not trained.")
            
        int_labels = self._map_labels(labels)
        predictions = self.pipeline.predict(texts)
        
        precision, recall, f1, _ = precision_recall_fscore_support(int_labels, predictions, average='binary')
        accuracy = accuracy_score(int_labels, predictions)
        
        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }

    def get_model_info(self) -> Dict[str, str]:
        """Gets information about the current model."""
        if not self.is_trained:
            return {"model_type": "Logistic Regression with TF-IDF", "status": "Untrained"}
        
        return {
            "model_type": "Logistic Regression with TF-IDF",
            "status": "Trained",
            "training_accuracy": f"{self.training_accuracy:.4f}"
        }

    def save_model(self, file_path: str):
        """Saves the entire trained pipeline to a file."""
        if not self.is_trained:
            raise RuntimeError("Cannot save an untrained model.")
        joblib.dump(self.pipeline, file_path)
        print(f"✅ Model pipeline saved to {file_path}")

    def load_model(self, file_path: str):
        """Loads a trained pipeline from a file."""
        self.pipeline = joblib.load(file_path)
        self.is_trained = True
        print(f"✅ Model pipeline loaded from {file_path}")