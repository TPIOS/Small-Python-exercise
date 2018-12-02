import scipy as sp
from scipy import linalg as LA
A = sp.rand(2, 2)
B = sp.rand(2, 2)

evals = LA.eigvals(A)
# print(evals)
evals, evect = LA.eig(A)
print("eigenvalues:",evals)
print("eigenvectors:",evect)

print(LA.inv(A))

print(LA.det(A))