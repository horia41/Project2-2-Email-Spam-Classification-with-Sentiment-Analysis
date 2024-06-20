import matplotlib.pyplot as plt
import numpy as np

# Datasets
datasets = ['Spambase', 'Enron Spam', 'Third Dataset', 'SMS Spam', 'Fifth Dataset']

# Naive Bayes Metrics
nb_accuracy = [0.82, 0.28, 0.68, 0.23, 0.23]
nb_precision = [0.70, 0.18, 0.63, 0.14, 0.14]
nb_recall = [0.95, 0.94, 0.91, 0.88, 0.89]
nb_f1_score = [0.80, 0.30, 0.75, 0.23, 0.24]

# SVM Metrics
svm_accuracy = [0.93, 0.88, 0.66, 0.84, 0.84]
svm_precision = [0.93, 0.62, 0.76, 0.41, 0.42]
svm_recall = [0.90, 0.64, 0.48, 0.45, 0.45]
svm_f1_score = [0.91, 0.63, 0.59, 0.43, 0.43]

# Plot Accuracy Comparison
plt.figure(figsize=(10, 6))
plt.plot(datasets, nb_accuracy, marker='o', label='Naive Bayes')
plt.plot(datasets, svm_accuracy, marker='o', label='SVM')
plt.xlabel('Datasets')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison Between Naive Bayes and SVM')
plt.legend()
plt.grid(True)
plt.show()

# Plot Precision Comparison
plt.figure(figsize=(10, 6))
plt.plot(datasets, nb_precision, marker='o', label='Naive Bayes')
plt.plot(datasets, svm_precision, marker='o', label='SVM')
plt.xlabel('Datasets')
plt.ylabel('Precision')
plt.title('Precision Comparison Between Naive Bayes and SVM')
plt.legend()
plt.grid(True)
plt.show()

# Plot Recall Comparison
plt.figure(figsize=(10, 6))
plt.plot(datasets, nb_recall, marker='o', label='Naive Bayes')
plt.plot(datasets, svm_recall, marker='o', label='SVM')
plt.xlabel('Datasets')
plt.ylabel('Recall')
plt.title('Recall Comparison Between Naive Bayes and SVM')
plt.legend()
plt.grid(True)
plt.show()

# Plot F1 Score Comparison
plt.figure(figsize=(10, 6))
plt.plot(datasets, nb_f1_score, marker='o', label='Naive Bayes')
plt.plot(datasets, svm_f1_score, marker='o', label='SVM')
plt.xlabel('Datasets')
plt.ylabel('F1 Score')
plt.title('F1 Score Comparison Between Naive Bayes and SVM')
plt.legend()
plt.grid(True)
plt.show()
