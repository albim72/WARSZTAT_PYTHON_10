#przykład 1

def witaj(imie):
    return f"Miło Cię znowu widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik {imie}, liczba punktów = {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Tomek",45))
