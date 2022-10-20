from tywin import Tywin
from tyrion import Tyrion
from cersei import Cersei

tyw = Tywin("Lannister","Lord","m",3,8,9)
tyr = Tyrion("Lannister","Lord","m",5,10,8)
cer = Cersei("Lannister","Queen","k",3,10,10)

print("_________ Lord Tywin ______________")
tyw.walka()
tyw.negocjacja()
tyw.uczta()

print("_________ Lord Tyrion ______________")
tyr.walka()
tyr.negocjacja()
tyr.uczta()

print("_________ Queen Cersei ______________")
cer.walka()
cer.negocjacja()
cer.uczta()

