#Render proporcionado en clase para trabajar eficientemente
import struct
from fiRender import *

#Colores predefinidos
BLACK = color(0, 0, 0)

class Render(object):

    def __init__(self, width, height):
            self.width  = width
            self.height = height
            self.color_actual   = BLACK
            self.texture = None
            self.Model = None
            self.View = None
            self.Shader = None
            self.Fondo = None
            self.clear()

#Llena el frame con todo un color
    def clear(self):
        self.framebuffer = [
            [ self.color_actual for x in range(self.width)]
            for y in range(self.height)
        ]
        self.zbuffer = [
            [ -999999 for x in range(self.width)]
            for y in range(self.height)
        ]

#Escritura
    def write(self, filename):
        f = open(filename, 'bw')

        #pixel header

        f.write( char('B'))
        f.write( char('M'))
        f.write( dword(14 + 40 + self.width * self.height * 3))
        f.write( word(0))
        f.write( word(0))
        f.write( dword(14+40))

        #info header

        f.write( dword(40))
        f.write( dword(self.width))
        f.write( dword(self.height))
        f.write( word(1))
        f.write( word(24))
        f.write( dword(0))
        f.write( dword(self.width*self.height*3))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))
        f.write( dword(0))

        # pixel data

        for y in range(self.height):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()

#Punto
    def point(self, x, y):
        self.framebuffer[y][x] = self.color_actual

#Cambia el color actual
    def set_color(self, color):
        self.color_actual = color
