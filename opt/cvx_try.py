#!/bin/python3
import numpy as np
import my_lib as ml


# Load the training data
training_data = ml.load_data('small_lin.csv')
[w, x] = ml.format_data(training_data)

A = ml.get_opt_mat(w, x)
print(A)
print(np.linalg.norm((A @ w[0]) - x[0]))
