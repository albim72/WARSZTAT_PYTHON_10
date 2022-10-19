class Book:

    #deklaracja stanu (dane) -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=10):
        self.idksiazki = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        #Book.create_book(self)
        #print("tworzenie nowej książki -> bez metody z komunikatem")
        self.create_book()


    #definicja zachowania - > funkcje klasy -> metody
    def create_book(self):
        print("tworzenie nowej książki")

    def print_book(self):
        print(f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}.")

    def rabat(self):
        return 0.05 * self.cena

    def setcena(self,nowacena):
        self.cena = nowacena




b1 = Book(35,"Wiedźmin","Andrzej Sapkowski",38)
b1.print_book()
#f-string
print(f'rabat: {b1.rabat():.2f} zł')

b1.setcena(43)
b1.print_book()
print(f'rabat: {b1.rabat():.2f} zł')


b2 = Book(44,"Hobbit","J.R.R. Tolkien",36)
b2.oprawa = "twarda"
b2.print_book()
print(f'rabat: {b2.rabat():.2f} zł')






