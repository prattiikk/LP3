# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Load the dataset
data = pd.read_csv('Churn_Modelling.csv')  # Load the customer churn dataset

# Step 2: Preprocess the Data
# Drop unnecessary columns
data = data.drop(['RowNumber', 'CustomerId', 'Surname', 'Geography', 'Gender'], axis=1)

# Separate features and target variable
X = data.drop('Exited', axis=1)  # Features
y = data['Exited']               # Target variable

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Define and compile the neural network model
model = Sequential([
    Dense(16, input_dim=X_train.shape[1], activation='relu', kernel_initializer='uniform'),
    Dense(8, activation='relu', kernel_initializer='uniform'),
    Dense(1, activation='sigmoid', kernel_initializer='uniform')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2, verbose=1)

# Step 6: Evaluate the model on the test set
y_pred = (model.predict(X_test) > 0.5).astype("int32")  # Predict and apply threshold

# Calculate and print accuracy and confusion matrix
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy Score: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)

# Print detailed classification report
print(classification_report(y_test, y_pred))