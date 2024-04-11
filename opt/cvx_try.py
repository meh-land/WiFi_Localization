#!/bin/python3
import numpy as np
import my_lib as ml


# Load the training data
training_data = ml.load_data('data_dir/lin100.csv')
[w, x] = ml.format_data(training_data)

[A, B] = ml.get_opt_AB(w, x)
print(f"A = {A}")
print(f"B = {B}")
[mse, std_dev] = ml.err_stats(A, B, w, x)
print(f"Avg Err = {mse}")
print(f"Std Dev = {std_dev}")
