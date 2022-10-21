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


