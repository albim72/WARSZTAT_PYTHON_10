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
