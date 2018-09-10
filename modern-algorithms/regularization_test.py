import numpy as np
import math
import matplotlib.pyplot as plt

def calc_error(X, y, a, n):
    results = X.dot(a)
    results = results.reshape((n))
    y = y.reshape((n))
    numer = np.linalg.norm(results-y)
    denom = np.linalg.norm(y)
    return float(numer) / denom

def plot_bar(lambda_val, test_errors_list, train_errors_list):
    fig, ax = plt.subplots()
    index = np.arange(len(lambda_val))
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, train_errors_list, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Train')

    rects2 = plt.bar(index + bar_width, test_errors_list, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Test')

    plt.xlabel('Lambdas')
    plt.ylabel('Errors')
    plt.title('Test and Train Errors vs Lambdas')
    plt.xticks(index + bar_width, lambda_val)
    legend = ax.legend(loc = 'upper left')
    plt.tight_layout()
    plt.savefig('2b' + '.png', bbox_inches='tight')

n_trials = 10
lambda_val = [0.0005, 0.005, 0.05, 0.5, 5, 50, 500]
test_errors_list = []
train_errors_list = []
train_n = 100
test_n = 1000
d = 100

for lambda_current in lambda_val:
    total_test_error = 0
    total_train_error = 0
    for trial in range(n_trials):
        X_train = np.random.normal(0,1, size=(train_n, d))
        a_true = np.random.normal(0,1, size=(d, 1))
        y_train = X_train.dot(a_true) + np.random.normal(0, 0.5, size=(train_n, 1))
        X_test = np.random.normal(0, 1, size=(test_n, d))
        y_test = X_test.dot(a_true) + np.random.normal(0, 0.5, size=(test_n, 1))

        X_mat_T = np.mat(X_train).T
        a_vector_computed = np.linalg.inv(X_mat_T.dot(X_train) + \
            lambda_current * np.eye(d)  \
            ).dot(X_mat_T).dot(y_train)

        total_test_error += calc_error(X_test, y_test, \
            a_vector_computed, test_n)
        total_train_error += calc_error(X_train, y_train, \
            a_vector_computed, train_n)

    average_test = total_test_error / n_trials
    average_train = total_train_error / n_trials
    print "Current: "
    print lambda_current
    print average_test
    print average_train
    test_errors_list.append(average_test)
    train_errors_list.append(average_train)

plot_bar(lambda_val, test_errors_list, train_errors_list)
