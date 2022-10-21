class MojaMeta(type):

    def __new__(cls, clsname,supercls,attrs):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {supercls}")
        print(f"atrybuty: {attrs}")
        return type.__new__(cls,clsname,supercls,attrs)

class Pierwsza:
    pass

class Specjalna(Pierwsza,metaclass=MojaMeta):
    pass

class Kolejna(Specjalna):
    pass


p1 = Pierwsza()
p2 = Specjalna()
p3 = Kolejna()
