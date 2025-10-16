# preprocessing/text_cleaner.py

import re
import nltk
from typing import List
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TextCleaner:
    """A class to handle all text preprocessing."""
    
    def __init__(self):
        self._initialize_nltk_resources()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def _initialize_nltk_resources(self):
        """Check for and download NLTK resources if missing."""
        resources = ['stopwords', 'wordnet', 'omw-1.4']
        for resource in resources:
            try:
                nltk.data.find(f'corpora/{resource}')
            except LookupError:
                print(f"Downloading NLTK resource: {resource}...")
                nltk.download(resource, quiet=True)

    def clean_text(self, text: str) -> str:
        """Cleans and preprocesses a single string of text."""
        text = str(text).lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'\@\w+|\#','', text)
        text = re.sub(r'[^a-z\s]', '', text)
        tokens = text.split()
        lemmatized_tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        return " ".join(lemmatized_tokens)
        
    def clean_texts(self, texts: List[str]) -> List[str]:
        """Cleans and preprocesses a list of texts."""
        return [self.clean_text(text) for text in texts]