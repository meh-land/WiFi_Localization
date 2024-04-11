#!/bin/python3
import cvxpy as cp
import numpy as np
import my_lib as ml


# Load the training data
training_data = ml.load_data('small_lin.csv')
[w, x] = ml.format_data(training_data)

def get_opt_mat(w,x):
    # Define the variables
    A = cp.Variable((2, 3))  # 2x3 matrix
    
    # Define the objective function
    objective = cp.Minimize(ml.MSE(A, w, x))
    
    # Formulate the problem
    problem = cp.Problem(objective)
    
    # Solve the problem
    problem.solve()
    
    # Get the optimal value of A
    optimal_A = A.value
    return optimal_A 


A = get_opt_mat(w, x)
print(A)
