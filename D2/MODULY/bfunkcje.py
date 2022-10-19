def czytaj(lista):
    for j,i in enumerate(lista):
        print(f"Element listy nr {j+1} -> {i}")

def czytaj_dict(dict):
    for x,y in dict.items():
        print(f"klucz -> {x} : wartość -> {y}")
