import math

#funkcja nr 1
n = 45
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c + n
    return n

print(policz(3,6,7,2))
print(n)


def zewnetrzna():
    x = "lokalne"
    def wewnetrzna():
        nonlocal x
        x = "nielokalne"
        print(f"wewnętrzne: {x}")
    wewnetrzna()
    print(f"zewnętrzna: {x}")


zewnetrzna()

#funkcja nr 3

def gx(n,m=1,k=3,b=5):
    return math.sqrt(n+m)*k - b

print(gx(3,2,6))
print(gx(3,2))
print(gx(3))

#wywołaj funkcję z wartościami n = 9, m zostaw domyślną, k=11
print(gx(9,k=11,b=2))


#funkcja nr 4

def ranking(l3,l2,l1):
    print(f'ranking języków programowania: pierwsze miejsce: {l1}, drugie: {l2}, trzecie: {l3}')

ranking("Java","C++","Python")

def rank(*lang,nrrank):
    print(f'ranking języków programowania: pierwsze miejsce: {lang[0]}, '
          f'drugie: {lang[1]}, trzecie: {lang[2]} - nr rankingu: {nrrank}, liczba języków: {len(lang)}')

rank("Java","C++","Python",nrrank=23)
rank("Java","Ruby","C++","Python","JavaScript",nrrank=27)


#funkcja lambda

print((lambda e:e**3)(4))

b = lambda u:u+90

print(b(8))

def px(u):
    return u+90

print(px(8))

h = lambda a,b,c=3:a/(b-c)

print(h(4,6,2))
print(h(4,6,56))
print(h(4,6))

def ob(k):
    return lambda a,b:a**k-b

print(ob(34)(5,3))

num = [67,2,5,177,-9,34,122,4,7,1,100,-4,0,5]

#stwórz listę nparz i przekaż do niej wszystkie wartości parzyste z listy num
#funkcja filter  standardowa wyższego rzędu -> parametrem 0 jest inna funkcja, 1 jest źrodło danych

nparz = list(filter(lambda x:x%2==0,num))
print(nparz)

#stwórz listę cube i przekaż do niej wszystkie wartości z listy num podniesione do potęgi 3

cube = list(map(lambda x:x**3,num))
print(cube)

def dodaj(x):
    return x + 3


trojka = list(map(dodaj,num))
print(trojka)


#własne funkcje wyższego rzędu

def filtrowanie(dane,test):
    plus = []
    for element in dane:
        if (test(element)):
            plus.append(element)
    return plus


def ekstra_liczba(n):
    return n >=100

mliczby = [119,0,-6,17,93,101,70,231]

print(filtrowanie(mliczby,ekstra_liczba))


def mapowanie(dane,transformacja):
    mapa = []
    for element in dane:
        mapa.append(transformacja(element))
    return mapa

def addFive(n):
    return n+5

print(mapowanie(mliczby,addFive))
