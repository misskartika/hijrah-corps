# Website Profil Perusahaan Dummy (Python Flask)

## 1. Persiapan
Pastikan Python 3 sudah terpasang.

## 2. Buka terminal di folder proyek
Opsional, buat virtual environment:

Windows:
```bash
py -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Flask
```bash
python -m pip install -r requirements.txt
```

## 4. Jalankan website
Windows:
```bash
py app.py
```

macOS/Linux:
```bash
python3 app.py
```

Buka alamat yang tampil di terminal, biasanya http://127.0.0.1:5000

## Catatan
- Semua nama, statistik, portofolio, alamat, dan nomor telepon adalah data dummy.
- Formulir kontak hanya melakukan validasi demo; belum menyimpan pesan atau mengirim email.
- `debug=True` hanya untuk pengembangan lokal. Jangan gunakan mode debug untuk deployment publik.
