# Contributing to Sentiment Analysis project

This document provides guidelines and information for contributors.

##  Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contribution Process](#contribution-process)
- [Coding Standards](#coding-standards)
- [Issue Guidelines](#issue-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Guidelines](#documentation-guidelines)

##  Submission Requirements

### Quality Standards
- Code must be functional and tested
- Documentation must be clear and complete
- Solutions must address the issue requirements
- Performance should be reasonable for the task

### Deadline
- Submissions must be made before the competition deadline
- Late submissions will not be accepted
- Extensions may be granted for technical issues (contact organizers)

## 📝 Submission Format

### Pull Request Structure
1. **Title**: Clear, descriptive title referencing the issue number
2. **Description**: Detailed explanation of changes and approach
3. **Code**: Well-structured, commented code
4. **Tests**: Unit tests for new functionality
5. **Documentation**: Updated README or code comments

### Required Information
- Issue number being addressed
- Approach taken to solve the problem
- Any assumptions or limitations
- Testing performed
- Performance considerations

### File Organization
- Follow existing project structure
- Use meaningful file and function names
- Group related functionality together
- Maintain consistent coding style

## 🔧 Technical Guidelines

### Code Quality
- Write clean, readable code with proper comments
- Follow Python PEP 8 style guidelines
- Use meaningful variable and function names
- Implement proper error handling
- Add type hints where appropriate

### Testing Requirements
- Write unit tests for new functionality
- Ensure all tests pass before submission
- Test edge cases and error conditions
- Maintain or improve test coverage

### Performance Considerations
- Optimize for reasonable performance
- Consider memory usage for large datasets
- Document any performance trade-offs
- Use efficient algorithms and data structures

### Documentation Standards
- Update README if adding new features
- Add docstrings to all functions and classes
- Include usage examples where helpful
- Document any breaking changes

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of sentiment analysis concepts
- Familiarity with Python development

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-competition.git
   cd sentiment-analysis-competition
   ```

3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/originalowner/sentiment-analysis-competition.git
   ```

## 🛠️ Development Setup

### Environment Setup

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

3. **Install pre-commit hooks** (optional but recommended):
   ```bash
   pre-commit install
   ```

4. **Install the package in development mode**:
   ```bash
   pip install -e .
   ```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v
```

## 📝 Contribution Process

### 1. Choose an Issue

- Browse the [Issues](https://github.com/yourusername/sentiment-analysis-competition/issues) tab
- Look for issues labeled with your skill level:
  - 🟢 `good first issue`: Perfect for beginners
  - 🟡 `intermediate`: Requires some experience
  - 🔴 `advanced`: Complex tasks for experienced developers

### 2. Claim an Issue

- Comment on the issue to express your interest
- Wait for maintainer approval before starting work
- This prevents duplicate work

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number
```

### 4. Make Changes

- Write clean, readable code
- Add tests for new functionality
- Update documentation as needed
- Follow the coding standards below

### 5. Test Your Changes

```bash
# Run tests
pytest

# Check code style
flake8 src/
black --check src/
isort --check-only src/

# Type checking
mypy src/
```

### 6. Commit Changes

Use clear, descriptive commit messages:

```bash
git add .
git commit -m "Add sentiment analysis for emoji handling

- Implement emoji sentiment mapping
- Add tests for emoji processing
- Update documentation"
```

### 7. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## 📏 Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Line length**: 88 characters (Black formatter standard)
- **Import order**: isort configuration
- **Type hints**: Use type hints for function parameters and return values
- **Docstrings**: Use Google-style docstrings

### Code Formatting

We use automated formatting tools:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

Run formatting before committing:

```bash
black src/ tests/
isort src/ tests/
```

### Example Code Style

```python
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class SentimentAnalyzer:
    """A sentiment analysis class for text processing.
    
    This class provides methods for analyzing sentiment in text using
    various machine learning models.
    
    Args:
        model_type: Type of model to use ('naive_bayes', 'svm', 'neural')
        confidence_threshold: Minimum confidence for predictions
    """
    
    def __init__(
        self, 
        model_type: str = "naive_bayes",
        confidence_threshold: float = 0.5
    ) -> None:
        self.model_type = model_type
        self.confidence_threshold = confidence_threshold
        self.model = None
        
    def predict(self, text: str) -> Dict[str, float]:
        """Predict sentiment for given text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing sentiment and confidence score
            
        Raises:
            ValueError: If text is empty or model not trained
        """
        if not text.strip():
            raise ValueError("Text cannot be empty")
            
        if self.model is None:
            raise ValueError("Model must be trained before prediction")
            
        # Implementation here
        pass
```

## 🐛 Issue Guidelines

### Reporting Bugs

When reporting bugs, please include:

1. **Clear title**: Brief description of the issue
2. **Steps to reproduce**: Detailed steps to reproduce the bug
3. **Expected behavior**: What you expected to happen
4. **Actual behavior**: What actually happened
5. **Environment**: Python version, OS, package versions
6. **Screenshots**: If applicable
7. **Code samples**: Minimal code to reproduce the issue

### Requesting Features

When requesting features, please include:

1. **Clear title**: Brief description of the feature
2. **Use case**: Why this feature would be useful
3. **Proposed solution**: How you think it should work
4. **Alternatives**: Other solutions you've considered
5. **Additional context**: Any other relevant information

## 🔄 Pull Request Guidelines

### PR Template

Use the provided PR template and fill out all sections:

- **Description**: What changes were made and why
- **Type of change**: Bug fix, feature, documentation, etc.
- **Testing**: How the changes were tested
- **Checklist**: Ensure all items are completed

### PR Requirements

- [ ] Code follows the project's coding standards
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated if needed
- [ ] No merge conflicts
- [ ] PR is linked to an issue
- [ ] Commit messages are clear and descriptive

### Review Process

1. **Automated checks**: CI/CD pipeline runs tests and checks
2. **Code review**: Maintainers review the code
3. **Feedback**: Address any feedback or requested changes
4. **Approval**: Once approved, the PR will be merged

## 🧪 Testing Guidelines

### Test Structure

```
tests/
├── unit/                 # Unit tests
│   ├── test_models.py
│   ├── test_preprocessing.py
│   └── test_evaluation.py
├── integration/          # Integration tests
│   ├── test_api.py
│   └── test_pipeline.py
└── fixtures/             # Test data
    ├── sample_texts.json
    └── expected_results.json
```

### Writing Tests

- **Test coverage**: Aim for >80% code coverage
- **Test names**: Use descriptive names that explain what is being tested
- **Test isolation**: Each test should be independent
- **Mocking**: Use mocks for external dependencies
- **Fixtures**: Use pytest fixtures for common test data

### Example Test

```python
import pytest
from src.models.sentiment_analyzer import SentimentAnalyzer


class TestSentimentAnalyzer:
    """Test cases for SentimentAnalyzer class."""
    
    @pytest.fixture
    def analyzer(self):
        """Create a SentimentAnalyzer instance for testing."""
        return SentimentAnalyzer()
    
    def test_predict_positive_text(self, analyzer):
        """Test sentiment prediction for positive text."""
        # Arrange
        text = "I love this product!"
        
        # Act
        result = analyzer.predict(text)
        
        # Assert
        assert result['sentiment'] == 'positive'
        assert result['confidence'] > 0.5
    
    def test_predict_empty_text_raises_error(self, analyzer):
        """Test that empty text raises ValueError."""
        with pytest.raises(ValueError, match="Text cannot be empty"):
            analyzer.predict("")
```

## 📚 Documentation Guidelines

### Code Documentation

- **Docstrings**: All public functions and classes need docstrings
- **Comments**: Add comments for complex logic
- **Type hints**: Use type hints for better code understanding

### API Documentation

- **Endpoint documentation**: Document all API endpoints
- **Request/response examples**: Provide examples for API usage
- **Error codes**: Document possible error responses

### User Documentation

- **README updates**: Update README for new features
- **Tutorial notebooks**: Create notebooks for complex features
- **Changelog**: Update CHANGELOG.md for significant changes

## 🏆 Competition Scoring

Your contributions will be evaluated based on:

### Code Quality (40%)
- Clean, readable code
- Proper error handling
- Efficient algorithms
- Good test coverage

### Functionality (30%)
- Correct implementation
- Meets requirements
- Handles edge cases
- Performance considerations

### Documentation (20%)
- Clear docstrings
- Updated README
- Code comments
- API documentation

### Testing (10%)
- Comprehensive tests
- Edge case coverage
- Integration tests
- Performance tests


---

Thank you for contributing to the Sentiment Analysis Competition! Your contributions help make this project better for everyone. 🚀
