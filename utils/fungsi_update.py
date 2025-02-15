from .fungsi_baca_data import read_data
from .fungsi_validasi import validasi_id_buku, validasi_input_angka, validasi_tanggal

# def perbarui_peminjaman():

#     from main_menu import peminjaman
    
#     read_data(peminjaman)

#     while True:
#         id_peminjam = input("Masukkan ID Peminjam yang ingin diperbarui: ").strip().upper()

#         for data in peminjaman:
#             if data['ID Peminjam'] == id_peminjam:
#                 print("Data ditemukan. Silakan pilih data yang ingin diperbarui.")

#                 from main_menu import peminjaman
#                 from main_menu import stok_buku

#                 while True:
#                     pembaruan = input("Masukkan data yang ingin diperbarui (Nama Peminjam, Judul Buku, Jumlah Buku, Tanggal Peminjaman). Ketik 'selesai' untuk keluar: ").strip().title()
#                     if pembaruan == "Selesai":
#                         print("Perbaruan selesai")
#                         read_data(peminjaman)
#                         return

#                     if pembaruan in ["Nama Peminjam", "Judul Buku", "Jumlah Buku", "Tanggal Peminjaman"]:
#                         if pembaruan == "Judul Buku":
#                             while True:
#                                 id_buku_baru = validasi_id_buku('Mengganti judul buku, berarti mengganti buku yang ingin dipinjam. Masukkan ID buku baru yang ingin dipinjam: ')
#                                 read_data(stok_buku)        
#                                 for buku in stok_buku:
#                                     if buku["ID Buku"] == id_buku_baru:
#                                         data["ID Buku"] = id_buku_baru
#                                         data["Judul Buku"] = buku["Judul Buku"]
#                                         break
#                                 else:
#                                     print("ID Buku tidak ditemukan! Silakan masukkan ID yang benar.")
#                                     continue  # Minta input ID lagi jika salah
#                                 break
#                         elif pembaruan == "Jumlah Buku":
#                             data[pembaruan] = validasi_input_angka("Masukkan jumlah buku baru: ")
#                         elif pembaruan == "Tanggal Peminjaman":
#                             data[pembaruan] = validasi_tanggal()
#                         else:
#                             data[pembaruan] = input(f"Masukkan {pembaruan} baru: ").strip()

#                         print(f"{pembaruan} berhasil diperbarui!")
#                     else:
#                         print("Kolom tidak valid. Gunakan: Nama Peminjam, Judul Buku, Jumlah Buku, Tanggal Peminjaman.")
#                 return

#         print("ID Peminjam tidak ditemukan! Silakan masukkan ID yang benar.")


def perbarui_peminjaman():
    from main_menu import peminjaman, stok_buku

    read_data(peminjaman)  # Load the latest peminjaman data

    while True:
        id_peminjam = input("Masukkan ID Peminjam yang ingin diperbarui: ").strip().upper()

        # Cek apakah ID peminjam ada dalam data peminjaman
        data_peminjam = None
        for data in peminjaman:
            if data['ID Peminjam'] == id_peminjam:
                data_peminjam = data
                break  # Stop loop when found

        if data_peminjam:
            print("Data ditemukan. Silakan pilih data yang ingin diperbarui.")
            break
        else:
            print("ID Peminjam tidak ditemukan! Silakan coba lagi.")

    while True:
        pembaruan = input("Masukkan data yang ingin diperbarui (Nama Peminjam, Judul Buku, Jumlah Buku, Tanggal Peminjaman). Ketik 'selesai' untuk keluar: ").strip().title()

        if pembaruan.lower() == "selesai":
            print("Perbaruan selesai.")
            read_data(peminjaman)  # Simpan perubahan
            return

        if pembaruan not in ["Nama Peminjam", "Judul Buku", "Jumlah Buku", "Tanggal Peminjaman"]:
            print("Kolom tidak valid. Gunakan: Nama Peminjam, Judul Buku, Jumlah Buku, Tanggal Peminjaman.")
            continue

        # Perbarui data berdasarkan input
        if pembaruan == "Judul Buku":
            print("\n📚 Daftar Buku yang Tersedia 📚")
            read_data(stok_buku)  # Refresh stock data

            while True:
                id_buku_baru = validasi_id_buku("Mengganti judul buku, berarti mengganti buku yang ingin dipinjam. Masukkan ID buku baru yang ingin dipinjam: ")
                buku_baru = None
                for buku in stok_buku:
                    if buku["ID Buku"] == id_buku_baru:
                        buku_baru = buku
                        break  # Stop loop once found

                if buku_baru:
                    data_peminjam["ID Buku"] = id_buku_baru
                    data_peminjam["Judul Buku"] = buku_baru["Judul Buku"]
                    print("Judul Buku berhasil diperbarui!")
                    break
                else:
                    print("ID Buku tidak ditemukan! Silakan coba lagi.")

        elif pembaruan == "Jumlah Buku":
            data_peminjam[pembaruan] = validasi_input_angka("Masukkan jumlah buku baru: ")
            print("Jumlah Buku berhasil diperbarui!")

        elif pembaruan == "Tanggal Peminjaman":
            data_peminjam[pembaruan] = validasi_tanggal()
            print("Tanggal Peminjaman berhasil diperbarui!")

        else:  # Untuk Nama Peminjam
            data_peminjam[pembaruan] = input(f"Masukkan {pembaruan} baru: ").strip()
            print(f"{pembaruan} berhasil diperbarui!")

def pengembalian_pinjaman():

    from main_menu import peminjaman
    from main_menu import stok_buku
  
    if not peminjaman:
        print("Tidak ada data peminjaman saat ini.")
        return
    
    read_data(peminjaman)
    
    while True:
        id_peminjam = input("Masukkan ID Peminjam yang mengembalikan buku: ").strip().upper()
        
        for i, pem in enumerate(peminjaman):
            if pem["ID Peminjam"] == id_peminjam:
                print("Data peminjaman ditemukan. Mengembalikan buku...")
                
                # Kembalikan stok buku
                for buku in stok_buku:
                    if buku["ID Buku"] == pem["ID Buku"]:
                        buku["Stok"] += pem["Jumlah Buku"]
                        break
                
                # Hapus dari data peminjaman
                del peminjaman[i]
                
                print("Buku berhasil dikembalikan!")
                read_data(peminjaman)
                return
        
        print("ID Peminjam tidak ditemukan dalam daftar peminjaman. Silakan coba lagi.")
