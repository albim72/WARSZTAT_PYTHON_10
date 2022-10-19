from clss.osoba import Osoba
from clss.trener import Trener
from clss.klient import

os1 = Osoba("Feliks",43,88,175)
os1.print_osoba()
print(f"czy osoba jest trenerem personalnym? ({os1.czytrener()})")

print("___________________________________________________________")

os2 = Osoba("Ola",27,50,160)
os2.kolor_oczu = "niebieski"
os2.print_osoba()
print(f"czy osoba jest trenerem personalnym? ({os2.czytrener()})")

print("___________________________________________________________")

tr1 = Trener("Jacek",40,77,178,5435,13,True,4,"Alianz","ul. Złota 5, Krosno")
tr1.print_osoba()
print(f"czy osoba jest trenerem personalnym? ({tr1.czytrener()})")
print(tr1.infoklub())
tr1.print_trener()
