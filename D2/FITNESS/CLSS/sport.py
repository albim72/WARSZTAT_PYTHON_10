class Sport:

    def __init__(self,dyscyplina,lata_upr,zyciowka):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.zyciowka = zyciowka
        self.dysycyplina_przypisanie()
        
    def infosport(self):
        return f"{self.dyscyplina}, czas uprawiania [lata]: {self.lata_upr}, życiówka: {self.zyciowka}"

    def dysycyplina_przypisanie(self):
        print(f"przyspisanie do dyscypliny: {self.dyscyplina}")
