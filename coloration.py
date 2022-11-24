#clase de nuevo color definicion

class color:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, other):
        r = self.r
        b = self.b
        g = self.g
        if type(other)==int or type(other)==float :
            r *= other
            g *= other
            b *= other
        else:
            r *= other.r
            g *= other.g
            b *= other.b

        r = min(255,max(r,0))
        g = min(255,max(g,0))
        b = min(255,max(b,0))

        return color(r,g,b)

    def __add__(self, other):
        r = self.r
        b = self.b
        g = self.g
        if type(other)==int or type(other)==float :
            r += other
            g += other
            b += other
        else:
            r += other.r
            g += other.g
            b += other.b

        r = min(255,max(r,0))
        g = min(255,max(g,0))
        b = min(255,max(b,0))

        return color(r,g,b)

    def toBytes(self):
        return bytes ([int(self.b), int(self.g), int(self.r)])