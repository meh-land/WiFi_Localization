from math import sqrt
from math import ceil
ap1_loc = [0, 0]
ap2_loc = [0, 10]
ap3_loc = [10, 0]


def get_dist(torta_loc):
    d1 = sqrt((torta_loc[0] - ap1_loc[0])**2 + (torta_loc[1] - ap1_loc[1])**2)
    d2 = sqrt((torta_loc[0] - ap2_loc[0])**2 + (torta_loc[1] - ap2_loc[1])**2)
    d3 = sqrt((torta_loc[0] - ap3_loc[0])**2 + (torta_loc[1] - ap3_loc[1])**2)
    return [d1, d2, d3]

def dist_to_quality(dists):
    Q = dists
    for i in range(len(dists)):
        Q[i] = ceil(-9.9*dists[i] + 100)
    return Q

print(dist_to_quality([0, 10, 5]))
