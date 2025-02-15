print("""
============ SISTEM ADMINISTRASI PEMINJAMAN BUKU ============

Selamat datang di Sistem Administrasi Peminjaman Buku!
Sistem ini digunakan oleh petugas perpustakaan untuk mencatat, mengelola, dan memantau peminjaman buku di perpustakaan.
""")

from utils import fungsi_add as fd, fungsi_baca_data as fb, fungsi_create_data as fc, fungsi_search as fs, fungsi_update as fu, fungsi_validasi as fv, fungsi_restore as fr

# Data Peminjaman
peminjaman = [
    {"ID Peminjam": "P12345", "Nama Peminjam": "Budi Santoso", "ID Buku": "B001", "Judul Buku": "Laskar Pelangi", "Jumlah Buku": 1, "Tanggal Peminjaman": "01-02-2025"},
    {"ID Peminjam": "P67890", "Nama Peminjam": "Siti Aminah", "ID Buku": "B002", "Judul Buku": "Bumi Manusia", "Jumlah Buku": 2, "Tanggal Peminjaman": "03-02-2025"},
    {"ID Peminjam": "P23456", "Nama Peminjam": "Andi Wijaya", "ID Buku": "B003", "Judul Buku": "Ayat-Ayat Cinta", "Jumlah Buku": 1, "Tanggal Peminjaman": "05-02-2025"},
    {"ID Peminjam": "P34567", "Nama Peminjam": "Rina Kartika", "ID Buku": "B004", "Judul Buku": "Dilan 1990", "Jumlah Buku": 1, "Tanggal Peminjaman": "06-02-2025"},
    {"ID Peminjam": "P45678", "Nama Peminjam": "Joko Supriyanto", "ID Buku": "B005", "Judul Buku": "Negeri 5 Menara", "Jumlah Buku": 2, "Tanggal Peminjaman": "07-02-2025"},
    {"ID Peminjam": "P56789", "Nama Peminjam": "Dewi Lestari", "ID Buku": "B006", "Judul Buku": "Supernova", "Jumlah Buku": 1, "Tanggal Peminjaman": "08-02-2025"},
    {"ID Peminjam": "P67891", "Nama Peminjam": "Teguh Prasetyo", "ID Buku": "B007", "Judul Buku": "Ronggeng Dukuh Paruk", "Jumlah Buku": 1, "Tanggal Peminjaman": "09-02-2025"},
    {"ID Peminjam": "P78912", "Nama Peminjam": "Maya Sari", "ID Buku": "B008", "Judul Buku": "Perahu Kertas", "Jumlah Buku": 2, "Tanggal Peminjaman": "10-02-2025"},
    {"ID Peminjam": "P89123", "Nama Peminjam": "Fajar Hidayat", "ID Buku": "B009", "Judul Buku": "Anak Semua Bangsa", "Jumlah Buku": 1, "Tanggal Peminjaman": "11-02-2025"},
    {"ID Peminjam": "P91234", "Nama Peminjam": "Lisa Marlina", "ID Buku": "B010", "Judul Buku": "Cantik Itu Luka", "Jumlah Buku": 1, "Tanggal Peminjaman": "12-02-2025"},
    {"ID Peminjam": "P10234", "Nama Peminjam": "Rahmat Saputra", "ID Buku": "B011", "Judul Buku": "Laut Bercerita", "Jumlah Buku": 2, "Tanggal Peminjaman": "13-02-2025"}
]

# Data Stok Buku
stok_buku = [
    {"ID Buku": "B001", "Judul Buku": "Laskar Pelangi", "Penulis": "Andrea Hirata", "Stok": 5},
    {"ID Buku": "B002", "Judul Buku": "Bumi Manusia", "Penulis": "Pramoedya Ananta Toer", "Stok": 3},
    {"ID Buku": "B003", "Judul Buku": "Perahu Kertas", "Penulis": "Dee Lestari", "Stok": 4},
    {"ID Buku": "B004", "Judul Buku": "Pride and Prejudice", "Penulis": "Jane Austen", "Stok": 6},
    {"ID Buku": "B005", "Judul Buku": "To Kill a Mockingbird", "Penulis": "Harper Lee", "Stok": 4},
    {"ID Buku": "B006", "Judul Buku": "Pemrograman Python untuk Pemula", "Penulis": "Budi Raharjo", "Stok": 5},
    {"ID Buku": "B007", "Judul Buku": "Belajar Java dalam 7 Hari", "Penulis": "Abdul Kadir", "Stok": 4},
    {"ID Buku": "B008", "Judul Buku": "Pemrograman Web dengan HTML, CSS, dan JavaScript", "Penulis": "Jubilee Enterprise", "Stok": 3},
    {"ID Buku": "B009", "Judul Buku": "Database MySQL untuk Pemula", "Penulis": "Jubilee Enterprise", "Stok": 2},
    {"ID Buku": "B010", "Judul Buku": "Algoritma dan Pemrograman dengan Python", "Penulis": "Dian Wahyu", "Stok": 5}
]

recycle_bin = []

def perpustakaan ():
    while True:
        print("")
        print('1. Tambah Peminjaman')
        print('2. Periksa Data Peminjaman')
        print('3. Periksa Stok Buku')
        print('4. Tambah Stok Buku')
        print('5. Perbarui Data Peminjaman')
        print('6. Hapus Peminjaman (Recycle Bin)')
        print('7. Pulihkan Data dari Recycle Bin')
        print('8. Cari Data Peminjaman')
        print('9. Pengembalian Pinjaman')
        print('10. Keluar')
        print("")
        pilihan = fv.validasi_input_angka('Masukkan pilihan (1-10): ')

        if pilihan == 1:
            fd.tambah_peminjaman(peminjaman)
        elif pilihan == 2:
            fb.read_data(peminjaman)
        elif pilihan == 3:
            fb.read_stok_buku()
        elif pilihan == 4:
            fd.tambah_stok_buku()
        elif pilihan == 5:
            fu.perbarui_peminjaman()
        elif pilihan == 6:
            fr.hapus_peminjaman()
        elif pilihan == 7:
            fr.pulihkan_peminjaman()
        elif pilihan == 8:
            fs.cari_peminjaman()
        elif pilihan == 9:
            fu.pengembalian_pinjaman()
        elif pilihan == 10:
            print("\nTerima kasih sudah menggunakan sistem administrasi peminjaman perpustakaan!")
            break
        else:
            print("\nPilihan tidak valid, coba lagi.")

perpustakaan ()
# Untuk menjalankan fungsi perpustakaan