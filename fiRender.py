#Funciones que pueden tener o no el uso de instancias de Render

import struct
from vector import *
from coloration import *

def reflect(I,N):
    return (I - N*2 * (N@I)).normalize()
#Escribe BMP
def writebmp(filename,width, height, framebuffer):
    f = open(filename, 'bw')

    #pixel header

    f.write( char('B'))
    f.write( char('M'))
    f.write( dword(14 + 40 + width * height* 3))
    f.write( word(0))
    f.write( word(0))
    f.write( dword(14+40))

    #info header

    f.write( dword(40))
    f.write( dword(width))
    f.write( dword(height))
    f.write( word(1))
    f.write( word(24))
    f.write( dword(0))
    f.write( dword(width*height*3))
    f.write( dword(0))
    f.write( dword(0))
    f.write( dword(0))
    f.write( dword(0))

    # pixel data

    for y in range(height):
        for x in range(width):
            f.write(framebuffer[y][x].toBytes())

    f.close()


#Shader que funciona con o sin textura con un valor de r definido
def shader_rosado(renderizado, **kwargs):
    tA, tB, tC = kwargs['texture_coords']
    nA, nB, nC = kwargs['normals']
    A, B, C = kwargs['vertices']
    w, u, v = kwargs['bar']
    L = V3(1,1,1)

    if renderizado.texture:
        iA,iB, iC  = nA.normalize() @ L.normalize() , nB.normalize() @ L.normalize(), nC.normalize() @ L.normalize()

        i = iA * w + iB * u + iC * v

        tx = tA.x * w + tB.x * u + tC.x * v
        ty = tA.y * w + tB.y * u + tC.y * v

        r,g,b = renderizado.texture.GetColorIntensity(tx,ty,i)

        return color(150,g,r)
    else:
        iA,iB, iC  = nA.normalize() @ L.normalize() , nB.normalize() @ L.normalize(), nC.normalize() @ L.normalize()

        i = iA * w + iB * u + iC * v

        azul    = abs(round(255*i))
        rojo    = abs(round(i))
        verde   = abs(round(i))

        return color(max(min(rojo,255),0),max(min(verde,255),0) ,max(min(azul,255),0))

#Shader que funciona con o sin textura
def shaders(renderizado, **kwargs):
    tA, tB, tC = kwargs['texture_coords']
    nA, nB, nC = kwargs['normals']
    A, B, C = kwargs['vertices']
    w, u, v = kwargs['bar']
    L = V3(1,1,1)

    if renderizado.texture:
        iA,iB, iC  = nA.normalize() @ L.normalize() , nB.normalize() @ L.normalize(), nC.normalize() @ L.normalize()

        i = iA * w + iB * u + iC * v

        tx = tA.x * w + tB.x * u + tC.x * v
        ty = tA.y * w + tB.y * u + tC.y * v

        r,g,b = renderizado.texture.GetColorIntensity(tx,ty,i)

        return color(b,g,r)
    else:
        iA,iB, iC  = nA.normalize() @ L.normalize() , nB.normalize() @ L.normalize(), nC.normalize() @ L.normalize()

        i = iA * w + iB * u + iC * v

        azul    = abs(round(255*i))
        rojo    = abs(round(255*i))
        verde   = abs(round(255*i))

        return color(max(min(rojo,255),0),max(min(verde,255),0) ,max(min(azul,255),0))

#Cuadro delimitador
def bounding_box(A,B,C):
    coors = [(A.x, A.y), (B.x, B.y), (C.x, C.y)]

    xmin = 999999
    xmax = -999999
    ymin = 999999
    ymax = -999999

    for (x,y) in coors:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y

    return V3(xmin, ymin), V3(xmax, ymax)

#Multiplicacion entre V3 externa y unica
def mul_externa(v0,v1):
    return(
        v0.y * v1.z - v0.z * v1.y,
        v0.z * v1.x - v0.x * v1.z,
        v0.x * v1.y - v0.y * v1.x
    )

#Puntos baricentricos
def barycentric(A,B,C,P):
    cx,cy, cz = mul_externa(
                    V3(B.x - A.x, C.x - A.x, A.x-P.x),
                    V3(B.y - A.y, C.y - A.y, A.y-P.y) )

    if cz == 0:
        u = 0
        v = 0
        w = 0.0001
    else:
        u = cx/cz
        v = cy/cz
        w = 1-(u+v)

    return(w,v,u)

#Byte de color
def color(r,g,b):
    return bytes([b, g, r])

#Struct que permite esribir archivo bmp
def dword(d):
    #4bytes
    return struct.pack('=l', d)

def word(w):
    #2bytes
    return struct.pack('=h', w)

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))
