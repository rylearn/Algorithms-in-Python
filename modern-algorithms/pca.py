from numpy.random import randn
import numpy as np
from sklearn.decomposition import PCA
import math
import matplotlib.pyplot as plt

def normalize(x, y):
    x_mat = np.mat(x)
    av_x = x_mat.sum()/x_mat.shape[1]
    norm_x = x_mat - av_x

    y_mat = np.mat(y)
    av_y = y_mat.sum()/y_mat.shape[1]
    norm_y = y_mat - av_y
    return (norm_x, norm_y)

def ls_recover(x, y):
    (norm_x, norm_y) = normalize(x,y)
    a_vec = norm_x.dot(norm_y.T)/(norm_x.dot(norm_x.T))
    return a_vec

def pca_recover(x, y):
    (norm_x, norm_y) = normalize(x,y)
    norm_x = norm_x.A1
    norm_y = norm_y.A1
    data = [(norm_x[i],norm_y[i]) for i in xrange(norm_x.shape[0])]
    pca = PCA(n_components=1)
    pca.fit(data)
    V = pca.components_
    return V[0][1]/V[0][0]

def generate_points(n_trials, all_c):
    pca_vals = {c:[] for c in all_c}
    lsr_vals = {c:[] for c in all_c}
    for i in xrange(n_trials):
        for c in all_c:
            x = np.arange(0.001,1.001,0.001)

            # y = 2 * x
            y = np.arange(0.002,2.002,0.002)
            y += randn(1000)*math.sqrt(c)
            x += randn(1000)*math.sqrt(c)
            pca_vals[c].append(pca_recover(x,y))
            lsr_vals[c].append(ls_recover(x,y)[0,0])
    return ([pca_vals[c] for c in all_c],[lsr_vals[c] for c in all_c])

def scatterplot(x_vals, pca_y, lsr_y):
    fig, ax = plt.subplots()
    ax.scatter(x_vals, lsr_y,facecolors='b',edgecolors='b', label = 'Least Squares')
    ax.scatter(x_vals, pca_y,facecolors='r',edgecolors='r', label = 'Principal Components')
    legend = ax.legend(loc = 'upper left')
    plt.xlabel("c value")
    plt.ylabel("recovered slope")
    plt.savefig('part2d_plot' + '.png', bbox_inches='tight')
    plt.show()


all_c = np.arange(.05,.55,0.05)
(pca_all, lsr_all) = generate_points(30, all_c)
scatterplot([a for a in all_c for x in xrange(30)], sum(pca_all,[]), sum(lsr_all,[]))
