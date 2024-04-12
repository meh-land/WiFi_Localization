#!/bin/python3
import gen_theoretical as gt
import my_lib as ml
import numpy as np

# epsilon is just a small number added to weights to make sure we are not dividing by zero
epsilon = 10**-10 

'''
This function takes in a W vector and predicts the position that resulted in it
It takes the weighted sums of the k nearest neighbors
The weights are determined according to the distance between W and W_in (The smaller difference gets higher weight)
'''
def predict_pose(w_in, k=5):
    w_in = np.array(w_in)
    diffs = w - w_in
    diff_norms = np.zeros(len(diffs))
    for i in range(len(diffs)):
        diff_norms[i] = np.linalg.norm(diffs[i])
    # Get indices of the elements with the least diffs
    indices = np.argpartition(diff_norms, k)[:k]
    # Get the scaling factors that will be used in the weighted average
    nearest_norms = diff_norms[indices] + epsilon
    nearest_norms = 1/nearest_norms
    norm_scale = np.sum(nearest_norms)
    weights = nearest_norms/norm_scale
    # Get the positions with the nearest readings
    nearest_points = x[indices]
    # Multiply the positions by the weights
    prediction = nearest_points * weights[:, np.newaxis]
    # Get the weighted sum
    prediction = np.sum(prediction, axis=0)
    print(prediction)

if __name__ == "__main__":
    filename = "knn_smol.csv"
    gt.gen_data(10, file_name=filename)
    td = ml.load_data(filename)
    [w, x] = ml.format_data(td)

    predict_pose([50, 50, 50])

