import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pickle
from pathlib import Path
import scipy.sparse as sp

# Load the TfidfVectorizer
model_folder = Path(__file__).resolve().parent.parent / 'Models'
vectorizer_file = model_folder / 'tfidf_vectorizer2.pkl'

with open(vectorizer_file, 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

# Load the trained model (change this to the model you want to test, e.g., SVM or Naive Bayes)
model_file_path = model_folder / 'best_svm_with_sentiment.pkl'
with open(model_file_path, 'rb') as file:
    model = pickle.load(file)

# Load the new data
data_folder = Path(__file__).resolve().parent.parent / 'spambase'
new_data_file = data_folder / 'processed_data_SMS_with_sentiment_advanced.data'
new_data = pd.read_csv(new_data_file, header=None, names=['Message', 'sentiment_neg', 'sentiment_neu', 'sentiment_pos', 'sentiment_compound', 'text_blob_polarity', 'text_blob_subjectivity', 'Category'])

# Ensure there are no NaN values
new_data['Message'] = new_data['Message'].fillna('').astype(str)

# Transform the new data using the loaded TfidfVectorizer
X_new_text = new_data['Message']
X_new_sentiment = new_data[['sentiment_neg', 'sentiment_neu', 'sentiment_pos', 'sentiment_compound', 'text_blob_polarity', 'text_blob_subjectivity']]

X_new_text_transformed = tfidf_vectorizer.transform(X_new_text)

# Combine text features with sentiment features
X_new_transformed = sp.hstack((X_new_text_transformed, sp.csr_matrix(X_new_sentiment)))

# Predict the labels for the new data
y_pred_new = model.predict(X_new_transformed)

# Map 'ham' to 0 and 'spam' to 1 for numerical labels for evaluation
label_mapping = {'ham': 0, 'spam': 1}
reverse_label_mapping = {v: k for k, v in label_mapping.items()}
new_data['Category'] = new_data['Category'].map(label_mapping)

# Calculate metrics for the new data
y_true = new_data['Category']
accuracy = accuracy_score(y_true, y_pred_new)
precision = precision_score(y_true, y_pred_new)
recall = recall_score(y_true, y_pred_new)
f1 = f1_score(y_true, y_pred_new)
conf_matrix = confusion_matrix(y_true, y_pred_new)

# Print the evaluation results for the new data
print("New Data Metrics:")
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'Confusion Matrix:\n{conf_matrix}')
