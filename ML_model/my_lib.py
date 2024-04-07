#!/bin/python3
import cvxpy as cp
import numpy as np
import csv

# Load the training data from the CSV file
def load_data(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            data.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])
    return data

def format_data(training_data):
    W = []
    Pose = []
    
    for r in training_data:
        W.append(r[0:3])
        Pose.append(r[3:])
    return [np.array(W), np.array(Pose)]

def MSE(A, w, x):
    #Get data length (dl)
    dl = len(w)

    mse = 0
    for i in range(dl):
        curr_pose = x[i]
        predicted_pose = A @ w[i]
        pose_diff = curr_pose - predicted_pose
        mse += pose_diff[0]**2 + pose_diff[1]**2
    return np.sqrt(mse) / dl
