#przykład 1

def witaj(imie):
    return f"Miło Cię znowu widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik {imie}, liczba punktów = {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Tomek",45))

#przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"
    def brak():
        return "jeśli chcesz znaleźć się na liście startowej, dokonaj wpłaty"
    def error():
        return "wpisz 1 - wpłata, 0 - brak wpłaty"
    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(6)())
