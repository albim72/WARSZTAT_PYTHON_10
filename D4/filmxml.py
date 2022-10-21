import xml.sax
class UchwytFilmu(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.id = ""
        self.tytul = ""
        self.rok = ""
        self.kraj = ""
        self.czas_t = ""
        self.gatunek = ""

    #funkcja predefinowana klasy ContentHandler -> startElement
    def startElement(self,tag,attributes):
        self.CurrentData = tag
        if tag == "film":
            print("_____________film_______________")

    # funkcja predefinowana klasy ContentHandler -> endElement
    def endElement(self,tag):
        if self.CurrentData == "idfilmu":
            print(f"identyfikator filmu: {self.id}")
        elif self.CurrentData == "tytul":
            print(f"tytuł filmu: {self.tytul}")
        elif self.CurrentData == "rok":
            print(f"rok produkcji filmu: {self.rok}")
        elif self.CurrentData == "kraj":
            print(f"kraj produkcji filmu: {self.kraj}")
        elif self.CurrentData == "czas_trwania":
            print(f"czas trwania filmu [min]: {self.czas_t}")
        elif self.CurrentData == "gatunek":
            print(f"gatunek filmu: {self.gatunek}")

    # funkcja predefinowana klasy ContentHandler -> characters
    def characters(self,content):
        if self.CurrentData == "id_filmu":
            self.id = content
        elif self.CurrentData == "tytul":
            self.tytul = content
        elif self.CurrentData == "rok":
            self.rok = content
        elif self.CurrentData == "kraj":
            self.kraj = content
        elif self.CurrentData == "czas_trwania":
            self.czas_t = content
        elif self.CurrentData == "gatunek":
            self.gatunek = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)

handler = UchwytFilmu()
parser.setContentHandler(handler)
parser.parse("filmy.xml")
