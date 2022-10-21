class Moj_Dict(dict):

    def __missing__(self, key):
        return "brak klucza"
