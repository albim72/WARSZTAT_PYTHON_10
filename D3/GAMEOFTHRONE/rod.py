from abc import ABC,abstractmethod

class CzlonekRodu(ABC):

    def __init__(self,rod,tytul,plec,punkty_walki,punkty_palacowe,doswiadczenie):
        self.rod = rod
        self.tytul = tytul
        self.plec = plec
        self.punkty_walki = punkty_walki
        self.punkty_palacowe = punkty_palacowe
        self.doswiadczenie = doswiadczenie

    @abstractmethod
    def walka(self):
        pass

    @abstractmethod
    def negocjacja(self):
        pass

    @abstractmethod
    def uczta(self):
        pass
