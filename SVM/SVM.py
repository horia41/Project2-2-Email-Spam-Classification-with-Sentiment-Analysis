import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pickle
from pathlib import Path

# Fetch the dataset
data_folder = Path(__file__).resolve().parent.parent / 'spambase'
data_file = data_folder / 'spambase.data'

column_names = ['feature_' + str(i) for i in range(1, 58)] + ['label']

df = pd.read_csv(data_file, header=None, names=column_names)

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
y_pred_train = classifier.predict(X_train)


# Calculate metrics for the test set and training set, including accuracy, precision, recall, F1 score, and confusion matrix
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

accuracy_train = accuracy_score(y_train, y_pred_train)
precision_train = precision_score(y_train, y_pred_train)
recall_train = recall_score(y_train, y_pred_train)
f1_train = f1_score(y_train, y_pred_train)
conf_matrix_train = confusion_matrix(y_train, y_pred_train)


# Print the evaluation results for the test set
print("Test Set Metrics:")
print(f'Accuracy : {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'Confusion Matrix:\n{conf_matrix}')


# Print the evaluation results for the training set
print("Training Set Metrics:")
print(f'Accuracy: {accuracy_train:.2f}')
print(f'Precision: {precision_train:.2f}')
print(f'Recall: {recall_train:.2f}')
print(f'F1 Score: {f1_train:.2f}')
print(f'Confusion Matrix:\n{conf_matrix_train}')

# Save the trained model to a file
model_file_path = 'SVM_model.pkl'
with open(model_file_path, 'wb') as file:
    pickle.dump(classifier, file)
print(f"Model saved to {model_file_path}")

# Optionally: Load the model later to make predictions or further evaluation
def load_model(path):
    with open(path, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model


# Example of loading the model and making a prediction
loaded_model = load_model(model_file_path)
new_predictions = loaded_model.predict(X_test)
print("Loaded model predictions:", new_predictions[:5])
