import random
import string
def membuat_id_buku():

    from main_menu import stok_buku

    while True:
        id_baru = 'B' + ''.join(random.choices(string.digits, k=3))
        if not any(buku["ID Buku"] == id_baru for buku in stok_buku):
            return id_baru
        
def membuat_id_peminjam():
    return 'P' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
