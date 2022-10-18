print("to linia na dobry początek")

# komentarz - kolekcja: lista

"""
komentarz dokumentacyjny wieloliniowy
"""

'''
komentarz wieloliniowy
'''

imiona = ["Jan", "Paweł", "Leon", "Anna", "Olga", "Leon", "Tekla", "Grzegorz", "Magda", "Leon"]

print(imiona)
print(imiona[0])
print(imiona[2:6])
print(imiona[-2])

w = "kalejdoskop"
print(w)
print(w[3])
print(w[2:4])

print(imiona[0][1])

imionaparz = imiona[::2]

print(imionaparz)

imionanparz = imiona[1::2]

print(imionanparz)

wyr1 = "listopad"
wyr2 = "Urszula"

wyr1o = wyr1[::-1]
wyr2o = wyr2[::-1]

print(wyr1, "-", wyr1o)
print(wyr2, "-", wyr2o)

imiona.append("Klara")
print(imiona)

imiona.insert(2, "Hanka")
print(imiona)

imiona.remove("Leon")
print(imiona)

el = imiona.index("Anna")
del imiona[el]
print(imiona)

team = imiona
team_n = imiona[:]
team_m = list(imiona)
print("_____________________________________________")
print(imiona)
print(team)
print(team_n)
print(team_m)

imiona[2:4] = ["Henryk", "Olaf", "Berta", "Ewa"]
print("_____________________________________________")
print(imiona)
print(team)
print(team_n)
print(team_m)

print("_____________________________________________")
for imie in imiona:
    print(imie)

k = 999
print(k)
print(type(k))

h: float
h = 0.0066555
print(h)
print(type(h))

h = 1
print(h)
print(type(h))

h = "blabla"
print(h)
print(type(h))

h = ["blabla", 5345, 4.6656, True]
print(h)
print(type(h))

# krotka

miasta = ("Kraków", "Lublin", "Warszawa", "Kraków", "Poznań", "Wrocław", "Gdańsk", "Kraków")
print(miasta)
print(type(miasta))

print(miasta.count("Kraków"))
imiona.sort()
print(imiona)

miasta_list = list(miasta)
miasta_list.append("Kielce")

miasta = tuple(miasta_list)
print(miasta)
