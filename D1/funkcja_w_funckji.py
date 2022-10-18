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


#przykład3

def startstop(funkcja):
    def wrapper(*args):
        print("Startowanie procesu....")
        funkcja(*args)
        print("Kończenie procesu....")
    return wrapper

def zawijanie():
    print("zawijanie czekoladek w sreberka")
print("__________________________________")
zw = startstop(zawijanie)
zw()

@startstop
def dmuchanie():
    print("dmuchanie baloników na imprezę...")


print("__________________________________")
dmuchanie()
print("__________________________________")
@startstop
def fx(n):
    print(f"wynik = {n*2}")

fx(9)

