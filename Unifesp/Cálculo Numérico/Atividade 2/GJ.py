import numpy as np 
from scipy.sparse import csr_matrix, csc_matrix
from scipy.sparse.linalg import spsolve

A = csc_matrix((20, 20), dtype = np.int8).toarray()
print(A)
b = csr_matrix((1, 20), dtype = np.int8).toarray()
b = np.array(b)
print(b)
#x = spsolve(A, b)
