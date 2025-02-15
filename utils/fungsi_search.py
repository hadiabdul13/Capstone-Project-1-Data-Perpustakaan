from .fungsi_baca_data import read_data

def cari_peminjaman():

    from main_menu import peminjaman

    keyword = input("Masukkan nama peminjam atau judul buku: ").strip().lower()
    hasil = [p for p in peminjaman if keyword in p["Nama Peminjam"].lower() or keyword in p["Judul Buku"].lower()]
    read_data(hasil)