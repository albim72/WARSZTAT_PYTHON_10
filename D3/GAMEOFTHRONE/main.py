from tywin import Tywin
from tyrion import Tyrion

tyw = Tywin("Lannister","Lord","m",3,8,9)
tyr = Tyrion("Lannister","Lord","m",5,10,8)

print("_________ Lord Tywin ______________")
tyw.walka()
tyw.negocjacja()
tyw.uczta()

print("_________ Lord Tyrion ______________")
tyr.walka()
tyr.negocjacja()
tyr.uczta()
