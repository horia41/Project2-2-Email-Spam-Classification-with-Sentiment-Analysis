import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pickle  # Import pickle for saving the model

# Fetch the dataset
path = 'C:\\Users\\lauri\\OneDrive\\Documents\\GitHub\\Project2-2\\spambase\\spambase.data'

column_names = ['feature_' + str(i) for i in range(1, 58)] + ['label']

# Load the data
df = pd.read_csv(path, header=None, names=column_names)

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
