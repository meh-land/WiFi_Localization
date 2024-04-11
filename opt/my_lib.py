#!/bin/python3
import cvxpy as cp
import numpy as np
import csv
import matplotlib.pyplot as plt
# from math import sqrt

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
        mse += cp.norm(pose_diff)
    return mse

def get_opt_mat(w,x):
    # Define the variables
    A = cp.Variable((2, 3))  # 2x3 matrix
    
    # Define the objective function
    objective = cp.Minimize(MSE(A, w, x))
    
    # Formulate the problem
    problem = cp.Problem(objective)
    
    # Solve the problem
    problem.solve()
    
    # Get the optimal value of A
    return A.value 

def plot(x, y, xlabel="X", ylablel="Y", title="X vs Y"):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
