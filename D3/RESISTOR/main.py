from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

print("______________________________________")
print("klasa OldResistor")
r0 = OldResistor(10.2E2)
print(r0)
print(r0._ohms)
r0._ohms = 2.88E3
print(r0._ohms)

r0.set_ohms(3.33E2)

print(r0.get_ohms())
print("______________________________________")
print("klasa Resistor")
r1 = Resistor(50E3)
r1.ohms = 10E3

print(f'układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A')

print("______________________________________")
print("klasa VoltageResistance")

r2 = VoltageResistance(1E3)
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 25
print(f'natężenie prądu: {r2.current} A')

print(f'napięcie: {r2.voltage} V')


print("______________________________________")
print("klasa BoundedResistance")

try:
      r3 = BoundedResistance(1E2)
      r3.ohms = 12
      print(f'oporność: {r3.ohms}')
except ValueError as d:
      print(str(d))
except:
      print('Wsytąpił błąd w kodzie wywołującym!')

print("czy program działa???")

