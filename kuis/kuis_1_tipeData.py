import os, time

def isValid(jawaban):
    kunci = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e']
    lenKunci = len(kunci)
    retVal = False
    for i in range(lenKunci):
        if (jawaban == kunci[i]):
            retVal = True
    return retVal
        

def isTrue(jawaban, kunci):
    return (jawaban.lower() == kunci)

clear = lambda: os.system('cls')

soal = [{"soal": "12"       , "jawaban": 'a'},
        {"soal": "7.5"      , "jawaban": 'b'},
        {"soal": "\'a\'"    , "jawaban": 'c'},
        {"soal": "\"Naura\"", "jawaban": 'd'},
        {"soal": "True"     , "jawaban": 'e'},
        {"soal": "8.0"      , "jawaban": 'b'},
        {"soal": "\'1\'"    , "jawaban": 'c'},
        {"soal": "\"123\""  , "jawaban": 'd'},
        {"soal": "\"False\"", "jawaban": 'd'},
        {"soal": "\"8.0\""  , "jawaban": 'd'}
        ]

# INISIALISASI QUIZ
input("Press any key to begin")
clear()

start_time = time.time()

for i in range(len(soal)):
    print(f"Apa tipe data dari\n\n{soal[i]['soal']}\n")
    print("a. Integer\nb. Float / Double\nc. Char\nd. String\ne. Boolean\n")
    jawaban = input("JAWABAN : ")
    while (not isTrue(jawaban, soal[i]['jawaban'])):
        clear()
        if (isValid(jawaban)):
            print("Jawaban Salah! Masukkan jawaban lagi!\n")
        else:
            print("Masukkan jawaban lagi!\n\nJawab dengan \"a\" atau \"b\" atau \"c\" atau \"d\" atau \"e\"\n")
        print(f"Apa tipe data dari\n\n{soal[i]['soal']}\n")
        print("a. Integer\nb. Float / Double\nc. Char\nd. String\ne. Boolean\n")
        jawaban = input("JAWABAN : ")
    print("BENAR!\n")
    input("Press button to continue")
    clear()

end_time = time.time()

print(f'Execution time : {end_time-start_time} seconds')