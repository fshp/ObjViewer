import math

import numpy as np


class Point3f:
    def __init__(self, x, y, z):
        self.point = np.matrix([x, y, z, 1])

    def __call__(self):
        return self.point


class Polygons3f:
    def __init__(self, points=[]):
        self.points = points
        self.temp = self.points
        self.x = 0
        self.y = 0
        self.z = 0
        self.anglex = 0
        self.angley = 0
        self.anglez = 0
        self.mirrorx = False
        self.mirrory = False
        self.mirrorz = False
        self.scale = 1

    def __call__(self):
        rotatex = np.matrix([[1, 0, 0, 0],
                             [0, math.cos(self.anglex), -math.sin(self.anglex), 0],
                             [0, math.sin(self.anglex), math.cos(self.anglex), 0],
                             [0, 0, 0, 1]])

        rotatey = np.matrix([[math.cos(self.angley), 0, math.sin(self.angley), 0],
                             [0, 1, 0, 0],
                             [-math.sin(self.angley), 0, math.cos(self.angley), 0],
                             [0, 0, 0, 1]])

        rotatez = np.matrix([[math.cos(self.anglez), -math.sin(self.anglez), 0, 0],
                             [math.sin(self.anglez), math.cos(self.anglez), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])

        scale = np.matrix([[self.scale, 0, 0, 0],
                           [0, self.scale, 0, 0],
                           [0, 0, self.scale, 0],
                           [0, 0, 0, 1]])

        transfer = np.matrix([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 1, 0],
                              [self.x, self.y, self.z, 1]])

        mirrorx = np.matrix([[-1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]])

        mirrory = np.matrix([[1, 0, 0],
                             [0, -1, 0],
                             [0, 0, 1]])

        m = rotatex * rotatez * rotatey * scale * transfer
        # if self.mirrorx: m *= mirrorx
        #if self.mirrory: m *= mirrory
        temp = []

        for p in self.points:
            temp.append((p * m).tolist()[0])
        return temp


    def set_scale(self, scale):
        self.scale += scale;

    def set_anglex(self, angle):
        self.anglex += math.radians(angle)
        degrees = math.degrees(self.anglex)
        sign = math.copysign(1, degrees)
        self.anglex = math.radians(sign * (abs(degrees) % 360))

    def set_angley(self, angle):
        self.angley += math.radians(angle)
        degrees = math.degrees(self.angley)
        sign = math.copysign(1, degrees)
        self.angley = math.radians(sign * (abs(degrees) % 360))

    def set_anglez(self, angle):
        self.anglez += math.radians(angle)
        degrees = math.degrees(self.anglez)
        sign = math.copysign(1, degrees)
        self.anglez = math.radians(sign * (abs(degrees) % 360))

    def set_x(self, x):
        self.x += x

    def set_y(self, y):
        self.y += y

    def set_z(self, z):
        self.z += z

