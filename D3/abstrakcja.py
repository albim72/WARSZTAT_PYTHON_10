from abc import ABC, abstractmethod

class Prototyp(ABC):

    def __init__(self,x):
        self.x=x

    def msg(self):
        print("to jest metoda nieabstrakcyjna klasy abstrakcyjnej")

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*3


class ZwKlasa(Prototyp):

    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 45

    def policz_x(self):
        return super().policz_x() + 6*self.y


z = ZwKlasa(4,6)
z.msg()

print(z.policz())
print(z.policz_x())

