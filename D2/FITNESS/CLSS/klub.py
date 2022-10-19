class Klub:
    
    def __init__(self,nr,nazwa,adres):
        self.nr = nr
        self.nazwa = nazwa
        self.adres = adres
        
    def infoklub(self):
        return f"klub {self.nazwa}, nr filii: {self.nr}"
