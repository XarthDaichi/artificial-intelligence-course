import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#  the trajectory
def plot_trajectory(trajectory, f):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-2, 2, 100)
    y = np.linspace(-1, 3, 100)
    x, y = np.meshgrid(x, y)
    z = f(x, y)

    ax.plot_surface(x, y, z)# cmap='viridis')

    x_traj, y_traj = trajectory[:, 0], trajectory[:, 1]
    z_traj = f(x_traj, y_traj)
    
    ax.plot(x_traj, y_traj, z_traj, marker='>', color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('$f(X, Y)$')

    plt.show()


