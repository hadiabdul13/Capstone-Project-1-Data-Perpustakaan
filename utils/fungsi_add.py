from .fungsi_baca_data import read_data, read_stok_buku
from .fungsi_validasi import validasi_input_alfabet, validasi_input_angka, validasi_tanggal
from utils.fungsi_create_data import membuat_id_peminjam, membuat_id_buku

def tambah_peminjaman(data):
    from main_menu import stok_buku 

    id_peminjam = membuat_id_peminjam().upper()
    nama_peminjam = validasi_input_alfabet('Masukkan nama peminjam: ').strip()
    read_stok_buku()

    while True:
        while True:
            id_buku = input('Masukkan ID Buku yang ingin dipinjam: ').strip().upper()
            buku_ditemukan = None
            for buku in stok_buku:
                if buku["ID Buku"] == id_buku:
                    buku_ditemukan = buku
                    break
            if buku_ditemukan:
                break
            else:
                print("\nID Buku tidak ditemukan! Masukkan ID yang benar.")

        while True:
            jumlah_buku = validasi_input_angka('Masukkan jumlah buku: ')
            if buku_ditemukan["Stok"] >= jumlah_buku:
                buku_ditemukan["Stok"] -= jumlah_buku
                break
            else:
                print("\nStok tidak mencukupi! Masukkan jumlah yang sesuai.")

        tanggal_peminjaman = None
        while not tanggal_peminjaman:  # This will keep looping until a valid date is entered
            tanggal_peminjaman = validasi_tanggal().strip().upper()
            if not tanggal_peminjaman:
                print("\nTanggal tidak valid! Masukkan format yang benar (DD-MM-YYYY).")

        data.append({
            'ID Peminjam': id_peminjam,
            'Nama Peminjam': nama_peminjam,
            'ID Buku': id_buku,
            'Judul Buku': buku_ditemukan["Judul Buku"],
            'Jumlah Buku': jumlah_buku,
            'Tanggal Peminjaman': tanggal_peminjaman
        })
        print("\nPeminjaman berhasil dicatat!")

        # Ask if the user wants to borrow another book
        while True:
            lanjut = input("Tambah buku lain? (ya/tidak): ").strip().lower()
            if lanjut in ['ya', 'tidak']:
                break
            print("Input tidak valid! Masukkan 'ya' atau 'tidak'.")

        if lanjut == 'tidak':
            break

    read_data(data)

def tambah_stok_buku():

    from main_menu import stok_buku

    print("")
    print("\n----- TAMBAH STOK BUKU -----")
    judul_buku = input("Masukkan judul buku yang akan ditambahkan: ").strip()
    penulis = validasi_input_alfabet("Masukkan Nama Penulis: ").strip()

    jumlah_tambahan = validasi_input_angka("Masukkan Jumlah Stok Tambahan: ")

    # Cek apakah buku sudah ada dalam stok
    for buku in stok_buku:
        if buku["Judul Buku"].lower() == judul_buku.lower() and buku["Penulis"].lower() == penulis.lower():
            buku["Stok"] += jumlah_tambahan
            print(f"/nStok buku '{buku['Judul Buku']}' berhasil ditambahkan sebanyak {jumlah_tambahan}!")
            return

    # Jika buku baru, membuat ID baru dan menambahkan ke stok
    id_buku_baru = membuat_id_buku()
    stok_buku.append({
        "ID Buku": id_buku_baru,
        "Judul Buku": judul_buku,
        "Penulis": penulis,
        "Stok": jumlah_tambahan
    })
    print(f"/nBuku baru '{judul_buku}' oleh {penulis} berhasil ditambahkan dengan ID {id_buku_baru} dan stok berjumlah {jumlah_tambahan}!")
    read_stok_buku()