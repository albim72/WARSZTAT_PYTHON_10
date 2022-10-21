#interface - w pythonie taka struktura nie istnieje!

from abc import ABC, ABCMeta, abstractmethod

class IPojazd:

    __metaclass__ = ABCMeta

    @property
    def paliwo(self):
        return self._cena_l

    @paliwo.setter
    def paliwo(self, cena_l):
        self._cena_l = cena_l

    @abstractmethod
    def silnik(self,rodzaj_poj,kategoria,marka,model,rodzaj_silnika,poj):
        raise NotImplementedError(f"obowiązkowo zainplementuj metodę")

    @abstractmethod
    def trasa(self,start,koniec,odl,czas_przejazdu):
        raise NotImplementedError(f"obowiązkowo zainplementuj metodę")

    @abstractmethod
    def spal_100(self,odl,litry):
        raise NotImplementedError(f"obowiązkowo zainplementuj metodę")

    @abstractmethod
    def koszt_przejazdu(self,odl,litry,cena_l):
        raise NotImplementedError(f"obowiązkowo zainplementuj metodę")


class Pojazd(IPojazd):

    # def __init__(self,_cena_l):
    #     self._cena_l = _cena_l


    def silnik(self, rodzaj_poj, kategoria, marka, model, rodzaj_silnika, poj):
        return f"Pojazd -> {rodzaj_poj}, {kategoria}, marka:{marka}, model: {model}," \
               f" rodzaj silnika: {rodzaj_silnika}, pojemność:; {poj}."

    def trasa(self, start, koniec, odl, czas_przejazdu):
        trasa = f"początek trasy: {start}, koniec trasy: {koniec}"
        przej = f"odległość: {odl} km, czas przejazdu {czas_przejazdu} h"
        return trasa,przej


    def spal_100(self, odl, litry):
        return litry*100/odl

    def koszt_przejazdu(self, odl, litry, cena_l):
        return self.spal_100(odl,litry)*(odl/100)*cena_l


p = Pojazd()

print(p.silnik("samochód","osobowy","Opel","Vectra","diesel",1.9))
tr,pr = p.trasa("Lublin","Warszawa",173,1.5)
print(f"trasa: {tr}, {pr}")

print(f"spalanie silnika [l/100km]: {p.spal_100(173,19):.2f}")
p.paliwo = 8.09
print(p.paliwo)

print(f"koszt przejazdu: {p.koszt_przejazdu(173,19,p.paliwo)} zł")


