# import dane
# import dane as dn
from dane import book as ksiazka
from dane import nb as liczba
from bfunkcje import czytaj,czytaj_dict
from cls.sdane.czytaniedanych import CDane

print(ksiazka)
print(liczba)

czytaj(liczba)
czytaj_dict(ksiazka)
print("________________z klasy________________")
cd = CDane(liczba,ksiazka)

cd.czytaj_l()
cd.czytaj_d()

