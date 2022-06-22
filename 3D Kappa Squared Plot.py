# for generating data
import random

# for linear algebra
import numpy as np

# for visualizing data
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
# draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


def unit_sphere(center_x, center_y):
   
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
    
    r = 1
    
    x = r * np.cos(u) * np.sin(v) + center_x
    y = r * np.sin(u) * np.sin(v) + center_y
    z = r * np.cos(v)
    
    return x, y, z


def transition_vector(center_x, center_y):

    u = np.random.uniform(0, 2) * np.pi
    v = np.random.uniform(0, 1) * np.pi
    
    x = np.cos(u) * np.sin(v) 
    y = np.sin(u) * np.sin(v) 
    z = np.cos(v)
    
    return x, y, z


def l2_norm(vector):
    
    v = vector ** 2
    v = v.sum()
    v = np.sqrt(v)
    
    return v   


def kappa_squared(dv, rv, av):
    
    k = (np.dot(dv, av) - 3 * np.dot(dv, rv) * np.dot(rv, av))
    k = k ** 2 
    
    return k


# initialize axes
fig = plt.figure(figsize=(20,10))
ax = plt.axes(projection='3d')

# plot donor center and surface
x, y, z = unit_sphere(-1, 0)
ax.plot_wireframe(x, y, z, color="b", alpha=0.25)
ax.plot(-1, 0, 0, 'ob', label='donor')

# plot acceptor center and surface 
x, y, z = unit_sphere(1, 0)
ax.plot_wireframe(x, y, z, color="r", alpha=0.25)
ax.plot(1, 0, 0, 'or', label='acceptor')

#plot vectors
## center-to-center vector "r"
x = np.linspace(-1, 1, 10)
y = np.zeros(10)
z = np.zeros(10)
r_vector = np.array([1, 0, 0])
ax.plot(x, y, z, '-k', label='r', alpha=0.7)

## donor transition 
x, y, z = transition_vector(-1, 0)
d_vector = np.array([x, y, z])
d_norm = l2_norm(d_vector)
ax.quiver(-1, 0, 0, x, y, z)

## acceptor transition
x, y, z = transition_vector(1, 0)
a_vector = np.array([x, y, z])
a_norm = l2_norm(a_vector)
ax.quiver(1, 0, 0, x, y, z)

# format axes
ax.legend()
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)

ax.set_title(f'Donor-Acceptor Kappa Squared {kappa_squared(d_vector, r_vector, a_vector):0.2f}')

plt.show()