import re
from typing import List


class TextCleaner:
    """Text cleaner for sentiment analysis - participants can enhance."""
    
    def __init__(self) -> None:
        """Initialize the text cleaner."""
        # TODO: Participants can add configuration options here
        # Examples: self.remove_urls = True, self.remove_stopwords = False, etc.
        pass
        
    def clean_text(self, text: str) -> str:
        """
        Clean a single text string.
        
        Args:
            text: Input text to clean
            
        Returns:
            Cleaned text string
            
        TODO for participants:
        - Implement comprehensive text cleaning
        - Remove URLs, mentions, hashtags
        - Handle special characters and emojis
        - Remove stopwords
        - Handle contractions
        - Normalize repeated characters
        """
        if not text:
            return ""
            
        # Basic cleaning - participants can enhance
        cleaned = text.lower()
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        
        return cleaned
        
    def clean_texts(self, texts: List[str]) -> List[str]:
        """
        Clean a list of text strings.
        
        Args:
            texts: List of texts to clean
            
        Returns:
            List of cleaned text strings
            
        TODO for participants:
        - Implement batch processing optimization
        - Add parallel processing for large datasets
        - Add progress tracking for long operations
        """
        return [self.clean_text(text) for text in texts]
        
    def remove_urls(self, text: str) -> str:
        """
        Remove URLs from text.
        
        Args:
            text: Input text
            
        Returns:
            Text with URLs removed
            
        TODO for participants:
        - Implement URL detection and removal
        - Handle different URL formats
        - Preserve text around URLs
        """
        # Function body - participants need to implement
        return text
        
    def remove_mentions(self, text: str) -> str:
        """
        Remove @mentions from text.
        
        Args:
            text: Input text
            
        Returns:
            Text with mentions removed
            
        TODO for participants:
        - Remove @username patterns
        - Handle edge cases
        """
        # Function body - participants need to implement
        return text
        
    def remove_hashtags(self, text: str) -> str:
        """
        Remove #hashtags from text.
        
        Args:
            text: Input text
            
        Returns:
            Text with hashtags removed
            
        TODO for participants:
        - Remove #hashtag patterns
        - Decide whether to keep hashtag text or remove entirely
        """
        # Function body - participants need to implement
        return text
        
    def remove_stopwords(self, text: str) -> str:
        """
        Remove stopwords from text.
        
        Args:
            text: Input text
            
        Returns:
            Text with stopwords removed
            
        TODO for participants:
        - Implement stopword removal
        - Use NLTK or custom stopword lists
        - Handle different languages
        """
        # Function body - participants need to implement
        return text
        
    def handle_contractions(self, text: str) -> str:
        """
        Expand contractions in text.
        
        Args:
            text: Input text
            
        Returns:
            Text with contractions expanded
            
        TODO for participants:
        - Expand contractions (don't -> do not)
        - Handle various contraction forms
        - Maintain text meaning
        """
        # Function body - participants need to implement
        return text


# TODO for participants - Additional text preprocessing features:
# - Stemming and lemmatization
# - Part-of-speech tagging
# - Named entity recognition
# - Sentiment-aware preprocessing
# - Language detection
# - Text normalization
# - Spell checking and correction
# - Emoji handling and sentiment mapping
# - Slang and abbreviation expansion
# - Text augmentation techniques
