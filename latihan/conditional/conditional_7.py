print("\n")
a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua : "))
c = int(input("Masukkan angka ketiga : "))

if (a >= b):
    if (c >= a):
        print(f"{c} lebih besar dari {a}, {a} lebih besar dari {b}")
    else:
        if (b >= c):
            print(f"{a} lebih besar dari {b}, {b} lebih besar dari {c}")
        else:
            print(f"{a} lebih besar dari {c}, {c} lebih besar dari {b}")
elif (b >= c):
    if (a >= b):
        print(f"{a} lebih besar dari {b}, {b} lebih besar dari {c}")
    else:
        if (a >= c):
            print(f"{b} lebih besar dari {a}, {a} lebih besar dari {c}")
        else:
            print(f"{b} lebih besar dari {c}, {c} lebih besar dari {a}")
elif (c >= a):
    if (b >= c):
        print(f"{b} lebih besar dari {c}, {c} lebih besar dari {a}")
    else:
        if (b >= a):
            print(f"{c} lebih besar dari {b}, {b} lebih besar dari {a}")
        else:
            print(f"{c} lebih besar dari {a}, {a} lebih besar dari {b}")