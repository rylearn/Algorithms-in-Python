import csv
import numpy as np

# uses random.choice to select k people at random, sort, then
# call conductance
def rand_conductance(k, A):
    n_people = A.shape[0]
    all_people = np.sort(np.random.choice(n_people, k, replace = False))
    return conductance(all_people, A)

# given a set of people, finds the conductance
def conductance(people, A):
    in_group_friendships = 0
    for (x, y) in [(a, b) for a in people for b in people]:
        if x < y:
            in_group_friendships += A[x][y]
    total_friendships = 0
    for x in people:
        total_friendships += A[x].sum()
    return float(in_group_friendships)/total_friendships

# given the input data file, constructs the adjacency matrix A
def read_A(n_friends):
    f_name = "data.csv"
    friends_mat = np.zeros(shape =(n_friends, n_friends), dtype=np.int16)
    with open(f_name, 'r') as csvfile:
        friend_reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for friendship in friend_reader:
            person = int(friendship[0])
            friend = int(friendship[1])
            # check to make sure assumption about number of people was correct
            if person > 1495 or friend > 1495:
                print "too many friends"
                return
            else:
                friends_mat[person-1][friend-1] = 1
    for x in range(all_friends.shape[0]):
        friends_mat[x][x] = friends_mat[x].sum()
    return friends_mat

A = read_A(1495)
print rand_conductance(150, A)
