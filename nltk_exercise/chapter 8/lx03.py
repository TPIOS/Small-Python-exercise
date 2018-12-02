import scipy as sp
from scipy.integrate import quad, dblquad, tplquad
def f(x):
    return x

x_lower = 0
x_upper = 1
val, abserr = quad(f, x_lower, x_upper)
print(val, abserr)
