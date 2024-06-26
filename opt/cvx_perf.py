#!/bin/python3
import my_lib as ml
import gen_theoretical as gt
import numpy as np
import time
import matplotlib.pyplot as plt

# Here we will generate training data with different sizes and measure the accuracy of the resulting model and the time it takes to solve the system

def data_size_perf():
    mse = []
    times = []
    n_range = np.arange(10, 101, 10)
    for n in n_range:
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
    
    # Plot the results
    # MSE
    plt.plot(n_range, mse, color='blue', label='MSE')

    # Time
    plt.plot(n_range, times, color='red', label='Time')

    # Adding labels and title
    plt.xlabel('N')
    plt.title('MSE and Time vs N')

    # Adding legend
    plt.legend()

    # Display the plot
    plt.show()

def data_size_perf_AB():
    mse = []
    times = []
    n_range = np.arange(10, 101, 10)
    for n in n_range:
        print(n)
        file_name = f"data_dir/lin{n}_AB.csv"
        gt.gen_data(n, file_name=file_name)
        training_data = ml.load_data(file_name)
        [w, pose] = ml.format_data(training_data)
        # Get optimal matrix for given data
        t1 = time.time() 
        [A, B] = ml.get_opt_AB(w, pose)
        t2 = time.time() 
        # Get the MSE for this matrix
        mse.append(ml.MSE(A, B, w, pose).value/len(w))
        times.append(t2 - t1)
    
    # Plot the results
    # MSE
    plt.plot(n_range, mse, color='blue', label='MSE')

    # Time
    # plt.plot(n_range, times, color='red', label='Time')

    # Adding labels and title
    plt.xlabel('N')
    plt.title('MSE vs N')

    # Adding legend
    # plt.legend()

    # Display the plot
    plt.show()


def room_size_perf():
    mse = []
    times = []
    n = 50
    l_range = np.arange(10, 101, 10)
    for l in l_range:
        print(l)
        file_name = f"data_dir/room{l}.csv"
        gt.gen_data(l, file_name=file_name, l=l)
        training_data = ml.load_data(file_name)
        [w, pose] = ml.format_data(training_data)
        # Get optimal matrix for given data
        t1 = time.time() 
        A = ml.get_opt_mat(w, pose)
        t2 = time.time() 
        # Get the MSE for this matrix
        mse.append(ml.MSE(A, w, pose).value/(len(w)*l))
        times.append(t2 - t1)
    
    # Plot the results
    # MSE
    plt.plot(l_range, mse, color='blue', label='MSE')

    # Time
    plt.plot(l_range, times, color='red', label='Time')

    # Adding labels and title
    plt.xlabel('N')
    plt.title('MSE and Time vs N')

    # Adding legend
    plt.legend()

    # Display the plot
    plt.show()


if __name__ == "__main__":
    data_size_perf_AB()
