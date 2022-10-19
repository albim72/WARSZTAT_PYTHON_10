class Klub:

    def __init__(self,nr_kb,nazwa_kb,adres):
        self.nr = nr_kb
        self.nazwa = nazwa_kb
        self.adres = adres
        self.przypisanie()

    def infoklub(self):
        return f"klub {self.nazwa}, nr filii: {self.nr}"

    def przypisanie(self):
        print(f"przypisanie do klubu nr :{self.nr}")
