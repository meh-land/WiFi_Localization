import csv
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Load the training data from the CSV file
def load_data(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            data.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])
    return np.array(data)

# Load the training data
training_data = load_data('random_data.csv')

# Separate features (strength of wifi signals) and labels (x, y coordinates)
X_train = training_data[:, :3]  # Features (strength of wifi signals)
y_train = training_data[:, 3:]  # Labels (x, y coordinates)

# Initialize and train the KNN regressor
knn_regressor = KNeighborsRegressor(n_neighbors=5)  # You can adjust the number of neighbors (K) as needed
knn_regressor.fit(X_train, y_train)

# Function to predict the position of a new data point
def predict_position(strengths):
    strengths = np.array(strengths).reshape(1, -1)  # Reshape the input into the right format
    return knn_regressor.predict(strengths)

# Example of how to use the predict_position function
new_data_point = [70, 80, 90]  # Strengths of wifi signals for the new data point
predicted_position = predict_position(new_data_point)
print("Predicted position:", predicted_position)
