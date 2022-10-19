liczby = [56,9009,-1009,0,35,-4,12,39,555,-123,99,101]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    return minimum,maksimum,rozstep

wynik = pokaz_stat(liczby)
print(wynik)

mini, maxi, roz = pokaz_stat(liczby)
print(f"wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}")
