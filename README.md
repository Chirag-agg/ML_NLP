# All-in-One Sentiment Analysis API

This repository contains a complete, end-to-end sentiment analysis project consolidated into a single Python script. The application can be run in two modes: `train` to build the model from a dataset, and `api` to serve predictions via a Flask web server.

## ✨ Features

-   **Sentiment Classification**: Predicts if a given text is **Positive** or **Negative**.
-   **RESTful API**: Exposes the model through a robust Flask API.
-   **Command-Line Interface**: Easily switch between training and serving modes.
-   **Model Persistence**: The trained model is saved and can be loaded on API startup.

## ⚙️ Setup and Installation

Follow these steps to set up and run the project locally.

#### 1. Get the Code
Download the `app.py` and `requirements.txt` files into a new folder.

#### 2. Create a Virtual Environment (Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate


