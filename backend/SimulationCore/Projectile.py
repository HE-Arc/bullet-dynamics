import math as m

class Projectile:
    def __init__(self,x,y,v0,mass,frontalradius,cx,name=""):
        self.ax = 0.0
        self.ay = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.trajectorysX =[]
        self.trajectorysY =[]
        self.speedsX =[]
        self.energies = []
        self.times = []
        self.x = x
        self.y = y
        self.v0 = v0
        self.mass = mass
        self.cx = cx
        self.name = name
        self.surface = m.pi*(frontalradius**2)
