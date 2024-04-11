#!/bin/python3
import csv
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

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

MSE = np.zeros((10, 10, 10, 10, 10, 10))
MSE += 10**6

def get_opt_mat(mat_start):
    for a11 in range(mat_start, mat_start+10):
        for a12 in range(mat_start, mat_start+10):
            for a13 in range(mat_start, mat_start+10):
                for a21 in range(mat_start, mat_start+10):
                    for a22 in range(mat_start, mat_start+10):
                        for a23 in range(mat_start, mat_start+10):
                            mse = 0
                            for i in range(len(W)):
                                curr_w = np.array(W[i])
                                curr_pose = np.array(Pose[i])
                                mat = np.array([[a11, a12, a13], [a21, a22, a23]])
                                est_pose = np.dot(mat ,curr_w)
                                mse += (est_pose[0] - curr_pose[0])**2 + (est_pose[1] - curr_pose[1])**2 
                            mse /= len(W)
                            MSE[a11-mat_start, a12-mat_start, a13-mat_start, a21-mat_start, a22-mat_start, a23-mat_start] = mse

    # Get the least element in the array
    opt_mat = np.argmin(MSE)
    min_index_multi = np.unravel_index(opt_mat, MSE.shape)
    return [min_index_multi, MSE[min_index_multi]]
        
min_res = [10**6, 10**6]
for st in range(1, 100, 10):
    curr_res = get_opt_mat(st)
    if curr_res[1] < min_res[1]:
        min_res = curr_res
        print(min_res, st)
