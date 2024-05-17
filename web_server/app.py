from flask import Flask, request, jsonify
import pickle
import re
import pandas as pd
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load models
model_SVM_path = 'C:\\Users\\vasea\\OneDrive\\Documents\\GitHub\\Project2-2\\SVM\\SVM_model.pkl'
model_Bayes_path = 'C:\\Users\\vasea\\OneDrive\\Documents\\GitHub\\Project2-2\\Bayes\\naive_bayes_model.pkl'

model_SVM = None
model_Bayes = None

def load_models():
    global model_SVM, model_Bayes
    model_SVM = load_model(model_SVM_path)
    model_Bayes = load_model(model_Bayes_path)
    if not model_SVM or not model_Bayes:
        logger.error('Model loading failed')
        raise Exception('Model loading failed')

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

        spam_result_SVM = classify_email(text, model_SVM)
        spam_result_Bayes = classify_email(text, model_Bayes)

        logger.info(f"SVM Result: {spam_result_SVM}")
        logger.info(f"Bayes Result: {spam_result_Bayes}")

        return jsonify({'spam_Bayes': spam_result_Bayes, 'spam_SVM': spam_result_SVM})
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

def classify_email(email, model):
    features_df = extract_features(email)
    prediction = model.predict(features_df)
    return 'Spam' if prediction[0] == 1 else 'Not Spam'

def extract_features(email):
    email_lower = email.lower()
    capital_runs = re.findall(r'[A-Z]+', email)
    run_lengths = [len(run) for run in capital_runs] if capital_runs else [0]
    words = re.findall(r'\b\w+\b', email_lower)
    total_words = len(words) if words else 1

    word_list = ["make", "address", "all", "3d", "our", "over", "remove",
                 "internet", "order", "mail", "receive", "will", "people", "report",
                 "addresses", "free", "business", "email", "you", "credit", "your",
                 "font", "000", "money", "hp", "hpl", "george", "650", "lab",
                 "labs", "telnet", "857", "data", "415", "85", "technology",
                 "1999", "parts", "pm", "direct", "cs", "meeting", "original",
                 "project", "re", "edu", "table", "conference"]
    word_freqs = {f"word_freq_{word}": 100 * words.count(word) / total_words for word in word_list}

    char_freqs = {f"char_freq_{char}": 100 * email_lower.count(char) / len(email_lower)
                  for char in [';', '(', '[', '!', '$', '#']}

    capital_run_features = {
        "capital_run_length_average": sum(run_lengths) / len(run_lengths) if run_lengths else 0,
        "capital_run_length_longest": max(run_lengths) if run_lengths else 0,
        "capital_run_length_total": sum(run_lengths)
    }

    features = {**word_freqs, **char_freqs, **capital_run_features}
    features_dataframe = pd.DataFrame([features])
    features_dataframe.columns = ['feature_' + str(i) for i in range(1, 58)]

    return features_dataframe

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
