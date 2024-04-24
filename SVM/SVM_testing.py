import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# Load the dataset
data_path = r'Project2-2/Bayes/spambase/spambase.data'
column_names = [
    'word_freq_' + str(i) for i in range(1, 49)
] + [
    'char_freq_' + str(i) for i in range(1, 7)
] + [
    'capital_run_length_average',
    'capital_run_length_longest',
    'capital_run_length_total',
    'label'
]

df = pd.read_csv(data_path, header=None, names=column_names)

# Split the dataset into features and target variable
X = df.drop('label', axis=1)
y = df['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the SVM classifier
classifier = SVC(kernel='linear', random_state=42)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)


# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Print the evaluation results
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'Confusion Matrix:\n{conf_matrix}')

def text_to_features(text):
    # Tokenize the text into words
    words = text.lower().split()
    
    # Initialize feature vector with zeros
    features = np.zeros(len(column_names) - 1)  # Exclude the label column
    
    # Define word frequency features
    word_freq_features = [
        'make', 'address', 'all', '3d', 'our', 'over', 'remove', 'internet', 'order', 'mail',
        'receive', 'will', 'people', 'report', 'addresses', 'free', 'business', 'email', 'you',
        'credit', 'your', 'font', '000', 'money', 'hp', 'hpl', 'george', '650', 'lab', 'labs',
        'telnet', '857', 'data', '415', '85', 'technology', '1999', 'parts', 'pm', 'direct',
        'cs', 'meeting', 'original', 'project', 're', 'edu', 'table', 'conference'
    ]
    
    # Count word frequency in the text
    for word in words:
        if word in word_freq_features:
            index = column_names.index('word_freq_' + word)
            features[index] += 1
    
    # Define character frequency features
    char_freq_features = [';', '(', '[', '!', '$', '#']
    
    # Count character frequency in the text
    for char in text:
        if char in char_freq_features:
            index = column_names.index('char_freq_' + char)
            features[index] += 1
    
    # Calculate capital run length features
    capital_run_length_average = sum(1 for c in text if c.isupper()) / len(words)
    capital_run_length_longest = max(sum(1 for c in word if c.isupper()) for word in words)
    capital_run_length_total = sum(1 for c in text if c.isupper())
    
    # Append capital run length features
    features[-3] = capital_run_length_average
    features[-2] = capital_run_length_longest
    features[-1] = capital_run_length_total
    
    return features

# Example text
text = "i dont know just for testing make make money all make.......!!"

# Convert text to features
text_features = text_to_features(text)

print(text_features)