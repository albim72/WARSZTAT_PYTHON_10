#interface - w pythonie taka struktura nie istnieje!

from abc import ABCMeta, abstractmethod

class IPojazd:

    __metaclass__ = ABCMeta

    @abstractmethod
    def silnik(self,rodzaj_poj,kategoria,marka,model,rodzaj_silnika,poj):
        raise NotImplementedError

    @abstractmethod
    def trasa(self,start,koniec,odl,czas_przejazdu):
        raise NotImplementedError

    @abstractmethod
    def set_paliwo(self,cena_l):
        self._cena_l = cena_l

    @abstractmethod
    def spal_100(self,odl,litry):
        raise NotImplementedError

    @abstractmethod
    def koszt_przejazdu(self,odl,litry,cena_l):
        raise NotImplementedError

class Pojazd(IPojazd):

    def silnik(self, rodzaj_poj, kategoria, marka, model, rodzaj_silnika, poj):
        return f"Pojazd -> {rodzaj_poj}, {kategoria}, marka:{marka}, model: {model}," \
               f" rodzaj silnika: {rodzaj_silnika}, pojemność:; {poj}."

    def trasa(self, start, koniec, odl, czas_przejazdu):
        trasa = f"początek trasy: {start}, koniec trasy: {koniec}"
        przej = f"odległość: {odl} km, czas przejazdu {czas_przejazdu} h"
        return trasa,przej

    def set_paliwo(self, cena_l):
        super().set_paliwo(cena_l)

    def spal_100(self, odl, litry):
        return litry*100/odl

    def koszt_przejazdu(self, odl, litry, cena_l):
        return self.spal_100(odl,litry)*(odl/100)*cena_l
