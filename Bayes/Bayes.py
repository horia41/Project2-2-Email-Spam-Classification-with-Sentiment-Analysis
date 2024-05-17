import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pickle
import os

# Fetch the dataset
# path = 'D:\\project 2-2\\spambase\\spambase.data'
# 'C:\\Users\\mespi\\OneDrive\\Escritorio\\Project2.2\\spambase\\spambase.data'
# 'C:\\Users\\lauri\\OneDrive\\Documents\\GitHub\\Project2-2\\spambase\\spambase.data'

relative_path = os.path.join('..', 'spambase', 'spambase.data')
# esti chiar handicapat dan

column_names = ['feature_' + str(i) for i in range(1, 58)] + ['label']

# Load the data
df = pd.read_csv(relative_path, header=None, names=column_names)

# Split the data into features and target variable
X = df.drop('label', axis=1)
y = df['label']

# Split the dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the Naive Bayes classifier
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# Make predictions
y_pred = nb_classifier.predict(X_test)
y_pred_train = nb_classifier.predict(X_train)

# Calculate metrics for the test set,and training set , including accuracy, precision, recall, F1 score, and confusion matrix
accuracy_test = accuracy_score(y_test, y_pred)
precision_test = precision_score(y_test, y_pred)
recall_test = recall_score(y_test, y_pred)
f1_test = f1_score(y_test, y_pred)
conf_matrix_test = confusion_matrix(y_test, y_pred)

accuracy_train = accuracy_score(y_train, y_pred_train)
precision_train = precision_score(y_train, y_pred_train)
recall_train = recall_score(y_train, y_pred_train)
f1_train = f1_score(y_train, y_pred_train)
conf_matrix_train = confusion_matrix(y_train, y_pred_train)

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
model_file_path = 'naive_bayes_model.pkl'
with open(model_file_path, 'wb') as file:
    pickle.dump(nb_classifier, file)
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
