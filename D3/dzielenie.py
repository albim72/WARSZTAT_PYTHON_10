def dziel(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("dzielenie przez 0!")
    except NameError:
        print("zmienne niezdefiniowane")
    except TypeError:
        print("wykonuj obliczenia tylko na liczbach!")
    else:
        print(f"wynik = {wynik}")
    finally:
        print("policzmy coś jeszcze")

try:
    dziel(4,5)
    dziel(4,0)
    dziel(0,0)
    dziel(23,1.6756)
    dziel(5,False)
    dziel("fsdfaaddf",67)

    dziel(88)
except TypeError:
    print("zbyt mało argumentów - podaj dwie wartości numbers")
