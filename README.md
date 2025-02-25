# Creator Profile:
Abdul Hadi - [hadiabdul13@gmail.com](hadiabdul13@gmail.com) | [LinkedIn](https://www.linkedin.com/in/abdul-hadi-447608159/)

# Sistem Administrasi Peminjaman Buku

Sistem ini adalah program berbasis Python untuk membantu administrasi peminjaman buku di perpustakaan. Sistem ini memungkinkan petugas perpustakaan untuk mencatat, mengelola, dan memantau data peminjaman buku dengan berbagai fitur yang tersedia.

## Fitur Utama
- **Tambah Peminjaman**: Mencatat peminjaman buku baru.
- **Periksa Data Peminjaman**: Melihat daftar peminjaman yang sedang berlangsung.
- **Periksa Stok Buku**: Mengecek ketersediaan buku di perpustakaan.
- **Tambah Stok Buku**: Menambah stok buku baru atau memperbarui stok buku yang sudah ada.
- **Perbarui Data**: Mengedit informasi peminjaman dan data buku.
- **Hapus & Pulihkan Data**: Memindahkan data peminjaman ke Recycle Bin dan memulihkannya jika diperlukan.
- **Pencarian Data**: Mencari data peminjaman berdasarkan nama peminjam atau judul buku.
- **Pengembalian Buku**: Mencatat pengembalian buku dan memperbarui stok.

## Instalasi
1. Pastikan Anda memiliki Python terinstal di sistem Anda.
2. Clone repositori ini:
   ```sh
   git clone https://github.com/username/repository.git](https://github.com/hadiabdul13/Capstone-Project-1-Data-Perpustakaan)
   cd repository
   ```
3. Install dependensi yang diperlukan:
   ```sh
   pip install -r requirements.txt
   ```

## Cara Penggunaan
1. Jalankan program dengan perintah:
   ```sh
   python main_menu.py
   ```
2. Ikuti instruksi di layar untuk mengakses berbagai fitur sistem.

## Struktur Proyek
```
📂 repository
├── main_menu.py           # Program utama
├── __init__.py            # Inisialisasi modul
├── fungsi_add.py          # Fungsi menambah peminjaman dan stok buku
├── fungsi_baca_data.py    # Fungsi membaca data peminjaman dan stok buku
├── fungsi_create_data.py  # Fungsi membuat ID buku dan peminjam
├── fungsi_search.py       # Fungsi pencarian data peminjaman
├── fungsi_update.py       # Fungsi pembaruan data peminjaman dan buku
├── fungsi_restore.py      # Fungsi untuk menghapus dan memulihkan peminjaman
├── fungsi_validasi.py     # Fungsi validasi input
└── utils/                 # Folder utilitas
```

## Kontribusi
Jika ingin berkontribusi dalam pengembangan sistem ini:
1. Fork repositori ini
2. Buat branch baru (`git checkout -b feature-branch`)
3. Commit perubahan (`git commit -m 'Add new feature'`)
4. Push ke branch Anda (`git push origin feature-branch`)
5. Buat Pull Request
