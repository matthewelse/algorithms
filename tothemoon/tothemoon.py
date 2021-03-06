"""
    Basic Gravity Simulation (No Animation)
    Uses Newton's Universal Law of Gravitation and the Forward Euler Method
    to estimate position of a projectile (in the code, called the moon). The
    black circle in the diagram represents the usual distance of the moon's orbit
    the blue dot which will be very small in the diagram is the earth.

    02/02/2014
    Copyright Matthew Else 2014
"""
from scipy import constants
import numpy as np
from matplotlib import pyplot as mp
from matplotlib import animation as an


MASS_EARTH = 5.972E24 # kg
MASS_MOON = 7.34767309E22 # kg

MOON_STARTING_DISTANCE = 384400E3 # m
#MOON_STARTING_VELOCITY = np.array([0, 2.0230E3]) # m s^-1
MOON_STARTING_VELOCITY = np.array([-300, 2.0230E2]) # m s^-1

#MOON_STARTING_POSITION = np.array([-MOON_STARTING_DISTANCE, 0])
MOON_STARTING_POSITION = np.array([0.5E10, -0.2E10])

EARTH_RADIUS = 6371E3 # m

DT = 1000 # s

# m1, m2 in kg
# r in m
def F_g(m1, m2, r):
    return constants.G * m1 * m2 / r**2

# m1 in kg
# r in m
def A_g(m1, r):
    return -constants.G * m1 / r**2

# m1 in kg
# r in m^2
def A_g_r2(m1, r2):
    return -constants.G * m1 / r2

objects = {'earth': {'mass': MASS_EARTH,
                     'position': np.array([0, 0]),
                     'v': np.array([0, 0])},
           'moon':  {'mass': MASS_MOON,
                     'position': MOON_STARTING_POSITION,
                     'v': MOON_STARTING_VELOCITY}
           }

moon_points_x = [objects['moon']['position'][0],]
moon_points_y = [objects['moon']['position'][1],]

# Evaluate the acceleration towards the earth...

for i in range(50000):
    a = A_g_r2(MASS_EARTH, objects['moon']['position'][0]**2 + objects['moon']['position'][1]**2)
    a = (objects['moon']['position']/np.linalg.norm(objects['moon']['position'])) * a

    objects['moon']['v'] = (a * DT) + objects['moon']['v']
    objects['moon']['position'] = (objects['moon']['v'] * DT) + objects['moon']['position']
    moon_points_x.append(objects['moon']['position'][0])
    moon_points_y.append(objects['moon']['position'][1])

fig = mp.figure()
ax = fig.add_subplot(111)
circle = mp.Circle((0,0), radius=MOON_STARTING_DISTANCE, fill=False)
ax.add_patch(circle)
ax = fig.add_subplot(111)
circle = mp.Circle((0,0), radius=EARTH_RADIUS)
ax.add_patch(circle)
ax = fig.add_subplot(111)
mp.axis('equal')
ax.scatter(moon_points_x, moon_points_y)
mp.show()
