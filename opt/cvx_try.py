#!/bin/python3
import numpy as np
import my_lib as ml


# Load the training data
training_data = ml.load_data('small_lin.csv')
[w, x] = ml.format_data(training_data)

[A, B] = ml.get_opt_AB(w, x)
print(A)
print(B)
print(np.linalg.norm(((A @ w[0]) + B) - x[0]))
