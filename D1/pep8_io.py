marka = "Jeep"
model = "Cherokee"
rocznik = 2020

sam = "samochód -> marka:{}, rocznik:{}, model: {}."

print(sam.format(marka,rocznik,model))

sam = "samochód -> marka:{0}, model:{2}, rocznik: {1}."

print(sam.format(marka,rocznik,model))

#f-string
print(f"autokomis -> samochód marka: {marka}, model: {model}, rocznik: {rocznik}")


konkurs = [
    ("Jan",78),
    ("Anna",45),
    ("Olaf",12),
    ("Olga",89),
    ("Leon",75),
    ("Nadia",67)
]


print("____________________________________________________")
print(list(enumerate(konkurs)))

print("________________zestawienie wyników konkursowych_____________________")

for i,(imie,punkty) in enumerate(konkurs):
    print('nr %d: %-9s : %.1f punktów' %(i+1,imie,punkty))
