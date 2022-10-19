#prosty generator

def liczby():
    for i in range(11):
        yield i*2


for p in liczby():
    print(p)

print(type(liczby()))


#rozwiązanie hybrydowe

def wznowienie(n,k):
    print("wstrzymanie działania")
    yield 1001
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n*k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n**k
    print("wznowienie działania")

for i in wznowienie(3,4):
    if i == 1001:
        continue
    print(f"zwrócono wartość: {i}")

#generator z return

def genret():
    for i in range(5):
        if i==3:
            print("przerwanie")
            return
        else:
            yield i

for x in genret():
    print(x)

#generator złozony
def complexgen():
    x = 0
    while True:
        y = yield x
        if y is None:
            x = x+1
        else:
            x=y


g = complexgen()

print(next(g))
print(next(g))
print(next(g))
print(g.send(121))
print(next(g))
print(next(g))
print(next(g))
