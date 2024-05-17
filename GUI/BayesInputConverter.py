import pandas as pd
import pickle
import re
import os

# Extract features from an email
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

# Load the trained model, feature selector, and scaler
def load_model(path='naive_bayes_model.pkl'):
    with open(path, 'rb') as file:
        model, selector, scaler = pickle.load(file)
    return model, selector, scaler

# Classify an email as spam or not spam
def classify_email(email, model, selector, scaler):
    features_df = extract_features(email)
    features_df_selected = selector.transform(features_df)
    features_df_scaled = scaler.transform(features_df_selected)
    prediction = model.predict(features_df_scaled)

    return prediction[0] == 1

# Example usage
email_content = "International Women's Day is a special occasion for us at LEAN HQ. It's a day when we're reminded to celebrate strength, empowerment and beauty. All qualities we aim to embody here at LEAN! So to share the celebration with you all we're offering you7 DAYS FREE ACCESS TO LEAN WITH LILLY 📲You don't need a code. Just tap the button below and take advantage of our exclusive International Women's Day offer now 💕START YOUR FREE TRIAL NOW And in MORE good news, some of your favourite LEAN products have finally restocked!!!"
model, selector, scaler = load_model()
result = classify_email(email_content, model, selector, scaler)
print("The email is classified as:", "Spam" if result else "Not Spam")
