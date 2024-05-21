import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from pathlib import Path
import warnings

# Suppress warnings related to feature names
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

# Function to load the pre-trained Naive Bayes model
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


# Fetch the dataset
data_folder = Path(__file__).resolve().parent.parent / 'spambase'
data_file = data_folder / 'transformed_enron_spam_data.data'

# load saved model
model_folder = Path(__file__).resolve().parent.parent / 'SVM'
model_file = model_folder / 'SVM_model.pkl'

# Column names for the dataset
column_names = ['feature_' + str(i) for i in range(1, 58)] + ['label']

# Load the data
df = pd.read_csv(data_file, header=None, names=column_names)

# Split the data into features and target variable
X = df.drop('label', axis=1)
y = df['label']

# Load the pre-trained model
model = load_model(model_file)

# Make predictions
y_pred = model.predict(X)

# Calculate metrics for the dataset
accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)
recall = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)
conf_matrix = confusion_matrix(y, y_pred)

# Print the evaluation results
print("Evaluation Metrics for the Entire Dataset:")
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'Confusion Matrix:\n{conf_matrix}')
