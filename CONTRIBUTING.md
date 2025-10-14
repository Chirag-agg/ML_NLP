# Sentiment Analysis Competition Track

Build a complete sentiment analysis system from this barebones repository.

## Your Mission

Transform the skeleton code into a working sentiment analysis API that classifies text as positive, negative, or neutral.

## What You Must Build

### Core Requirements
1. **ML Model** (`src/models/sentiment_analyzer.py`) - Implement actual sentiment classification
2. **Text Preprocessing** (`preprocessing/text_cleaner.py`) - Clean text (URLs, mentions, contractions, etc.)
3. **API Integration** (`api/app.py`) - Replace placeholder responses with real predictions
4. **Tests** (`tests/`) - >80% coverage, test accuracy and edge cases

### Performance Requirements
- **Accuracy**: >70% required, >85% excellent
- **Speed**: <1s single prediction, <10s for 100 predictions
- **Coverage**: >80% test coverage

## Quick Start

```bash
# Setup
git clone <your-fork>
cd sentiment-analysis-competition
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Test skeleton API
python api/app.py
# Visit http://localhost:5000
```

## Implementation Strategy

### Step 1: Choose ML Approach
- **Traditional**: scikit-learn + TF-IDF (Naive Bayes, SVM, Logistic Regression)
- **Deep Learning**: Transformers (BERT, RoBERTa) or LSTM
- **Hybrid**: Ensemble multiple models

### Step 2: Core Implementation
```python
# SentimentAnalyzer class needs:
def train(self, texts, labels): pass
def predict(self, text): return {"sentiment": "positive", "confidence": 0.85}
def predict_batch(self, texts): pass

# TextCleaner needs comprehensive cleaning:
def clean_text(self, text):
    # Remove URLs, mentions, hashtags
    # Handle contractions, emojis, special chars
    # Optional: remove stopwords
```

### Step 3: Connect to API
Replace all placeholder responses in `api/app.py` endpoints:
- `/predict` - Single prediction
- `/predict_batch` - Batch predictions  
- `/train` - Model training
- `/model/evaluate` - Performance metrics

## Evaluation Criteria

- **Technical** (60%): Model performance, code quality, testing
- **Innovation** (25%): Advanced features, novel approaches
- **Documentation** (15%): README, code comments, analysis

## Bonus Features (Extra Points)
- Ensemble methods
- Real-time learning
- Model explainability
- Performance optimization
- Multi-language support

## Submission Checklist

- [ ] Model achieves >70% accuracy
- [ ] All API endpoints work with real predictions
- [ ] >80% test coverage
- [ ] Updated README with usage instructions
- [ ] Code follows Python standards (PEP 8)
- [ ] Performance requirements met

## Tips for Success

1. **Start Simple**: Get basic Naive Bayes working first
2. **Test Early**: Write tests as you build
3. **Optimize Later**: Focus on working code, then improve accuracy
4. **Handle Edge Cases**: Empty text, special characters, long text
5. **Document Everything**: Clear README and code comments

## Resources

**Datasets**: IMDB reviews, Stanford Sentiment Treebank, Twitter sentiment
**Libraries**: scikit-learn, transformers, nltk, pandas, flask
**Metrics**: accuracy, precision, recall, F1-score

## Final Submission

1. Ensure all tests pass: `pytest --cov=src`
2. Test API manually: `python api/app.py`
3. Push final code to your repository
4. Submit repository URL with brief description

**Goal**: Build a production-ready sentiment analysis system that works reliably and performs well. Start coding! 🚀