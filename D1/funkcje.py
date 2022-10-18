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

