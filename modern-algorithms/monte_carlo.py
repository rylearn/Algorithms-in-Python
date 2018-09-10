
import numpy as np
import random
import csv
import math
import copy
import matplotlib.pyplot as plt
from copy import deepcopy

def import_elems():
	elems_list = []
	with open('elems.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter = ',')
		count = 0
		for row in spamreader:
			if count != 0:
				elems_list.append((row[0], float(row[1]), float(row[2])))
			count += 1

	return elems_list

def distance_calc(first_coord, second_coord):
	(name1, long1, lat1) = first_coord
	(name2, long2, lat2) = second_coord
	return np.sqrt((long1-long2)**2 + (lat1-lat2)**2)

def distance_total(route):
	N = len(route)
	tot_dist = 0
	for i in range(N):
		tot_dist += distance_calc(route[i], route[(i+1)%N])
	return tot_dist

def swap(lst, a, b):
	temp = lst[a]
	lst[a] = lst[b]
	lst[b] = temp

def swap_elems_parta(route):
	indices = range(len(route))
	swap_start = random.sample(indices,1)[0] # uniformly select, swap with right neighbor
	index1 = swap_start
	index2 = (swap_start + 1) % len(route) #  wrap around to first 
	swap(route, index1, index2)
	return index1, index2

def swap_elems_partb(route):
	indices = range(len(route))
	index1, index2 = random.sample(indices, 2)
	swap(route, index1, index2)
	return index1, index2

def monte_carlo_markov_chain(route, MAXITER, T):
	random.shuffle(route)
	best = copy.deepcopy(route)
	x = []
	y = []
	for i in range(MAXITER):
		# swap two random successive elems
		current_route_distance = distance_total(route)
		a, b = swap_elems_partb(route)
		# print route
		# print new_route
		delta = distance_total(route) - current_route_distance
		if not (delta < 0 or \
			(T > 0 and \
				random.random() < math.exp(-delta/float(T))
				) ):
			swap(route,a,b) # swap back elems that were changed
		if distance_total(route) < distance_total(best):
			best = deepcopy(route)
		x.append(i)
		y.append(distance_total(route))
	return best, x, y

def run_trials(num_trials, T):
	route = import_elems()
	MAXITER = 10000
	for T in [0, 1, 10, 100]:
		if T != 0:
			plt.close()
		for i in range(num_trials):
			best, x, y = monte_carlo_markov_chain(route, MAXITER, T)
			plt.plot(x, y)
		plt.savefig("t_" + str(T) + "_plotb.png")

run_trials(10, 0)

