#!/bin/python3
import my_lib as ml
import gen_theoretical as gt
import numpy as np
import time

# Here we will generate training data with different sizes and measure the accuracy of the resulting model and the time it takes to solve the system

if __name__ == "__main__":
    mse = []
    times = []
    for n in range(10, 101, 10):
        print(n)
        file_name = f"data_dir/lin{n}.csv"
        gt.gen_data(n, file_name=file_name)
        training_data = ml.load_data(file_name)
        [w, pose] = ml.format_data(training_data)
        # Get optimal matrix for given data
        t1 = time.time() 
        A = ml.get_opt_mat(w, pose)
        t2 = time.time() 
        # Get the MSE for this matrix
        mse.append(ml.MSE(A, w, pose).value/len(w))
        times.append(t2 - t1)
    print(mse)
    print(times)

