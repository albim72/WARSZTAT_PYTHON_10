n = 3

match n:
    case 2: print("n jest parzyste i wynosi 2")
    case 5: print("n jest nieparzyste i wynosi 5")
    case 9: print("n jest nieparzyste i wynosi 9")
    case other: print("wartość spoza zakresu")


if n>6:
    print("zakres górny")
elif n==6:
    print("granica zakresu")
else:
    print("zakres dolny")
