from tabulate import tabulate

def read_data(data):
    print(tabulate(data, headers='keys', tablefmt='fancy_grid') if data else "Tidak ada data.")

def read_stok_buku():

    from main_menu import stok_buku

    print("\n----- Daftar Stok Buku -----")
    print(tabulate(stok_buku, headers='keys', tablefmt='fancy_grid'))
