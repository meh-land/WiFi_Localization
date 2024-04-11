#!/bin/python3
from math import sqrt
from math import ceil
import csv
import numpy as np



def get_dist(torta_loc, l=10):
    ap1_loc = [0, 0]
    ap2_loc = [0, l]
    ap3_loc = [l, 0]
    d1 = sqrt((torta_loc[0] - ap1_loc[0])**2 + (torta_loc[1] - ap1_loc[1])**2)
    d2 = sqrt((torta_loc[0] - ap2_loc[0])**2 + (torta_loc[1] - ap2_loc[1])**2)
    d3 = sqrt((torta_loc[0] - ap3_loc[0])**2 + (torta_loc[1] - ap3_loc[1])**2)
    return [d1, d2, d3]

def dist_to_quality(dists, l=10):
	Q = dists
	for i in range(len(dists)):
		Q[i] = ceil((-99/l)*dists[i] + 100)
		if Q[i] < 0:
		    Q[i] = 0
		if Q[i] > 100:
		    Q[i] = 100
	return Q

def gen_data(N, file_name='linear.csv', l=10):
	# iterate over x and y to get the corresponding quality
	rows= []
	for x in np.linspace(0, l, N):
		for y in np.linspace(0, l, N):
		    dists = get_dist([x, y], l)
		    Q = dist_to_quality(dists)
		    row = {'OurESP1': Q[0],
			   'OurESP2': Q[1],
			   'OurESP3': Q[2],
			   'x': x,
			   'y': y
			 }
		    rows.append(row)

	# write rows in a csv file
	with open(file_name, 'w', newline='') as csvfile:
		fieldnames = ['OurESP1', 'OurESP2', 'OurESP3', 'x', 'y']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for r in rows:
		    writer.writerow(r)


