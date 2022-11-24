#Clase esfera que permite ddibujar una esfera

from intersection import *

class Esfera(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, origin, direction):
        L = self.center - origin
        tca = L @ direction
        l = L.largo()

        d2 = l**2- tca**2

        if d2>self.radius**2:
            return None

        thc = (self.radius**2-d2)**0.5

        t0 = tca - thc
        t1 = tca + thc


        if t0 < 0:
            t0 = t1
        if t0 < 0 :
            return None

        impact = origin +  direction * t0
        normal = (impact - self.center).normalize()

        return Intersect(t0, impact, normal)