# SmartShopping - Modular Python GUI

Aplikasi daftar belanja berbasis Python Tkinter dengan struktur modular.

## Fitur
- Tambah barang, kategori, jumlah, dan harga
- Edit barang (klik baris dua kali atau pilih lalu tombol Edit Pilihan)
- Hapus barang dan hapus semua data
- Tandai status sudah/belum dibeli
- Cari nama barang dan filter kategori/status
- Dashboard total item, status, dan estimasi biaya
- Penyimpanan otomatis ke file JSON

## Struktur
```text
SmartShopping_Modular/
├── main.py
├── config.py
├── models.py
├── utils.py
├── storage.py
├── services.py
├── data_belanja.json  # dibuat otomatis
└── ui/
    ├── __init__.py
    ├── app.py
    └── components.py
```

## Cara menjalankan
Python 3 sudah terinstal dan Tkinter tersedia.

```bash
python main.py
```

Di Debian/Ubuntu jika Tkinter belum ada:
```bash
sudo apt update
sudo apt install python3-tk
```
