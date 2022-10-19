from bfunkcje import *

class CDane:

    def __init__(self,lista,dict):
        self.lista = lista
        self.dict = dict

    def czytaj_l(self):
        return czytaj(self.lista)

    def czytaj_d(self):
        return czytaj_dict(self.dict)
