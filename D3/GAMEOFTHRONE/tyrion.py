from rod import CzlonekRodu

class Tyrion(CzlonekRodu):

    def walka(self):
        if self.punkty_walki > self.punkty_palacowe and self.punkty_walki >=6:
            print("Lord wysłany do walki....")
        else:
            print("Lord pozostaje w pałacu")


    def negocjacja(self):
        if self.punkty_palacowe >= 8:
            print("Lord wysłany do negocjacji....")
        else:
            print("Lord wysłany do walki....")

    def uczta(self):
        if self.punkty_palacowe >= 6 and self.doswiadczenie >=7:
            print("Lord jedzie na ucztę...")
        else:
            print("Lord zostaje w pałacu...")
