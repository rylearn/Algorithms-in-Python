import numpy as np
import sys

# given a file name of a bitmap,
# list of lists of ints, np.array
def read_into_array(f_name): 
    all_lines = []
    with open(f_name) as f:
        for line in f:
            # map turns the "1" into 1
            all_lines.append(map(int, line.split()))
    return np.array(all_lines, dtype = np.int16)

def clamp(x):
    if x > 1.0:
        return 1
    elif x < 0.0:
        return 0
    else:
        return x

# svd matrix to a file
def write_binary_output(svd_mat, f_name):
    with open(f_name, 'w') as f_out:
        for i in range(svd_mat.shape[0]):
            for j in range(svd_mat.shape[1]):
                x = clamp(svd_mat[(i,j)])
                if x == 0 or x == 1:
                    f_out.write("%d " % int(x))
                else:
                    f_out.write("%.2f " % x)
            f_out.write('\n')

def create_D(u_dim, s, v_dim):
    d = np.eye(max(u_dim, v_dim))[0:u_dim, 0:v_dim]
    for i in range(len(s)):
        d[i, i] = s[i]
    return d

# Low rank approx of matrix
# keep first k rows and remove rest
def k_rank_svd(mat_x, k):
    (u, s, v_T) = np.linalg.svd(np.mat(mat_x))
    v = v_T.T       # V transpose to v
    s = np.hstack( (s[0:k], np.zeros(len(s) - k)) )
    (u_dim, v_dim) = (u.shape[0], v.shape[0])
    d = create_D(u_dim, s, v_dim)
    x = u[0:u_dim, 0:k]         # values to retain, top k rows
    u = np.hstack( (x, np.zeros(shape = (u_dim, u_dim - k)) ) )
    y = v[0:v_dim, 0:k]         # values to retain, top k rows
    v = np.hstack( (y, np.zeros(shape = (v_dim, v_dim - k)) ) )
    return u.dot(d).dot(v.T)

# using script
f_in_name = "./" + sys.argv[1]
k = int(sys.argv[2])
# k = 150
# f_in_name = "./bitmaps/alice.txt"
mat_x = read_into_array(f_in_name)
mat_x_k = k_rank_svd(mat_x, k)
print np.count_nonzero(mat_x_k)
write_binary_output(mat_x_k, "binary_output.txt")
