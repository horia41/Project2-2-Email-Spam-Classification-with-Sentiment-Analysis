import pandas as pd
import re
from pathlib import Path

# Load the provided Enron dataset
data_folder = Path(__file__).resolve().parent.parent / 'spambase'
data_file = data_folder / 'enron_spam_data.csv'
enron_spam_data = pd.read_csv(data_file)

# Function to extract features from an email
def extract_features(email):
    if not isinstance(email, str):
        email = ''

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
    word_freqs = [100 * words.count(word) / total_words for word in word_list]

    char_list = [';', '(', '[', '!', '$', '#']
    char_freqs = [100 * email_lower.count(char) / len(email_lower) if len(email_lower) > 0 else 0 for char in char_list]

    capital_run_features = [
        sum(run_lengths) / len(run_lengths) if run_lengths else 0,
        max(run_lengths) if run_lengths else 0,
        sum(run_lengths)
    ]

    return word_freqs + char_freqs + capital_run_features

# Apply feature extraction to the Enron dataset
features = enron_spam_data['Message'].apply(extract_features).tolist()
features_df = pd.DataFrame(features, columns=[f'feature_{i}' for i in range(1, 58)])

# Map 'Spam/Ham' to binary labels (1 for spam, 0 for ham)
enron_spam_data['Spam/Ham'] = enron_spam_data['Spam/Ham'].map({'spam': 1, 'ham': 0})

# Combine features and labels into a single DataFrame
transformed_data = pd.concat([features_df, enron_spam_data['Spam/Ham']], axis=1)

# Save the transformed data to a .data file
output_path = 'transformed_enron_spam_data.data'  # Update this path if needed
transformed_data.to_csv(output_path, index=False, header=False)

print(f"Transformed data saved to {output_path}")
