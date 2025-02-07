from tabulate import tabulate
import random
import string

print("----- Data Peminjaman Buku di Perpustakaan Daerah -----")

# Simpan data peminjaman buku dan stok buku
data_peminjaman = []
stok_buku = [
    {"ID Buku": "B001", "Judul Buku": "Laskar Pelangi", "Penulis": "Andrea Hirata", "Stok": 5},
    {"ID Buku": "B002", "Judul Buku": "Bumi Manusia", "Penulis": "Pramoedya Ananta Toer", "Stok": 3},
    {"ID Buku": "B003", "Judul Buku": "Perahu Kertas", "Penulis": "Dee Lestari", "Stok": 4},
    {"ID Buku": "B004", "Judul Buku": "Ayat-Ayat Cinta", "Penulis": "Habiburrahman El Shirazy", "Stok": 6},
    {"ID Buku": "B005", "Judul Buku": "Negeri 5 Menara", "Penulis": "Ahmad Fuadi", "Stok": 4},
    {"ID Buku": "B006", "Judul Buku": "Dilan 1990", "Penulis": "Pidi Baiq", "Stok": 7},
    {"ID Buku": "B007", "Judul Buku": "Supernova", "Penulis": "Dee Lestari", "Stok": 5},
    {"ID Buku": "B008", "Judul Buku": "Ronggeng Dukuh Paruk", "Penulis": "Ahmad Tohari", "Stok": 3},
    {"ID Buku": "B009", "Judul Buku": "Cantik Itu Luka", "Penulis": "Eka Kurniawan", "Stok": 4},
    {"ID Buku": "B010", "Judul Buku": "Rectoverso", "Penulis": "Dee Lestari", "Stok": 6}
]

def generate_id_peminjam():
    """Membuat ID unik untuk setiap peminjam."""
    return 'P' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def read_data(data):
    if not data:
        print("Tidak ada data peminjaman buku.")
    else:
        print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

def read_stok_buku():
    print("\n----- Daftar Stok Buku -----")
    print(tabulate(stok_buku, headers='keys', tablefmt='fancy_grid'))

def validasi_input_alfabet(prompt):
    while True:
        inputan = input(prompt).strip()
        if inputan.replace(" ", "").isalpha():
            return inputan
        else:
            print('Input harus berupa huruf.')

def validasi_input_angka(prompt):
    while True:
        inputan = input(prompt).strip()
        if inputan.isdigit():
            return int(inputan)
        else:
            print('Input harus berupa angka.')

def tambah_peminjaman(data):
    id_peminjam = generate_id_peminjam()
    nama_peminjam = validasi_input_alfabet('Masukkan nama peminjam: ')
    read_stok_buku()
    peminjaman_baru = []
    while True:
        id_buku = input('Masukkan ID Buku yang ingin dipinjam: ').strip()
        jumlah_buku = validasi_input_angka('Masukkan jumlah buku yang ingin dipinjam: ')
        tanggal_peminjaman = input('Masukkan tanggal peminjaman (DD-MM-YYYY): ').strip()
        
        for buku in stok_buku:
            if buku["ID Buku"] == id_buku:
                if buku["Stok"] >= jumlah_buku:
                    buku["Stok"] -= jumlah_buku
                    peminjaman_baru.append({
                        'ID Peminjam': id_peminjam,
                        'Nama Peminjam': nama_peminjam,
                        'ID Buku': id_buku,
                        'Judul Buku': buku["Judul Buku"],
                        'Jumlah Buku': jumlah_buku,
                        'Tanggal Peminjaman': tanggal_peminjaman
                    })
                    print("Peminjaman berhasil dicatat!")
                else:
                    print("Stok buku tidak mencukupi.")
                    continue
        
        lanjut = input("Apakah ingin meminjam buku lain? (ya/tidak): ").strip().lower()
        if lanjut != 'ya':
            break
    data.extend(peminjaman_baru)
    read_data(data)
    print("Terima kasih. Di atas adalah daftar buku yang Anda pinjam")

def main():
    while True:
        print('\n----- MENU PEMINJAMAN BUKU -----')
        print("")
        print("")
        print('1. Masukkan data buku yang ingin dipinjam')
        print('2. Periksa Data Peminjaman')
        print('3. Periksa Stok Buku')
        print('4. Perbarui Data Peminjaman')
        print('5. Tambah Stok Buku')
        print('6. Keluar')
        print('Pilih angka 1-6 untuk menginput data')
        pilihan = validasi_input_angka('Masukkan pilihan: ')
        
        if pilihan == 1:
            tambah_peminjaman(data_peminjaman)
        elif pilihan == 2:
            read_data(data_peminjaman)
        elif pilihan == 3:
            read_stok_buku()
        elif pilihan == 4:
            perbarui_peminjaman(data_peminjaman)
        elif pilihan == 5:
            tambah_stok_buku()
        elif pilihan == 6:
            print("Terima kasih telah menggunakan sistem peminjaman buku!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

main()
