from clss.trener import Trener
from clss.sport import Sport

class Klient(Trener,Sport):

    def __init__(self,imie, wiek, waga, wzrost,nr_klienta,miasto,
                 nr_licencji="",lata_dosw="",expert="",nr_kb="",nazwa_kb="",adres="",dyscyplina="",
                 lata_upr="",zyciowka=""):
        Trener.__init__(self,imie, wiek, waga, wzrost,nr_licencji,lata_dosw,expert,
                 nr_kb,nazwa_kb,adres)
        Sport.__init__(self,dyscyplina,lata_upr,zyciowka)
        self.nr_klienta = nr_klienta
        self.miasto = miasto
        self.numerklienta()


    def numerklienta(self):
        print(f"przydzielono numer klienta: {self.nr_klienta}")
    def czytrener(self):
        return self.nr_licencji != ""
