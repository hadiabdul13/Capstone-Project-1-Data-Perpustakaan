from .fungsi_baca_data import read_data
from .fungsi_validasi import validasi_id_buku, validasi_input_angka, validasi_tanggal

def perbarui_peminjaman():
    from main_menu import peminjaman, stok_buku

    read_data(peminjaman)  

    while True:
        id_peminjam = input("\nMasukkan ID Peminjam yang ingin diperbarui: ").strip().upper()

        # Cek apakah ID peminjam ada dalam data peminjaman
        data_peminjam = None
        for data in peminjaman:
            if data['ID Peminjam'] == id_peminjam:
                data_peminjam = data
                break  

        if data_peminjam:
            print("\nData ditemukan. Silakan pilih data yang ingin diperbarui.")
            break
        else:
            print("\nID Peminjam tidak ditemukan! Silakan coba lagi.")

    while True:
        pembaruan = input("\nMasukkan data yang ingin diperbarui (Nama Peminjam, Judul Buku, Jumlah Buku, Tanggal Peminjaman). Ketik 'selesai' untuk keluar: ").strip().title()

        if pembaruan.lower() == "selesai":
            print("\nPerbaruan selesai.")
            return

        if pembaruan not in ["Nama Peminjam", "Judul Buku", "Jumlah Buku", "Tanggal Peminjaman"]:
            print("\nKolom tidak valid. Gunakan: Nama Peminjam, Judul Buku, Jumlah Buku, Tanggal Peminjaman.")
            continue

        # Perbarui data berdasarkan input
        if pembaruan == "Judul Buku":
            print("\nDaftar Buku yang Tersedia")
            read_data(stok_buku)
            print("")
            while True:
                id_buku_baru = validasi_id_buku("Mengganti judul buku, berarti mengganti buku yang ingin dipinjam. Masukkan ID buku baru yang ingin dipinjam: ")
                
                # Cari buku dalam stok
                buku_baru = None
                for buku in stok_buku:
                    if buku["ID Buku"] == id_buku_baru:
                        buku_baru = buku
                        break  # Stop loop once found

                if buku_baru:
                    data_peminjam["ID Buku"] = id_buku_baru
                    data_peminjam["Judul Buku"] = buku_baru["Judul Buku"]
                    print(f"Judul Buku berhasil diperbarui menjadi: {buku_baru['Judul Buku']}!")
                    break
                else:
                    print("\nID Buku tidak ditemukan! Silakan coba lagi.")

        elif pembaruan == "Jumlah Buku":
            data_peminjam["Jumlah Buku"] = validasi_input_angka("\nMasukkan jumlah buku baru: ")
            print("\nJumlah Buku berhasil diperbarui!")

        elif pembaruan == "Tanggal Peminjaman":
            data_peminjam["Tanggal Peminjaman"] = validasi_tanggal()
            print("\nTanggal Peminjaman berhasil diperbarui!")

        elif pembaruan == "Nama Peminjam":
            data_peminjam["Nama Peminjam"] = input(f"\nMasukkan {pembaruan} baru: ").strip()
            print(f"\n{pembaruan} berhasil diperbarui!")

        while True:
            lanjut = input("\nMasih adakah yang ingin diperbarui? (ya/tidak): ").strip().lower()
            if lanjut in ["ya", "tidak"]:
                break
            else:
                print("\nMasukkan hanya 'ya' atau 'tidak'.")

        if lanjut == "tidak":
            print("\nPerbaruan selesai.")
            return
        
def perbarui_data_buku():
    from main_menu import stok_buku
    from utils.fungsi_validasi import validasi_input_angka, validasi_input_alfabet

    if not stok_buku:
        print("\nTidak ada data buku saat ini.")
        return

    read_data(stok_buku)  # Menampilkan daftar buku sebelum perbarui

    while True:
        id_buku = input("\nMasukkan ID Buku yang ingin diperbarui: ").strip().upper()

        # Cek apakah ID Buku ada dalam stok
        data_buku = None
        for buku in stok_buku:
            if buku["ID Buku"] == id_buku:
                data_buku = buku
                break

        if data_buku:
            print("\nData buku ditemukan. Silakan pilih informasi yang ingin diperbarui.")
            break
        else:
            print("\nID Buku tidak ditemukan! Silakan coba lagi.")

    while True:
        pembaruan = input("\nMasukkan data yang ingin diperbarui (Judul Buku, Penulis, Stok). Ketik 'selesai' untuk keluar: ").strip().title()

        if pembaruan.lower() == "selesai":
            print("\nPerbaruan selesai.")
            return

        if pembaruan not in ["Judul Buku", "Penulis", "Stok"]:
            print("\nKolom tidak valid. Gunakan: Judul Buku, Penulis, Stok.")
            continue

        # Perbarui data berdasarkan input
        if pembaruan == "Judul Buku":
            data_buku["Judul Buku"] = input("\nMasukkan judul buku baru: ").strip()
            print("\nJudul buku berhasil diperbarui!")

        elif pembaruan == "Penulis":
            data_buku["Penulis"] = validasi_input_alfabet("\nMasukkan nama penulis baru: ").strip()
            print("\nNama penulis berhasil diperbarui!")

        elif pembaruan == "Stok":
            data_buku["Stok"] = validasi_input_angka("\nMasukkan jumlah stok buku baru: ")
            print("\nJumlah stok berhasil diperbarui!")

        while True:
            lanjut = input("\nMasih adakah yang ingin diperbarui? (ya/tidak): ").strip().lower()
            if lanjut in ["ya", "tidak"]:
                break
            else:
                print("\nMasukkan hanya 'ya' atau 'tidak'.")

        if lanjut == "tidak":
            print("\nPerbaruan selesai.")
            return

def pengembalian_pinjaman():
    from main_menu import peminjaman, stok_buku

    if not peminjaman:  # Cek apakah ada peminjaman
        print("\nTidak ada data peminjaman saat ini.")
        return

    read_data(peminjaman)

    while True:  # Loop utama untuk pengembalian buku
        id_peminjam = input("\nMasukkan ID Peminjam yang akan mengembalikan buku: ").strip().upper()

        # Filter daftar pinjaman yang sesuai dengan ID Peminjam
        daftar_pinjaman = [p for p in peminjaman if p["ID Peminjam"] == id_peminjam]

        if not daftar_pinjaman:
            print("\nID Peminjam tidak ditemukan dalam daftar peminjaman. Silakan coba lagi.")
            continue  # Kembali ke awal untuk meminta ID Peminjam lagi

        print("\nDaftar Buku yang Dipinjam:")
        for pem in daftar_pinjaman:
            print(f"ID Buku: {pem['ID Buku']} | Judul: {pem['Judul Buku']} | Jumlah: {pem['Jumlah Buku']}")

        while True:
            id_buku_kembali = input("\nMasukkan ID Buku yang akan dikembalikan: ").strip().upper()

            # Cek apakah buku benar-benar dipinjam oleh peminjam ini
            peminjaman_terpilih = next((pem for pem in daftar_pinjaman if pem["ID Buku"] == id_buku_kembali), None)

            if not peminjaman_terpilih:
                print("\nID Buku tidak sesuai dengan data peminjaman. Silakan coba lagi.")
                continue  # Minta ID Buku lagi

            # Update stok buku
            for buku in stok_buku:
                if buku["ID Buku"] == id_buku_kembali:
                    buku["Stok"] += peminjaman_terpilih["Jumlah Buku"]
                    break

            # Hapus peminjaman hanya untuk buku ini
            peminjaman.remove(peminjaman_terpilih)

            print(f"\nBuku '{peminjaman_terpilih['Judul Buku']}' berhasil dikembalikan.")

            # Tanya apakah ingin mengembalikan buku lain
            while True:
                lanjut = input("\nApakah masih ada buku lain yang ingin dikembalikan? (ya/tidak): ").strip().lower()
                if lanjut in ["ya", "tidak"]:
                    break
                print("\nMasukkan hanya 'ya' atau 'tidak'. Silakan coba lagi.")

            if lanjut == "ya":
                break  # Kembali ke awal untuk memasukkan ID peminjam baru

            print("\nSemua buku yang ingin dikembalikan telah diproses.")
            return  # Keluar setelah semua proses selesai