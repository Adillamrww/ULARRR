import random


# ======= VARIABEL =======


nama = str(input("Masukan Username: "))
passw = "B"
score = 0
kesempatan = 3


# ======= LOGIN =======


def login():
    global passw
    print(" ")
    print("Petunjuk PASSWORD: Huruf - Huruf Apa Yang Kedinginan")
    passwl = str(input("Masukan Password: "))
    print(" ")
    umur = int(input("Masukan umur: "))
    print(" ")
    
    if passwl != passw and umur < 16:
        print ("KABEH SALAH")
        login()
    elif passwl != passw:
        print ("USERNAME SALAH GOBLOK")
        login()
    elif umur < 16:
        print ("BOCIL DILARANG MAIN HARAMMMMMMM")
        login()
    else:
        lobby()
pass

def lobby():
    print("======= SELAMAT DATANG DI AMBATUPLAY =======")
    print("Silahkan pilih permainan yang akan dimainkan")
    print(" ")
    print("1. Tebak Angka")
    print("2. Tebak Kata")
    print(" ")
    
    pilihan = int(input("Masukan nomor permainan: "))
    
    if pilihan == 1:
        permainan()
    elif pilihan == 2:
        permainan2()
        

# ======= GAME 1 =======
    
    
def permainan():
    print ("====== Selamat Datang Di Permainan 1 ======")
    print ("=== Anda Harus Menebak Angka Dari 1-4 ===")
    print ("=========== Semoga Berhasil :) ==========")
    print(" ")
    angka = random.randint(1, 4)
    tebakan = int(input("Masukan Angka Tebakan Anda: "))
    
    if tebakan == angka:
        print("Selamat Anda Berhasil Menebak")
        scorePlus()
        Level2() 
    else:
        print("Anda Salah")
        if score >= 2:
            scoreNeg()
            
        ulangi = str(input("Apakah Anda Ingin Mengulanginya Lagi? [Y/N]: "))
        if ulangi == ("Y"):
            permainanRepeat()
        
        else:
            cetakScore()
            exit() 
pass

def Level2() :
    global kesempatan
    print ("======== Selamat Datang Di Level 2 =======")
    print ("Kali Ini Kamu Harus Menebak Angka Dari 1-8")
    print ("============ Semoga Berhasil =============")
    
    angka = random.randint(1, 8)
    while kesempatan > 0:
        tebakan = int(input("Masukkan Tebakan Anda : "))
        if tebakan == angka :
            print ("Selamat Anda Berhasil Menebak")
            scorePlus2() 
            Level3()
        elif tebakan > angka :
            print ("Anda Salah")
            print (f"Angka Yang Benar Kurang Dari {tebakan}")
            kesempatanNeg() 
            print (f"Kesempatan Anda Bersisa {kesempatan}")
        elif tebakan < angka :
            print ("Anda Salah")
            print (f"Angka Yang Benar Lebih Besar Dari {tebakan}")
            kesempatanNeg() 
            print (f"Kesempatan Anda Bersisa {kesempatan}")
        
    while kesempatan == 0 :
        scoreNeg2() 
        print ("Anda Telah Kehabisan Kesempatan")
        ulangi = str(input("Apakah Anda Ingin Mengulangi Dari Level 1? [Y/N]: "))
        if ulangi == ("Y"):
            kesempatan += 3
            permainanRepeat()
        else:
            cetakScore() 
            exit() 
pass

def Level3() :
    global kesempatan
    kesempatan = 5
    print ("======= Selamat Datang Di Level Terakhir ======")
    print ("Di Level Ini Anda Harus Menebak Dari Angka 1-25")
    print ("=============== Semoga Berhasil ===============")

    angka = random.randint(1, 25)
    while kesempatan > 0:
        tebakan = int(input("Masukkan Tebakan Anda: "))
        if tebakan == angka :
            print ("Selamat Anda Berhasil Menebak")
            print ("Anda Telah Memenangkan Permainan Tebak Angka")
            scorePlus3()
            menang()
        elif tebakan < angka :
            print ("Anda Salah")
            print (f"Angka Yang Benar Lebih Besar Dari {tebakan}")
            kesempatanNeg()
            print (f"Kesempatan Anda Bersisa {kesempatan}")
        elif tebakan > angka :
            print ("Anda Salah")
            print (f"Angka Yang Benar Kurang Dari {tebakan}")
            kesempatanNeg()
            print (f"Kesempatan Anda Bersisa {kesempatan}")
        
    while kesempatan == 0 :
            scoreNeg3()
            print ("Anda Telah Kehabisan Kesempatan")
            ulangi = str(input("Apakah Anda Ingin Mengulangi Dari Level 1? [Y/N]"))
            if ulangi == ("Y") :
                permainanRepeat()
            else :
                cetakScore()
                exit()
pass  

def permainanRepeat ():
    angka = random.randint(1, 4)
    print(" ")
    print (angka)
    tebakan = int(input("Masukan Angka Tebakan Anda: "))
    
    if tebakan == angka:
        print("Selamat Anda Berhasil Menebak")
        scorePlus()
        Level2()
        
    else:
        print("Anda Salah")
        if score >= 2:
            scoreNeg()
        
    ulangi = str(input("Apakah Anda Ingin Mengulanginya Lagi? [Y/N]: "))
    
    if ulangi == "Y":
        permainanRepeat()
    else:
        cetakScore()
        exit() 
pass


# ======= GAME 2 ========


def permainan2():
    print("==== Selamat datang di permainan 2 ====")
    print("=== Tebak Kata Mengenai Nama Hewan! ===")
    print(" ")
    

    kata = ['BYAN', 'NATHAN', 'ALI', 'VENVEN', 'CHRISTO', 'YOSUA', 'REZA', 'DANISH', 'AGHA', 'RIJALS', 
            'DICKAS', 'ALVINO', 'NABIL', 'LEXA', 'IBNU', 'JUPRI']
    soalKata = random.choice(kata)
    kesempatan = 3
    jawaban = ['_' for _ in soalKata]

    print(" ", " ", " ", " ".join(jawaban), " ")
    print(" ")
    print(" ", " ", f"Clue = {len(soalKata)} huruf" )

    while kesempatan > 0 and '_' in jawaban:
        tebakan = input("Masukkan huruf (kapital): ")

    if tebakan in soalKata:
        for i in range(len(soalKata)):
            if soalKata[i] == tebakan:
                print(" ")
                print(f"Kamu sudah menebak dengan huruf {tebakan}, cari huruf lain!")
                jawaban[i] = tebakan
    else:
        kesempatan -= 1
        print(" ")
        print(f"Huruf '{tebakan}' tidak ada. Kesempatan tersisa: {kesempatan}")

    print(" ", " ", " ", " ".join(jawaban), " ")

    if '_' not in jawaban:
        print("Selamat! Anda berhasil menebak kata:", soalKata)
    else:
        print("Anda kehabisan kesempatan. Kata yang benar adalah:", soalKata)


# ======= SCORE =======


def menang () :
    global score
    score += 100
    print (f"{nama} Telah Menang")
    cetakScore()
    exit()
pass
    
def cetakScore():
    print(" ")
    print(f"{nama} Score = {score}") 
pass

def kesempatanNeg() :
    global kesempatan
    kesempatan -= 1
    
def scorePlus():
    global score
    score += 10
    
def scoreNeg():
    global score
    score -= 2
 
def scorePlus2() :
    global score
    score += 15

def scoreNeg2() :
    global score
    score -= 5

def scorePlus3() :
    global score
    score += 20

def scoreNeg3() :
    global score
    score -= 10

login()