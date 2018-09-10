import numpy as np
import matplotlib.pyplot as plt
import random
import time

def plot_histogram(bins, filename = None):
    assert bins.shape == (200000,4), "Bins must be a numpy array of shape (max_bin_population, num_strategies)"
    assert np.array_equal(np.sum(bins, axis = 0),(np.array([30,30,30,30]))), "30 runs per strategy"

    thresh =  max(np.nonzero(bins)[0])+3
    n_bins = thresh
    bins = bins[:thresh,:]
    
    ind = np.arange(n_bins)
    width = 1.0/6.0

    fig, ax = plt.subplots()
    rects_strat_1 = ax.bar(ind + width, bins[:,0], width, color='yellow')
    rects_strat_2 = ax.bar(ind + width*2, bins[:,1], width, color='orange')
    rects_strat_3 = ax.bar(ind + width*3, bins[:,2], width, color='red')
    rects_strat_4 = ax.bar(ind + width*4, bins[:,3], width, color='k')

    ax.set_ylabel('Number Occurrences in 30 Runs')
    ax.set_xlabel('Number of Balls In The Most Populated Bin')
    ax.set_title('Histogram: Load on Most Populated Bin For Each Strategy')

    ax.set_xticks(ind)
    ax.set_xticks(ind+width*3, minor = True)
    ax.set_xticklabels([str(i+1) for i in range(0,n_bins)], minor = True)
    ax.tick_params(axis=u'x', which=u'minor',length=0)

    ax.legend((rects_strat_1[0], rects_strat_2[0], rects_strat_3[0], rects_strat_4[0]), ('Strategy 1', 'Strategy 2', 'Strategy 3', 'Strategy 4'))
    plt.setp(ax.get_xmajorticklabels(), visible=False)

    if filename is not None: 
        plt.savefig(filename+'.png', bbox_inches='tight')

    plt.show()

number_of_runs = 30
number_of_balls = 200000

# use for strategy 1
def strategy1(number_of_balls, number_of_bins):
    bins_list = []
    for i in range(number_of_bins):
        bins_list.append(0)
    for i in range(number_of_balls):
        bins_list[random.randrange(len(bins_list))] += 1
    return max(bins_list)

# helper func for strategy 2 and strategy 3
# without replacement
def choose_some_bins(bins_list, n_choices):
    set_of_indices = set()
    while len(set_of_indices) < n_choices:
        set_of_indices.add(random.randrange(len(bins_list)))
    return set_of_indices

# helper func for strategy 2 and 3
def helper_func(bins_list, n_choices):
    set_of_indices = choose_some_bins(bins_list, n_choices)
    min_count = min([bins_list[i] for i in set_of_indices])
    # keep bin set_of_indices if that bin has the min number of balls
    set_of_indices = filter(lambda arg: bins_list[arg] == min_count, set_of_indices)
    bins_list[ set_of_indices[random.randrange(len(set_of_indices))] ] += 1

# used for strategy 2 and 3
def strategy2_and_3(number_of_balls, n_bins, n_choices):
    bins_list = [0 for i in range(n_bins)]
    for i in range(number_of_balls):
        helper_func(bins_list, n_choices)
    return max(bins_list)

# use for strategy 4
def strategy4(number_of_balls, n_bins):
    bins_list = []
    for i in range(n_bins):
        bins_list.append(0)
    for i in range(number_of_balls):
        front = random.randrange(len(bins_list)/2)
        back = random.randrange(len(bins_list)/2, len(bins_list))
        if bins_list[front] <= bins_list[back]:
            bins_list[front] += 1
        else:
            bins_list[back] += 1
    return max(bins_list)

n_bins = number_of_balls
simulations_functions = [strategy1, 
    lambda arg1, arg2: strategy2_and_3(arg1, arg2, 2), 
    lambda arg1, arg2: strategy2_and_3(arg1, arg2, 3), 
    strategy4]
x = [[0 for i in range(len(simulations_functions))] for j in range(number_of_balls)]
for i in range(len(simulations_functions)):
    for k in range(number_of_runs):
        maximum_num_of_balls = simulations_functions[i](number_of_balls, n_bins)
        x[maximum_num_of_balls - 1][i] += 1
histo = np.array(x)
plot_histogram(histo)

