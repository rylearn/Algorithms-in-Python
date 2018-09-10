import numpy as np
import matplotlib.pyplot as plt

iterations = 20
def gradient_descent(X_matrix, y, alpha):
    dims = len(X_matrix[0])
    num_points = len(X_matrix)
    a_curr = np.zeros(dims)
    errors_list = []
    for num_iterations in range(iterations):
        a_summation = np.zeros(dims)
        for j in range(num_points):
            e = X_matrix[j].dot(a_curr) - y[j]
            a_summation += X_matrix[j]*e
        a_curr = a_curr - 2 * alpha * a_summation

        errors_list.append(squared_error(X_matrix, y, a_curr.T))

    sum_sq = squared_error(X_matrix, y, a_curr.T)
    print "Via grad descent and alpha = " + \
        str(alpha) + ": " + str(sum_sq)

    return errors_list

def find_a_vector(X_matrix, y):
    gramMatrix = np.mat(X_matrix.T.dot(X_matrix))
    a_vector = np.linalg.inv(gramMatrix).dot(X_matrix.T).dot(y)
    return a_vector

def squared_error(X_matrix, y, a_t):
    sum_squared = 0
    for i in range(len(y)):
        sum_squared += (a_t.dot(X_matrix[i]) - y[i])**2
    return sum_squared[0]

def plot(x_vals, y_vals, x_label, y_label, 
    alpha_values, true_sum_sq):

    fig, ax = plt.subplots()
    symbols = ['b--', 'rs','g^']
    for i in range(len(y_vals)):
        ax.plot(x_vals, y_vals[i], symbols[i], 
            label = "alpha: "+str(alpha_values[i]))
    ref_x = np.arange(0.0, float(iterations), 0.1)
    ref_y = [true_sum_sq for i in range(len(ref_x))]
    ax.plot(ref_x,ref_y,'k',label="optimal value")

    legend = ax.legend(loc = 'upper left')
    plt.yscale('symlog')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig('1b' + '.png', bbox_inches='tight')


dims = 100          # dimensions of data
num_points = 1000   # number of data points
X_matrix = np.random.normal(0, 1, size=(num_points,dims))
a_true = np.random.normal(0, 1, size=(dims,1))
y = X_matrix.dot(a_true) + np.random.normal(0,0.5,size=(num_points,1))

a_calc = find_a_vector(X_matrix, y)
a_t = a_calc.T
true_sum_sq = squared_error(X_matrix, y, a_t)
true_sum_sq = true_sum_sq[0, 0]
print "true minimum: ", true_sum_sq

alpha_values = [0.00005, 0.0005, 0.0007]

all_errors = []
a_zeros = np.zeros(dims)
for alpha in alpha_values:
    errors_list = gradient_descent(X_matrix, y, alpha)
    all_errors.append([squared_error(X_matrix, \
        y, a_zeros.T)] + errors_list)

x_vals = range(0, iterations + 1)
y_vals = all_errors
plot(x_vals, y_vals, "Iterations",  \
   "Loss", alpha_values, true_sum_sq)
