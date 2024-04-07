#!/bin/python3
import cvxpy as cp
import numpy as np

# Predetermined values
w = np.array([[1], [2], [3]])  # 3x1 vector
x = np.array([[4], [5]])       # 2x1 vector

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

print("Optimal A:")
print(optimal_A)
print(np.dot(optimal_A, w))
print(optimal_A+optimal_A)
