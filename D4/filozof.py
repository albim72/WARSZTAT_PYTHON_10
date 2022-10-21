odp = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź? (t/n): ")
if odp.lower() == 't':
    required = True
else:
    required = False

def odpowiedz(self,*args):
    return "Tak! Ziemia jest płaska!"

def odpowiedz_new(self,*args):
    return "Nie! Ziemia jest okrągła!"


class SednoOdpowiedzi(type):

    def __init__(cls,clsname,spcls,attrs):
        if required:
            if clsname =="Kopernik":
                cls.odpowiedz = odpowiedz_new
            else:
                cls.odpowiedz = odpowiedz

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass
class Platon(metaclass=SednoOdpowiedzi):
    pass
class SwTomasz(metaclass=SednoOdpowiedzi):
    pass
class Kopernik(metaclass=SednoOdpowiedzi):
    # def odpowiedz(self, *args):
    #     return "Nie! Ziemia jest okrągła!"
    pass


fil1 = Arystoteles()
print(fil1.odpowiedz())

fil2 = Platon()
print(fil2.odpowiedz())

fil3 = SwTomasz()
print(fil3.odpowiedz())

fil4 = Kopernik()
print(fil4.odpowiedz())
