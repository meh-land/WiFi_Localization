from math import sqrt
from math import ceil
import csv

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
        if Q[i] < 0:
            Q[i] = 0
        if Q[i] > 100:
            Q[i] = 100
    return Q

# iterate over x and y to get the corresponding quality
rows= []
for x in range(0, 1001):
    x = x/100
    for y in range(0, 1001):
        y = y/100
        dists = get_dist([x, y])
        Q = dist_to_quality(dists)
        row = {'OurESP1': Q[0],
               'OurESP2': Q[1],
               'OurESP3': Q[2],
               'x': x,
               'y': y
               }
        rows.append(row)

# write rows in a csv file
file_name = 'linear.csv'
with open(file_name, 'w', newline='') as csvfile:
    fieldnames = ['OurESP1', 'OurESP2', 'OurESP3', 'x', 'y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for r in rows:
        writer.writerow(r)


