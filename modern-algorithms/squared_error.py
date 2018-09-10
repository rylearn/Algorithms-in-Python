import numpy as np

def squared_error(X, y, a_t):
    sum_squared = 0
    for i in range(len(y)):
        sum_squared += (a_t.dot(X[i]) - y[i])**2
    return sum_squared

d = 100 # dimensions of data
n = 1000 # number of data points
X = np.random.normal(0,1, size=(n,d))
a_true = np.random.normal(0,1, size=(d,1))
y = X.dot(a_true) + np.random.normal(0,0.5,size=(n,1))
a_calc = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

print "closed form solution: ", squared_error(X, y, a_calc.T)[0]
a_t = np.zeros(d)
print "z = 0 vector: ", squared_error(X, y, a_t.T)[0]