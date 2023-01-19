import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
print(a)
print(type(b))
#print(x)