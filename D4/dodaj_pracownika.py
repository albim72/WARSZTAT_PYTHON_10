import json

def dodaj_nowego_pracownika(new_data,klucz,filename = "pracownik.json"):
    with open(filename,"r+",encoding="utf-8") as file:
        file_data = json.load(file)
        file_data[klucz].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)


nowyprac = {
            "imie": "Jarosław",
            "nazwisko": "Kowal",
            "stanowisko": "informatyk",
            "lata_pracy": 8,
            "email": "jarek88@firma.pl"
        }

dodaj_nowego_pracownika(nowyprac,"pra_info")
