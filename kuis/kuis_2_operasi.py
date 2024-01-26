import os, time

def isValidPilgan(jawaban):
    kunci = ['A', 'a', 'B', 'b']
    lenKunci = len(kunci)
    retVal = False
    for i in range(lenKunci):
        if (jawaban == kunci[i]):
            retVal = True
    return retVal

def isTrue(jawaban, kunci, tipeSoal):
    return (jawaban.lower() == kunci)

clear = lambda: os.system('cls')

soal = [{"soal": "a = 17 % 6\nprint(a)"                                                 , "jawaban": '5', "tipe": "Isian"},
        {"soal": "a = 17 // 6\nprint(a)"                                                , "jawaban": '2', "tipe": "Isian"},
        {"soal": "a = 12\nb = 3\nc = a * b\nprint(c)"                                   , "jawaban": '36', "tipe": "Isian"},
        {"soal": "a = \"Andi\" == \"Andi\"\nprint(a)"                                   , "jawaban": 'a', "tipe": "Pilgan"},
        {"soal": "a = 1 != \"1\"\nprint(a)"                                             , "jawaban": 'a', "tipe": "Pilgan"},
        {"soal": "a = 8 - 4\nb = 4\nc = a > b\nprint(c)"                                , "jawaban": 'b', "tipe": "Pilgan"},
        {"soal": "a = 83 > 22\nb = 30 >= 31\nc = a and b\nprint(c)"                     , "jawaban": 'b', "tipe": "Pilgan"},
        {"soal": "z = (1 != 1) and (100 > 0)\nprint(z)"                                 , "jawaban": 'b', "tipe": "Pilgan"},
        {"soal": "umur = 16\nremaja = (umur > 12) and (umur >= 0)\nprint(remaja)"       , "jawaban": 'a', "tipe": "Pilgan"},
        {"soal": "kkm = 70\nnilaiAnda = 80\nlulus = (nilaiAnda - kkm) > 0\nprint(lulus)"    , "jawaban": 'a', "tipe": "Pilgan"}
        ]

# INISIALISASI QUIZ
input("Press any key to begin")
clear()

start_time = time.time()

for i in range(len(soal)):
    print(f"Apa hasil output (print) dari program ini\n\n{soal[i]['soal']}\n")
    if (soal[i]['tipe'] == 'Pilgan'):
        print("a. True\nb. False\n")
    jawaban = input("JAWABAN : ")
    while (not isTrue(jawaban, soal[i]['jawaban'], soal[i]['tipe'])):
        clear()
        if ((soal[i]['tipe'] == "Pilgan") and (not isValidPilgan(jawaban))):
            print("Masukan Anda salah. Pilih \"a\" atau \"b\"!\n")
        else:
            print("Jawaban Salah! Masukkan jawaban lagi!\n")
        print(f"Apa hasil output (print) dari program ini\n\n{soal[i]['soal']}\n")
        if (soal[i]['tipe'] == 'Pilgan'):
            print("a. True\nb. False\n")
        jawaban = input("JAWABAN : ")
    print("BENAR!\n")
    input("Press button to continue")
    clear()

end_time = time.time()

print(f'Execution time : {end_time-start_time} seconds')