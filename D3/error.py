try:
    #x=90
    print(x)
except NameError:
    print("x nie jest zdefiniowany")
except TypeError:
    print("niewłaściwa wartość")
except:
    print("nieokreślony błąd")
else:
    print("x istnieje!")
finally:
    y = 9
    print(f'y = {y}')


print("ciąg dalszy")


