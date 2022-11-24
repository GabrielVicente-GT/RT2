#Clase de material con albedo, defuse y espectro

class material:
    def __init__(self,defuse, albedo, spec):
        self.defuse = defuse
        self.albedo = albedo
        self.spec = spec