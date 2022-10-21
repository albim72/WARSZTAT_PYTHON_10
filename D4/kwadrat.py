class Kwadrat:

    def __init__(self,bok):
        self.bok = bok

    def pole(self):
        return self.bok**2


class Prostokat:

    def __new__(cls, width:float, height:float):
        if width == height:
            return Kwadrat(bok=width)
        return object.__new__(Prostokat)

    def __init__(self,width:float, height:float):
        self.width = width
        self.height = height

    def pole(self):
        return self.width*self.height

r1 = Prostokat(41,23)
r2 = Prostokat(6,6)

print(type(r1))
print(f"pole r1 = {r1.pole()}")
print(type(r2))
print(f"pole r1 = {r2.pole()}")
