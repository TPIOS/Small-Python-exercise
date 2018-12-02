from scipy import sparse as sp
import numpy as np
A = np.array([[1,0,0],[0,2,0],[0,0,3]])
C = sp.csr_matrix(A)

print(A)
print(C)
print(C.toarray())
print(C * C.todense())
print(np.dot(C,C).todense())
