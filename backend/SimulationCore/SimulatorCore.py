import numpy as np
import math as m
from .Projectile import *

# Constants
RHO = 1.22 #air density
g = 9.81 # gravity
NB_TICKS = 5000 # resolution of simulation
FLOOR_HEIGHT = -10 # height of the floor (the floor catch the projectile) must be (<= 0)
THETA = 0 # initial angle of fire
T0 = 0 # start time
T_END = 15 # end time

class Simulator:

    def __init__(self):
        self.projectiles = []

    def run(self,v0,mass,cx,theta=THETA,floorh=FLOOR_HEIGHT):
        self.projectiles.append(Projectile(0,0,v0,mass,0.003**2*m.pi,cx,"p1"))
        # Mathematical simulation of projectiles trajectory, speed, energy
        #   - Calculations are made on each axis individualy, and made sequentialy :
        #       - At first the accelerations are computed
        #       - Then the speeds based on previous speeds and accelerations
        #       - The new positions can then be updated based on the last and speed
        #
        #   - Air drag is computed with respect to :
        #       - air density, drag coeff., frontal surface and speed
        # 

        theta = theta/360 * 2 * m.pi # convert to rad
        tickSize = (T_END-T0)/NB_TICKS
        t = np.linspace(T0, T_END, num=NB_TICKS)
        maxX = 0
        for p in self.projectiles:

            p.vx = np.cos(theta) * p.v0
            p.vy = np.sin(theta) * p.v0
            p.ax = 0
            p.ay = -g
            
            for k in t:
                p.ax = -0.5*p.cx*RHO*p.surface*(p.vx**2)/p.mass
                if p.vy > 0:
                    p.ay = (-g*p.mass -0.5*p.cx*RHO*p.surface*(p.vy**2))/p.mass
                else:
                    p.ay = (-g*p.mass + 0.5*p.cx*RHO*p.surface*(p.vy**2))/p.mass
                p.vx = p.vx + p.ax*tickSize
                p.vy = p.vy + p.ay*tickSize

                p.x = p.x + p.vx*tickSize
                p.y = p.y + p.vy*tickSize

                if p.y < floorh:
                    break
                if p.x > maxX:
                    maxX = p.x
                p.trajectorysX.append(p.x)
                p.trajectorysY.append(p.y)
                p.speedsX.append(p.vx)
                p.energies.append((p.vx**2)*p.mass/2)
                p.times.append(k)

        for p in self.projectiles:
            tabOutput = []
            tabOutput.append(p.trajectorysX)
            tabOutput.append(p.trajectorysY)
        return tabOutput