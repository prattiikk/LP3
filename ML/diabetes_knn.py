# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('diabetes.csv')

# Handle missing values by replacing zeros in certain columns with the column mean
columns_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']
for col in columns_to_fix:
    data[col] = data[col].replace(0, np.NaN)  # Replace 0 with NaN
    mean_value = data[col].mean(skipna=True)
    # data[col].fillna(mean_value, inplace=True)  # Fill NaN with mean of the column
    data[col] = data[col].replace(np.NaN, mean_value)  # Replace NaN with the mean valueF


# Split features (X) and target variable (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]



# Display correlation heatmap
# sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")
# plt.show()

print(data.corr())


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Standardize the data to improve model performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train) 
X_test = scaler.transform(X_test)


# Elbow method to choose the optimal number of neighbors
error_rate = []

# Loop over different values of n_neighbors
for i in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    error_rate.append(np.mean(y_pred != y_test))  # Calculate error rate


# Plotting the elbow plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, 21), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. Number of Neighbors (K)', fontsize=14)
plt.xlabel('Number of Neighbors (K)', fontsize=12)
plt.ylabel('Error Rate', fontsize=12)
plt.xticks(range(1, 21))  # Show all x-ticks from 1 to 20
plt.grid(True)
plt.show()

# From the elbow plot, choose an optimal value for n_neighbors (e.g., 11)
optimal_k = 11  # You can change this based on the elbow plot

# Train the K-Nearest Neighbors (KNN) classifier with the chosen n_neighbors
knn = KNeighborsClassifier(n_neighbors=optimal_k, metric='euclidean')
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Calculate and print the confusion matrix and performance metrics
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Plot the confusion matrix for better visualization
sns.heatmap(pd.DataFrame(conf_matrix), annot=True, cmap="YlGnBu", fmt='g')
plt.title('Confusion Matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.show()

# Display model performance metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

# Display the classification report
report = classification_report(y_test, y_pred, target_names=['Non-Diabetic', 'Diabetic'])
print("Classification Report:\n", report)