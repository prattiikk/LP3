# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Load dataset and drop unnecessary column
data = pd.read_csv("emails.csv")
data = data.drop('Email No.', axis=1)

# Separate features (X) and target (y)
X = data.drop('Prediction', axis=1)
y = data['Prediction']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Initialize and train KNN classifier
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)

# Make predictions with KNN
y_pred_knn = knn.predict(X_test)

# Print KNN evaluation metrics
print("KNN Classifier Metrics:")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Precision:", precision_score(y_test, y_pred_knn))
print("Recall:", recall_score(y_test, y_pred_knn))
print("Classification Report:\n", classification_report(y_test, y_pred_knn))

# Display KNN Confusion Matrix
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_knn)).plot()
plt.title("KNN Confusion Matrix")
plt.show()

# Initialize and train SVM classifier
svm = SVC(gamma='auto')
svm.fit(X_train, y_train)

# Make predictions with SVM
y_pred_svm = svm.predict(X_test)

# Print SVM evaluation metrics
print("SVM Classifier Metrics:")
print("Accuracy:", accuracy_score(y_test, y_pred_svm))
print("Precision:", precision_score(y_test, y_pred_svm))
print("Recall:", recall_score(y_test, y_pred_svm))
print("Classification Report:\n", classification_report(y_test, y_pred_svm))

# Display SVM Confusion Matrix
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred_svm)).plot()
plt.title("SVM Confusion Matrix")
plt.show()