# train.py

import pandas as pd
import os
from src.models.sentiment_analyzer import SentimentAnalyzer

def main():
    """
    Main function to load data, train the sentiment model, and save it.
    """
    print("--- Starting the Training Process ---")
    
    # 1. Define the path to your dataset
    sentiment_file_path = "C:/Users/caagg/Downloads/training.1600000.processed.noemoticon.csv"
    
    # 2. Load your dataset
    try:
        col_names = ['target', 'ids', 'date', 'flag', 'user', 'text']
        dtype_spec = {'target': int, 'ids': str}
        
        df = pd.read_csv(
            sentiment_file_path,
            encoding='latin-1',
            header=0, # ✅ FIX: Changed from 'None' to '0' to correctly handle the header row.
            names=col_names,
            dtype=dtype_spec
        )
        print("✅ Dataset loaded successfully.")
    except FileNotFoundError:
        print(f"🚨 FATAL: Training file not found at '{sentiment_file_path}'.")
        print("🚨 Please update the 'sentiment_file_path' variable in train.py.")
        return

    # 3. Prepare the data for training
    df_sample = df.sample(n=100000, random_state=42)
    df_sample['target'] = df_sample['target'].replace(4, 1)
    texts = df_sample['text'].tolist()
    labels = df_sample['target'].tolist()

    # 4. Train the model
    analyzer = SentimentAnalyzer()
    string_labels = ['positive' if label == 1 else 'negative' for label in labels]
    analyzer.train(texts, string_labels)

    # 5. Save the trained model pipeline
    model_save_path = "sentiment_pipeline.pkl"
    analyzer.save_model(model_save_path)
    
    print(f"\n--- ✅ Training Process Finished. Model saved to '{model_save_path}' ---")

if __name__ == '__main__':
    main()