class Klub:

    def __init__(self,nr,nazwa,adres):
        self.nr = nr
        self.nazwa = nazwa
        self.adres = adres
        self.przypisanie()

    def infoklub(self):
        return f"klub {self.nazwa}, nr filii: {self.nr}"

    def przypisanie(self):
        print(f"przypisanie do klubu nr :{self.nr}")
