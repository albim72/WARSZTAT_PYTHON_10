from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self,a,b):
        self.a=a
        self.b=b

    @abstractmethod
    def policz_pole(self):
        pass

    @abstractmethod
    def policzobwod(self):
        pass

class Prostokat(Figura):

    def policz_pole(self):
        return self.a*self.b

    def policzobwod(self):
        pass


class Trojkat(Figura):

    def policz_pole(self):
        return self.a*self.b/2

    def policzobwod(self):
        pass



pr = Prostokat(4.5,5.7)
print(f'pole prostokąta wynosi:; {pr.policz_pole():.2f}')

tr = Trojkat(5.4,7.2)
print(f'pole trójkąta wynosi:; {tr.policz_pole():.2f}')


class Trapez(Figura):

    def __init__(self,a,b,h):
        super().__init__(a,b)
        self.h=h

    def policz_pole(self):
        return (self.a+self.b)*self.h/2

    def policzobwod(self):
        pass


trp = Trapez(5.5,4.3,4)
print(f'pole trapezu wynosi:; {trp.policz_pole():.2f}')

#zbuduj klasę Kolo i policz jego pole dla promienia = 5.5



