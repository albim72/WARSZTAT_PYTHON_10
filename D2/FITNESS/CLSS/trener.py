from osoba import Osoba
from klub import Klub

class Trener(Osoba,Klub):

    #konstruktor z wielodziedziczeniem
    def __init__(self,imie, wiek, waga, wzrost,nr_licencji,lata_dosw,expert,
                 nr_kb,nazwa_kb,adres):
        Osoba.__init__(self,imie, wiek, waga, wzrost)
        Klub.__init__(self,nr_kb,nazwa_kb,adres)
        self.nr_licencji = nr_licencji
        self.lata_dosw = lata_dosw
        self.expert = expert

    def print_trener(self):
        print(f"Trener nr licencji: {self.nr_licencji}, lata doświadczenia zawodowego: {self.lata_dosw},"
              f" poziom ekspercki? ({self.expert})")

