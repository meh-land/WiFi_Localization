#!/bin/python3
import cvxpy as cp
import numpy as np
import csv

def get_opt_mat(w,x):
    # Define the variables
    A = cp.Variable((2, 3))  # 2x3 matrix
    
    # Define the objective function
    objective = cp.Minimize(cp.sum_squares(A @ w - x))
    
    # Formulate the problem
    problem = cp.Problem(objective)
    
    # Solve the problem
    problem.solve()
    
    # Get the optimal value of A
    optimal_A = A.value
    return optimal_A 

# Load the training data from the CSV file
def load_data(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            data.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])
    return data

# Load the training data
training_data = load_data('small_lin.csv')

W = []
Pose = []

for r in training_data:
    W.append(r[0:3])
    Pose.append(r[3:])

for i in range(len(W)):
    if i == 0:
        my_mat = get_opt_mat(np.array(W[i]), np.array(Pose[i]))
    else:
        my_mat = my_mat + get_opt_mat(np.array(W[i]), np.array(Pose[i]))

my_mat /= len(W)
print(my_mat)
def calc_err(A, w, pose):
    err = []
    for i in range(len(w)):
        curr_w = np.array(w[i])
        curr_pose = np.array(pose[i])
        err.append(cp.sum_squares(np.dot(A,curr_w) - curr_pose))

    return err

avg_err = calc_err(my_mat, W, Pose)
print(avg_err)
