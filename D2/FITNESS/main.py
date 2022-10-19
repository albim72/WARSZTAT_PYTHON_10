from clss.osoba import Osoba
from clss.trener import Trener
from clss.klient import Klient

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

print("___________________________________________________________")

kl1 = Klient("Leon",27,80,180,678,"Lublin",nr_kb=26)
kl1.print_osoba()
print(f"czy osoba jest trenerem personalnym? ({kl1.czytrener()})")

print("___________________________________________________________")

kl2 = Klient("Anna",26,55,171,7654,"Kraków",7775,8,True,5,"Euforia","Wesoła 6, Wąchock")
kl2.print_osoba()
print(f"czy osoba jest trenerem personalnym? ({kl2.czytrener()})")
kl2.print_trener()
kl2.infoklub()


print("___________________________________________________________")

kl3 = Klient("Edyta",22,78,177,678567,"Zamość",nr_kb=26,dyscyplina="biegi ultra",lata_upr=3,
             zyciowka="105km 20h 16min 4s")
kl3.print_osoba()
print(f"czy osoba jest trenerem personalnym? ({kl3.czytrener()})")
print(kl3.infosport())

