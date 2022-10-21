from xml.etree.ElementTree import Element, SubElement, Comment
import xml.etree.ElementTree as ET
from prettyfy import pretty


top = Element("autokomis")


s1 = SubElement(top,'samochod')

id = SubElement(s1,'id')
id.text = 'sam1'

marka = SubElement(s1,'marka')
marka.text = 'Subaru'

model = SubElement(s1,'model')
model.text = 'Impreza'

poj = SubElement(s1,'poj')
poj.text = '2.0'

cena = SubElement(s1,'cena')
cena.text = '34000'

wyp_dod = SubElement(s1,'wyposazenie_dod')
kolor = SubElement(wyp_dod,"kolor")
kolor.text = 'czarna perła'
pod = SubElement(wyp_dod,'poduszki')
pod.text = '2'

#drugi samochód

s2 = SubElement(top,'samochod')

id = SubElement(s2,'id')
id.text = 'sam2'

marka = SubElement(s2,'marka')
marka.text = 'Subaru'

model = SubElement(s2,'model')
model.text = 'Outback'

poj = SubElement(s2,'poj')
poj.text = '2.4'

cena = SubElement(s2,'cena')
cena.text = '88900'

wyp_dod = SubElement(s2,'wyposazenie_dod')
kolor = SubElement(wyp_dod,"kolor")
kolor.text = 'crimson'
klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'KM664'


print(pretty(top))
zapis = open("subaru_komis.xml","a",encoding="utf-8")
zapis.write(pretty(top))
zapis.close()
