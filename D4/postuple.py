#moja wersja krotki, która będzie czytała listę argumentów konstruktora definiowanej klasy
# i będzie pobierała jako swoje wartości tylko liczby nieujemne
#dodatkową funkcjonalnością będzie zliczanie wartości odrzuconych

class PositiveNumberTuple(tuple):

    def __new__(cls, *numbers):
        skipped_values_count = 0
        positive_numbers = []
        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped_values_count += 1

        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_values_count = skipped_values_count
        return instance

pos = PositiveNumberTuple(-9,0,23,4,5,6,-1,0,34,5,7,6,-100)
print(pos)
print(type(pos))
print(pos.skipped_values_count)
