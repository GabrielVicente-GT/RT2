#Gabriel Alejandro Vicente Lorenzo
#20498

#RT2

from raytracer_2 import *
from Material import *
from coloration import *

#Creados para el rt2
oscuro          = material(defuse = color(0,0,0),           albedo = [0.6, 0.3, 0], spec = 35)
vesh            = material(defuse = color(212, 136, 102),   albedo = [0.9, 0.1, 0], spec = 50)
naranjapalido   = material(defuse = color(230, 115, 52),    albedo = [0.7, 0.2, 0], spec = 30)
corinto         = material(defuse = color(250,0  ,0  ),     albedo = [0.6, 0.3, 0], spec = 10)
platedo         = material(defuse = color(189, 195, 199  ), albedo = [0.6, 0.3, 0], spec = 10)
nieve           = material(defuse = color(200,200,200),     albedo = [1.3, 0.1, 0], spec = 50)
espejo          = material(defuse = color(255,255,255 ),    albedo = [0,1,0.8],     spec = 1425)

#Inicialiacion de un render para hacer el raytracer
r                   = Raytracer(800,600)
r.background_color  = color(248, 249, 240)
r.luz               = Light(V3(-0, 0, 0), 1, color(255, 255, 255))

#Objetos con raytracer
r.objetos           = [
#Oso Derecha
    #cuerpo
    Esfera(V3(3, 0+0.5, -10), 1.5,      corinto),
    #Cabeza
    Esfera(V3(3, -2+0.5, -9.5), 1,      vesh),
    #Brazos
    Esfera(V3(4, 1+0.5, -9), 0.5,       vesh),
    Esfera(V3(4.2, -1+0.5, -9), 0.5,    vesh),
    Esfera(V3(1.5, 1+0.5, -9), 0.5,     vesh),
    Esfera(V3(1.5, -1+0.5, -9.5), 0.5,  vesh),
    #Boca
    Esfera(V3(2.85, -1.7+0.5, -8.8), 0.5, naranjapalido),
    #Ojos y nariz
    Esfera(V3(2.77, -1.7+0.5, -8.3), 0.1,   oscuro),
    Esfera(V3(2.4, -2.1+0.5, -8.3), 0.1,    oscuro),
    Esfera(V3(3.05, -2.1+0.5, -8.3), 0.1,   oscuro),
    #Orejas
    Esfera(V3(2.2, -2.8+0.5, -9.5), 0.5,    naranjapalido),
    Esfera(V3(3.8, -2.8+0.5, -9.5), 0.5,    naranjapalido),
    
#Oso Izquierda
    #cuerpo
    Esfera(V3(-3, 0+0.5, -10), 1.5,     platedo),
    #Cabeza
    Esfera(V3(-3, -2+0.5, -9.5), 1,     nieve),
    #Brazos
    Esfera(V3(-4, 1+0.5, -9), 0.5,      nieve),
    Esfera(V3(-4.2, -1+0.5, -9), 0.5,   nieve),
    Esfera(V3(-1.5, 1+0.5, -9), 0.5,    nieve),
    Esfera(V3(-1.5, -1+0.5, -9.5), 0.5, nieve),
    #Boca
    Esfera(V3(-2.85, -1.7+0.5, -8.8), 0.5,  nieve),
    #Ojos y nariz
    Esfera(V3(-2.77, -1.7+0.5, -8.3), 0.1,  oscuro),
    Esfera(V3(-2.4, -2.1+0.5, -8.3), 0.1,   oscuro),
    Esfera(V3(-3.05, -2.1+0.5, -8.3), 0.1,  oscuro),
    #Orejas
    Esfera(V3(-2.2, -2.8+0.5, -9.5), 0.5,   nieve),
    Esfera(V3(-3.8, -2.8+0.5, -9.5), 0.5,   nieve),
]

r.render()
r.write('rt2.bmp')
