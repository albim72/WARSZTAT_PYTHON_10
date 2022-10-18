kolory = {"zielony","czerwony","niebieski","biały","fioletowy","żółty","biały"}

print(kolory)
print(kolory)
print(kolory)

kolory.add("pomarańczowy")
print(kolory)

kolory.update(["magenta","brąz","szary"])
print(kolory)

kolory.remove("zielony")
print(kolory)

kolory.discard("oliwkowy")
print(kolory)

kolory.discard("żółty")
print(kolory)

kolory.add("czerwony")
print(kolory)

nb = [3,5,6,2,3,4,5,2,2,2,4,4,3,3,1,1,3,2,5]
nbs = set(nb)
print(nbs)

nb = list(nbs)
print(nb)

osoba = {
    "imię":"Jan",
    "nazwisko":"Kot",
    "wiek":50
}

print(osoba)

print(osoba["nazwisko"])
osoba["wiek"] = 52

print(osoba)

osoba["miasto"] = "Toruń"

print(osoba)

# osoba.clear()
#
# print(osoba)

del osoba["wiek"]
print(osoba)

print(osoba.items())
print(osoba.keys())
print(osoba.values())

print("_______________klucze_______________")
for x in osoba:
    print(x)

print("_______________wartości_______________")
for x in osoba:
    print(osoba[x])

print("_______________wartości inaczej_______________")
for x in osoba.values():
    print(x)

print("_______________wartości parami_______________")
for x,y in osoba.items():
    print(f"{x}: {y}")
