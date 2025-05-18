import time
import sys


# ============= LOADING ================


def loading(durasi):
    print("Sedang diproses.. ", end='', flush = True)
    time.sleep(durasi)
    print("\r" + " " * 20 + "\r")
pass


# ============= DATA ================


toko = {
    "tentang": {
        "nama": "TOKO MAS AMBA",
        "jam buka": "8.00 - 21.00",
        "kontak": "087654321",
        "tentang kami": "Toko kami menjual hp flagship dari tiap tiap brand hp yang resmi di Indonesia"
    },

    "produk": {
        "samsul": 24,
        "oddo": 19,
        "siomi": 10,
        "pipo": 15,
        "onfonix": 5
    },

    "pelanggan": {
        
    }
}

print()


# ============= ABOUT ================


def menuTentang():
    for key, value in toko["tentang"].items():
        print(f"{key.title()}: {value}")
    print()
    menu()
pass


# ============= PRODUK ================


def menuProduk():
    print (" ========== PRODUK ========== ")
    print ("1. Tambah Produk")
    print ("2. Info Produk")
    print ("3. Hapus Produk")
    print ("4. Menu")
    print()
    opsi = int(input("Opsi: "))
    if opsi == 1:
        tambahProduk()
    elif opsi == 2:
        infoProduk()
    elif opsi == 3:
        hapusPelanggan()
    elif opsi == 4:
        menu()
pass

def tambahProduk():
    jumlah = int(input("Masukan jumlah produk yang ingin ditambahkan"))
    
    for i in range(jumlah):
        print(f"\nData Produk ke-{i+1}")
        nama = input("Masukan nama produk :")
        harga = input("Masukan harga produk: ")
        toko["produk"] = {
            nama: harga
        }
    print("\n✅ Data Produk berhasil ditambahkan!")
    menuProduk()
pass

def infoProduk():
    print("\n ===== DAFTAR PRODUK ===== ")
    if not toko["produk"]:
        print("Belum ada produk yang terdaftar.")
    else:
        for produk, data in toko["produk"].items():
            print(f"{produk} : {data}")
    print()
    menuPelanggan()
pass

# def hapusProduk():
    
# pass

# ============= PELANGGAN ================


def menuPelanggan():
    print (" ========== PELANGGAN ========== ")
    print ("1. Tambah pelanggan")
    print ("2. Info pelanggan")
    print ("3. Hapus pelanggan")
    print ("4. Menu")
    print()
    opsi = int(input("Opsi: "))
    if opsi == 1:
        tambahPelanggan()
    elif opsi == 2:
        infoPelanggan()
    elif opsi == 3:
        hapusPelanggan()
    elif opsi == 4:
        menu()
pass

def tambahPelanggan():
    print("\n=== TAMBAH PELANGGAN ===")
    jumlah = int(input("Berapa pelanggan yang ingin ditambahkan: "))
    
    for i in range(jumlah):
        print(f"\nData Pelanggan ke-{i+1}")
        nama = input("Nama Pelanggan: ")
        no_hp = input("No. HP: ")
        merk_hp = input("Merk HP yang dibeli: ")
        
        # Generate ID unik (misal: P001, P002, dst)
        id_pelanggan = f"P{len(toko['pelanggan']) + 1:04d}"
        
        # Tambahkan ke dictionary pelanggan
        toko['pelanggan'][id_pelanggan] = {
            "nama": nama,
            "no_hp": no_hp,
            "merk_hp": merk_hp
        }
    
    print("\n✅ Data pelanggan berhasil ditambahkan!")
    menuPelanggan()
pass

def infoPelanggan():
     print("\n ===== DAFTAR PELANGGAN ===== ")
     if not toko["pelanggan"]:
        print("Belum ada pelanggan yang terdaftar.")
     else:
        for id_pelanggan, data in toko["pelanggan"].items():
            print(f"\nID Pelanggan: {id_pelanggan}")
            for key, value in data.items():
                print(f"{key.title()}: {value.title()}")
     print()
     menuPelanggan()
pass

def hapusPelanggan():
    print("\n=== HAPUS PELANGGAN (BERDASARKAN NAMA) ===")
    
    if not toko["pelanggan"]:  # jika tidak ada pelanggan
        input("\nTekan Enter untuk kembali...")
        menuPelanggan()
        return
    
    nama_hapus = input("\nMasukkan nama pelanggan yang ingin dihapus: ").strip().title()
    
    # cari semua ID yang memiliki nama sesuai input
    pelanggan_ditemukan = {
        id_pelanggan: data 
        for id_pelanggan, data in toko["pelanggan"].items() 
        if data["nama"].title() == nama_hapus
    }
    
    if not pelanggan_ditemukan:
        print(f"\n❌ Tidak ada pelanggan dengan nama '{nama_hapus}'")
    else:
        # tampilkan semua pelanggan dengan nama tersebut
        print(f"\nDitemukan {len(pelanggan_ditemukan)} pelanggan:")
        for id_pelanggan, data in pelanggan_ditemukan.items():
            print(f"\nID: {id_pelanggan}")
            for key, value in data.items():
                print(f"{key.title()}: {value}")
        
        # jika hanya ada 1, langsung konfirmasi
        if len(pelanggan_ditemukan) == 1:
            id_hapus = next(iter(pelanggan_ditemukan.keys()))
            konfirmasi = input(f"\nHapus pelanggan {id_hapus}? (y/t): ").lower()
            if konfirmasi == 'y':
                del toko["pelanggan"][id_hapus]
                print("\n✅ Pelanggan berhasil dihapus!")
        
        # jika lebih dari 1, minta ID
        else:
            id_hapus = input("\nMasukkan ID pelanggan yang ingin dihapus: ").upper()
            if id_hapus in pelanggan_ditemukan:
                del toko["pelanggan"][id_hapus]
                print("\n✅ Pelanggan berhasil dihapus!")
            else:
                print("\n❌ ID tidak valid atau tidak sesuai dengan nama")
    
    input("\nTekan Enter untuk kembali ke menu...")
    menuPelanggan()
    
    
# ============= MENU ================


def dongo():
    opsi = int(input("Masukan opsi dari 1-3: "))
    if opsi == 1:
        menuTentang()
        print()
    elif opsi == 3:
        menuPelanggan()
        print()
    else:
        dongo()
        print()
pass

def menu():
    print(" ===== SELAMAT DATANG DI TOKO MAS AMBA ===== ")
    print("1. Tentang toko")
    print("2. Info Produk")
    print("3. Info pelanggan")
    print()
    
    opsi = int(input("Opsi: "))
    
    loading(1)
    
    if opsi == 1:
        menuTentang()
        print()
    elif opsi == 2:
        menuProduk()
        print()
    elif opsi == 3:
        menuPelanggan()
        print()
    else:
        dongo()
        print()
pass

menu()