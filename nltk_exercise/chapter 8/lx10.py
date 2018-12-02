import matplotlib.pyplot as plt
from matplotlib import figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# n = 12
# X = np.arange(n)
# Y1 = np.random.uniform(0.5, 1.0, n)
# Y2 = np.random.uniform(0.5, 1.0, n)
# plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
# plt.savefig("extra1.png")
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2+ + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

plt.savefig('extra2.png')