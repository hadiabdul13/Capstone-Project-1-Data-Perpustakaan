from .fungsi_baca_data import read_data
def hapus_peminjaman():

    from main_menu import peminjaman
    from main_menu import recycle_bin    
    
    read_data(peminjaman)
    while True:
        id_peminjam = input("Masukkan ID Peminjam yang ingin dihapus: ").strip().upper()
        for pem in peminjaman:
            if pem["ID Peminjam"] == id_peminjam:
                recycle_bin.append(pem)
                peminjaman.remove(pem)
                print("Data peminjaman dipindahkan ke Recycle Bin.\n")

                if peminjaman:
                    print("Data peminjaman yang tersisa:")
                    read_data(peminjaman)
                else:
                    print("Semua data peminjaman telah dihapus!")

                return

        print("ID Peminjam tidak ditemukan! Silakan masukkan ID yang benar.")
        read_data(peminjaman)  # Menampilkan data yang masih ada sebelum meminta input lagi

def pulihkan_peminjaman():

    from main_menu import peminjaman
    from main_menu import recycle_bin    

    if not recycle_bin:
        print("Recycle Bin kosong. Tidak ada data untuk dipulihkan.")
        return
    read_data(recycle_bin)

    while True:
        id_peminjam = input("Masukkan ID Peminjam yang ingin dipulihkan: ").strip().upper()
        for pem in recycle_bin:
            if pem["ID Peminjam"] == id_peminjam:
                peminjaman.append(pem)
                recycle_bin.remove(pem)
                print("Data peminjaman berhasil dipulihkan.\n")
                print("Data peminjaman setelah pemulihan:")
                read_data(peminjaman)
                return
        print("ID Peminjam tidak ditemukan di Recycle Bin! Silakan masukkan ID yang benar.")