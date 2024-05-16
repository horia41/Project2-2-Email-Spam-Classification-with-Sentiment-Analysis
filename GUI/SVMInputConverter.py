import pandas as pd
from sklearn.naive_bayes import GaussianNB
import pickle  # for loading/saving the model
import re
import pandas as pd
from collections import Counter


# Extract features from an email
def extract_features(email):
    # Normalize the email text for consistent processing
    email_lower = email.lower()

    # Extract capital runs before normalizing to lowercase for accurate measurements
    capital_runs = re.findall(r'[A-Z]+', email)  # Use the original email text here
    run_lengths = [len(run) for run in capital_runs] if capital_runs else [0]

    # Prepare regex pattern to extract words from the lowercased email
    words = re.findall(r'\b\w+\b', email_lower)  # This pattern matches any word
    total_words = len(words) if words else 1  # Avoid division by zero

    # Count frequencies of specific words relevant to spam detection
    word_list = ["make", "address", "all", "3d", "our", "over", "remove",
                 "internet", "order", "mail", "receive", "will", "people", "report",
                 "addresses", "free", "business", "email", "you", "credit", "your",
                 "font", "000", "money", "hp", "hpl", "george", "650", "lab",
                 "labs", "telnet", "857", "data", "415", "85", "technology",
                 "1999", "parts", "pm", "direct", "cs", "meeting", "original",
                 "project", "re", "edu", "table", "conference"]

    word_freqs = {f"word_freq_{word}": 100 * words.count(word) / total_words for word in word_list}

    # Character frequency calculations
    char_freqs = {f"char_freq_{char}": 100 * email_lower.count(char) / len(email_lower)
                  for char in [';', '(', '[', '!', '$', '#']}

    # Capital letters run lengths features
    capital_run_features = {
        "capital_run_length_average": sum(run_lengths) / len(run_lengths) if run_lengths else 0,
        "capital_run_length_longest": max(run_lengths) if run_lengths else 0,
        "capital_run_length_total": sum(run_lengths)
    }

    # Combine all feature dictionaries into one
    features = {**word_freqs, **char_freqs, **capital_run_features}

    # Convert the features dictionary to a DataFrame with one row
    features_dataframe = pd.DataFrame([features])

    # Rename the columns to match 'feature_1' to 'feature_57'
    features_dataframe.columns = ['feature_' + str(i) for i in range(1, 58)]

    return features_dataframe


# Load the trained model
def load_model(path='C:\\Users\\mespi\\OneDrive\\Escritorio\\Project2.2\\Bayes\\naive_bayes_model.pkl'):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model


# Classify an email as spam or not spam
def classify_email(email, model):
    # Extract features from the email
    features_df = extract_features(email)

    # Predict using the trained model
    prediction = model.predict(features_df)

    # Interpret the prediction result
    if prediction[0] == 1:
        return True # Spam
    else:
        return False # no Spam

# Example usage
email_content = "Dear All, I’d like to invite you to our next meeting on Inclusivity in STEM and CS. Meeting notes will follow."  # This would be the email text you want to classify
model = load_model()
result = classify_email(email_content, model)
print("The email is classified as:", result)

