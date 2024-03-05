import csv
import numpy as np
from math import sqrt
from sklearn.neighbors import KNeighborsRegressor
from gen_theoretical import get_dist
from gen_theoretical import dist_to_quality

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
knn_regressor = KNeighborsRegressor(n_neighbors=100)  # You can adjust the number of neighbors (K) as needed
knn_regressor.fit(X_train, y_train)

# Function to predict the position of a new data point
def predict_position(strengths):
    strengths = np.array(strengths).reshape(1, -1)  # Reshape the input into the right format
    return knn_regressor.predict(strengths)

# Example of how to use the predict_position function
err = []
for x in range(0, 101):
    x = x/10;
    for y in range(0, 101):
        y = y/10
        dist = get_dist([x, y])
        Q = dist_to_quality(dist)
        pred = predict_position(Q)
        #curr_err = sqrt((x - pred[0])**2 + (y - pred[1])**2)
        print([x, y])
        print(dist)
        print(Q)
        print(pred)
        break
    break
