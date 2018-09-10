import numpy as np
import matplotlib.pyplot as plt
import random

iterations = 1000
def stochastic_gradient_descent(X_matrix, y, alpha):
    d = len(X_matrix[0])
    n = len(X_matrix)
    a_curr = np.zeros(d)
    errors = []

    indices = range(n)
    random.shuffle(indices)

    for i in range(iterations):
        j = indices[i] % n
        e = X_matrix[j].dot(a_curr) - y[j]
        a_curr = a_curr - 2*alpha*X_matrix[j]*e
        if i % 10 == 0:
            errors.append(squared_error(X_matrix, y, a_curr.T))

    sum_sq = squared_error(X_matrix, y, a_curr.T)
    print "Via grad descent and alpha = " + \
        str(alpha) + ": " + str(sum_sq)

    return errors

# Returns the optimal vector a for a given data set
def find_a_vector(X_matrix, y):
    gramMatrix = X_matrix.T.dot(X_matrix)
    a_vector = np.linalg.inv(gramMatrix).dot(X_matrix.T).dot(y)
    return a_vector

def squared_error(X_matrix, y, a):
    sum_squared = 0
    for i in range(len(y)):
        sum_squared += (a.dot(X_matrix[i]) - y[i])**2
    return sum_squared[0]

def plot(x_vals, y_vals, x_label, y_label, alphas, true_sum_sq):
    fig, ax = plt.subplots()
    symbols = ['b--', 'r--','g--']
    for i in range(3):
        ax.plot(x_vals, y_vals[i], symbols[i], label = "alpha: " + str(alphas[i]))

    ref_x = np.arange(1.0, float(iterations), 0.1)
    ref_y = [true_sum_sq for i in range(len(ref_x))]
    ax.plot(ref_x, ref_y, 'k', label="optimal value")

    legend = ax.legend(loc = 'lower left')
    plt.yscale('symlog')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig('1c' + '.png', bbox_inches='tight')

d = 100 # dimensions of data
n = 1000 # number of data points
X_matrix = np.random.normal(0, 1, size=(n, d))
a_true = np.random.normal(0, 1, size=(d, 1))
y = X_matrix.dot(a_true) + np.random.normal(0, 0.5, size=(n,1))

a_calc = find_a_vector(X_matrix, y)
a_t = a_calc.T
true_sum_sq = squared_error(X_matrix, y, a_t)
true_sum_sq = true_sum_sq
print "true: ", true_sum_sq

alphas = [0.0005, 0.005, 0.01]

all_errors = []
a_zeros = np.zeros(d)
for alpha in alphas:
    errors_list = stochastic_gradient_descent(X_matrix, y, alpha)
    all_errors.append([squared_error(X_matrix, y, a_zeros.T)] + errors_list)

x_vals = range(0, iterations + 1, 10)
y_vals = all_errors
plot(x_vals, y_vals, "Number of iterations",  \
   "Value of objective function", alphas, true_sum_sq)
