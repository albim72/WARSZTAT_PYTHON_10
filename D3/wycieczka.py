
def opis(funkcja):
    def wrapper(*args):
        print("Funkcja licząca koszt wyjazdu turystycznego z uwzględnieniem wybranych kosztów i rabatem.")
        funkcja(*args)
    return wrapper

def kwota(t,nw,w,u,i,rab=0):
    if rab>=0 and rab <= 35:
        return (nw+t)*(1-rab/100)+w+u+i
    else:
        return "podaj rabat mniejszy niż 36% lub większy od 0"

print("kwota do zapłaty",kwota(100,100,50,50,50),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,25),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,75),"zł")


print("***************************************")
rabs = [0,8,10,12,15,20,25,32,35]

@opis
def wielerabatow():
    wynik = []
    for r in rabs:
        kw = kwota(1700, 1230, 450, 200, 180, r)

        if r == 0:
            print("cena bazowa do zapłaty wynosi:", kw, "zł")

        else:
            print("dla rabatu:", r, "%, kwota do zapłaty wynosi:", kw, "zł")

        wynik.append(kw)

    print (wynik)
wielerabatow()

print("_______tablica z użyciem funckji anonimowej________")
result = [kwota(1700,1230,450,200,180,r) for r in rabs]
print(result)
