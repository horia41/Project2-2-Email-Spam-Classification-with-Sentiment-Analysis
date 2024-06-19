import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pickle
from pathlib import Path
import time

# Load the processed data
data_folder = Path(__file__).resolve().parent.parent / 'spambase'
processed_data_file = data_folder / 'processed_data1.data'
processed_data = pd.read_csv(processed_data_file, header=None, names=['Message', 'Category'])

# Ensure there are no NaN values
processed_data['Message'] = processed_data['Message'].fillna('')

# Map 'ham' to 0 and 'spam' to 1 for numerical labels
label_mapping = {'ham': 0, 'spam': 1}
processed_data['Category'] = processed_data['Category'].map(label_mapping)

# Separate features and labels
X = processed_data['Message']
y = processed_data['Category']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a TfidfVectorizer and transform the training data
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_train_transformed = tfidf_vectorizer.fit_transform(X_train)
X_test_transformed = tfidf_vectorizer.transform(X_test)

# Save the TfidfVectorizer
model_folder = Path(__file__).resolve().parent.parent / 'Models'
vectorizer_file = model_folder / 'tfidf_vectorizer1.pkl'
with open(vectorizer_file, 'wb') as file:
    pickle.dump(tfidf_vectorizer, file)

# Initialize the MultinomialNB classifier
classifier = MultinomialNB()

# Define parameter grid for GridSearch
param_grid = {
    'alpha': [0.1, 0.5, 1.0]
}

# Perform GridSearch to find the best parameters
start_time = time.time()
grid_search = GridSearchCV(classifier, param_grid, cv=5, scoring='f1')
grid_search.fit(X_train_transformed, y_train)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Training completed in {elapsed_time // 60:.0f} minutes and {elapsed_time % 60:.0f} seconds.")

# Best model from GridSearch
best_model = grid_search.best_estimator_

# Make predictions on the test set
y_pred = best_model.predict(X_test_transformed)
y_pred_train = best_model.predict(X_train_transformed)

# Map numerical labels back to string labels
reverse_label_mapping = {v: k for k, v in label_mapping.items()}
y_test_str = y_test.map(reverse_label_mapping)
y_pred_str = pd.Series(y_pred).map(reverse_label_mapping)
y_train_str = y_train.map(reverse_label_mapping)
y_pred_train_str = pd.Series(y_pred_train).map(reverse_label_mapping)

# Calculate metrics for the test set and training set, including accuracy, precision, recall, F1 score, and confusion matrix
accuracy_test = accuracy_score(y_test_str, y_pred_str)
precision_test = precision_score(y_test_str, y_pred_str, pos_label='spam')
recall_test = recall_score(y_test_str, y_pred_str, pos_label='spam')
f1_test = f1_score(y_test_str, y_pred_str, pos_label='spam')
conf_matrix_test = confusion_matrix(y_test_str, y_pred_str)

accuracy_train = accuracy_score(y_train_str, y_pred_train_str)
precision_train = precision_score(y_train_str, y_pred_train_str, pos_label='spam')
recall_train = recall_score(y_train_str, y_pred_train_str, pos_label='spam')
f1_train = f1_score(y_train_str, y_pred_train_str, pos_label='spam')
conf_matrix_train = confusion_matrix(y_train_str, y_pred_train_str)

# Print the evaluation results for the test set
print("Test Set Metrics:")
print(f'Accuracy: {accuracy_test:.2f}')
print(f'Precision: {precision_test:.2f}')
print(f'Recall: {recall_test:.2f}')
print(f'F1 Score: {f1_test:.2f}')
print(f'Confusion Matrix:\n{conf_matrix_test}')

# Print the evaluation results for the training set
print("Training Set Metrics:")
print(f'Accuracy: {accuracy_train:.2f}')
print(f'Precision: {precision_train:.2f}')
print(f'Recall: {recall_train:.2f}')
print(f'F1 Score: {f1_train:.2f}')
print(f'Confusion Matrix:\n{conf_matrix_train}')

# Save the trained model to a file
model_file_path = model_folder / 'best_model.pkl'
with open(model_file_path, 'wb') as file:
    pickle.dump(best_model, file)
print(f"Model saved to {model_file_path}")

# Optionally: Load the model later to make predictions or further evaluation
def load_model(path):
    with open(path, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

# Example of loading the model and making a prediction
loaded_model = load_model(model_file_path)
new_predictions = loaded_model.predict(X_test_transformed)
new_predictions_str = pd.Series(new_predictions).map(reverse_label_mapping)
print("Loaded model predictions:", new_predictions_str[:5].tolist())
