from flask import Flask, request, jsonify
import pickle
import re
import pandas as pd
import logging
from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import scipy.sparse as sp

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model_SVM = None
model_Bayes = None
tfidf_vectorizer = None
sentiment_analyzer = SentimentIntensityAnalyzer()

def load_models():
    global model_SVM, model_Bayes, tfidf_vectorizer
    svm_folder = Path(__file__).resolve().parent.parent / 'Models'
    svm_file = svm_folder / 'best_svm_with_sentiment.pkl'  # updated model file name
    nb_folder = Path(__file__).resolve().parent.parent / 'Models'
    nb_file = nb_folder / 'best_bayes_with_sentiment.pkl'  # updated model file name
    vectorizer_file = svm_folder / 'tfidf_vectorizer1.pkl'

    model_SVM = load_model(svm_file)
    model_Bayes = load_model(nb_file)
    tfidf_vectorizer = load_model(vectorizer_file)
    if not model_SVM or not model_Bayes or not tfidf_vectorizer:
        logger.error('Model loading failed')
        raise Exception('Model loading failed')

def preprocess_text(text):
    if not isinstance(text, str):
        return ''

    # Convert to lowercase
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove email addresses
    text = re.sub(r'\S*@\S*\s?', '', text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stop words
    tokens = [word for word in tokens if word not in stopwords.words('english')]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    # Rejoin tokens into a single string
    text = ' '.join(tokens)

    return text

@app.route('/detect_spam', methods=['POST'])
def detect_spam():
    try:
        logger.info(f"Content-Type: {request.content_type}")
        logger.info(f"Request Data: {request.data.decode('utf-8')}")

        try:
            data = request.get_json(force=True)
        except Exception as e:
            logger.error(f"Error parsing JSON: {e}")
            return jsonify({"error": "Invalid JSON"}), 400

        logger.info(f"Received JSON data: {data}")

        if not data or 'text' not in data:
            logger.error('Invalid input')
            return jsonify({"error": "Invalid input"}), 400

        text = data['text']

        logger.info(f"Received text: {text}")

        # Preprocess text
        preprocessed_text = preprocess_text(text)

        # Sentiment analysis
        sentiment_scores = get_sentiment_scores(preprocessed_text)

        # Classification
        spam_result_SVM = classify_email(preprocessed_text, model_SVM)
        spam_result_Bayes = classify_email(preprocessed_text, model_Bayes)

        logger.info(f"SVM Result: {spam_result_SVM}")
        logger.info(f"Bayes Result: {spam_result_Bayes}")
        logger.info(f"Sentiment Scores: {sentiment_scores}")

        return jsonify({
            'spam_Bayes': spam_result_Bayes,
            'spam_SVM': spam_result_SVM,
            'sentiment_scores': sentiment_scores
        })
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

def classify_email(email, model):
    email_vectorized = tfidf_vectorizer.transform([email])

    # Get sentiment features
    sentiment_features = get_sentiment_features(email)
    sentiment_features_df = pd.DataFrame([sentiment_features])

    # Combine TF-IDF and sentiment features
    email_combined = sp.hstack((email_vectorized, sentiment_features_df))

    prediction = model.predict(email_combined)
    return 'Spam' if prediction[0] == 1 else 'Not Spam'

def get_sentiment_scores(text):
    sentiment_scores = sentiment_analyzer.polarity_scores(text)
    return {
        'negative': sentiment_scores['neg'],
        'neutral': sentiment_scores['neu'],
        'positive': sentiment_scores['pos'],
        'compound': sentiment_scores['compound']
    }

def get_sentiment_features(text):
    sentiment_scores = sentiment_analyzer.polarity_scores(text)
    return [
        sentiment_scores['neg'],
        sentiment_scores['neu'],
        sentiment_scores['pos'],
        sentiment_scores['compound']
    ]

def load_model(path):
    try:
        with open(path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        logger.error(f"Error loading model from {path}: {e}", exc_info=True)
        return None

if __name__ == '__main__':
    load_models()
    app.run(host='0.0.0.0', port=5000)
