from scipy import optimize
def f(x):
    return x**2 - 4

print(optimize.fmin_bfgs(f, 0.2))
