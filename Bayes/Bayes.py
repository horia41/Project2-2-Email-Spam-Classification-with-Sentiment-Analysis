import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.feature_selection import SelectKBest, f_classif
from imblearn.over_sampling import SMOTE
import pickle

# Fetch the dataset
path = r'C:\Users\Dan Loznean\Documents\GitHub\Project2-2\spambase\spambase.data'
column_names = ['feature_' + str(i) for i in range(1, 58)] + ['label']

# Load the data
df = pd.read_csv(path, header=None, names=column_names)

# Split the data into features and target variable
X = df.drop('label', axis=1)
y = df['label']

# Apply SMOTE to balance the classes
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Split the dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.3, random_state=42)

# Feature selection
selector = SelectKBest(score_func=f_classif, k=20)  # Selecting top 20 features
X_train = selector.fit_transform(X_train, y_train)
X_test = selector.transform(X_test)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the Naive Bayes classifier
nb_classifier = GaussianNB()

# Hyperparameter tuning using GridSearchCV
param_grid = {'var_smoothing': [1e-9, 1e-8, 1e-7, 1e-6, 1e-5]}
cv = StratifiedKFold(n_splits=5)
grid_search = GridSearchCV(estimator=nb_classifier, param_grid=param_grid, cv=cv, scoring='f1')
grid_search.fit(X_train, y_train)

# Train the best estimator found by GridSearchCV
best_nb_classifier = grid_search.best_estimator_
best_nb_classifier.fit(X_train, y_train)

# Make predictions
y_pred = best_nb_classifier.predict(X_test)
y_pred_train = best_nb_classifier.predict(X_train)

# Calculate metrics for the test set and training set, including accuracy, precision, recall, F1 score, and confusion matrix
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

# Save the trained model, feature selector, and scaler to a file
model_file_path = 'naive_bayes_model.pkl'
with open(model_file_path, 'wb') as file:
    pickle.dump((best_nb_classifier, selector, scaler), file)
print(f"Model saved to {model_file_path}")
