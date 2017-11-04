import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
import numpy as np
import os
import json
import pprint

CONFIG_PATH = os.path.join('..', 'config.json')
NUM_POINTS = 100


def smoothed_curve(xs, ys, zs):
	scale = np.linspace(0, 1, NUM_POINTS)
	tck, _ = interpolate.splprep([xs, ys, zs], s=0.1)
	return interpolate.splev(scale, tck)
	
if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim3d(-4, 4)
    ax.set_ylim3d(-4, 4)
    ax.set_zlim3d(-4, 4)
    
    with open(CONFIG_PATH, 'r') as config_data:
        data = json.loads(config_data.read())
    
    # add planets to plot 
    planets_x, planets_y, planets_z = [[d[pos] for d in data['planets']] for pos in ["x", "y", "z"]]

    ax.scatter(xs=planets_x, ys=planets_y, zs=planets_z, c='blue')
    for d, x, y, z in zip(data['planets'], planets_x, planets_y, planets_z):
        ax.text(x, y, z, d["name"])

    # add curve, and knots to plot
    points_x, points_y, points_z = [[d[pos] for d in data['points']] for pos in ["x", "y", "z"]]
    smooth_x, smooth_y, smooth_z = smoothed_curve(points_x, points_y, points_z)

    ax.scatter(points_x, points_y, points_z)
    ax.plot(smooth_x, smooth_y, smooth_z)

    plt.show()
