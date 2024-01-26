print("\n")
a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua : "))

if (a >= b):
    if (a > b):
        print(f"{a} lebih besar dari {b}")
    else:
        print(f"{a} sama dengan {b}")
else:
    print(f"{a} lebih kecil dari {b}")