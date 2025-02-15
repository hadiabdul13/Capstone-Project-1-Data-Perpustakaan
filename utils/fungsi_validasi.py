from datetime import datetime
def validasi_input_alfabet(prompt):
    while True:
        inputan = input(prompt).strip()
        if inputan.replace(" ", "").isalpha():
            return inputan
        print('Input harus berupa huruf.')

def validasi_input_angka(prompt):
    while True:
        inputan = input(prompt).strip()
        if inputan.isdigit():
            return int(inputan)
        print('Input harus berupa angka.')

def validasi_id_buku(pesan = "Masukkan ID Buku: "):

    from main_menu import stok_buku

    while True:
        id_buku = input(pesan).strip().upper()
        if any(buku["ID Buku"] == id_buku for buku in stok_buku):
            return id_buku
        else:
            print("\nID Buku tidak valid. Silakan coba lagi.")

def validasi_tanggal():
    while True:
        tanggal = input("Masukkan tanggal peminjaman (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(tanggal, "%d-%m-%Y")
            return tanggal  # Jika valid, kembalikan nilai tanggal
        except ValueError:
            print("\nFormat tanggal salah! Gunakan format DD-MM-YYYY.")
