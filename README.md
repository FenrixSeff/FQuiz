# FQuiz

Aplikasi kuis berbasis CLI (Command Line Interface) untuk pembelajaran interaktif. Pengguna dapat memilih kelas dan mata pelajaran.

## Fitur
- **Pemilihan Kelas & Mapel**: Baru tersedia untuk kelas 11 dan beberapa pelajaran saja
- **Sistem Penilaian Otomatis**:
  - Hitung nilai akhir (persentase)
  - Durasi pengerjaan
- **Pencatatan Riwayat**: Simpan hasil ke `riwayat.txt`
- **Berisi beberapa bocoran soal untuk test semester**

## Dependensi
- Python 3.x+

## Instalasi

Clone repo menggunakan `git`
```bash
git clone https://github.com/FenrixSeff/FQuiz.git
```

## Struktur File FQuiz
```
FQuiz
│
├── fquiz.py
│
├── data/
│   ├── Kelas_10/
│   │   ├── Belum ditambahkan
│   │   └── Belum ditambahkan
│   ├── Kelas_11/
│   │   ├── Sejarah tingkat lanjut
│   │   └── Sejarah Indonesia
│   └── Kelas_12/
│       ├── Belum ditambahkan
│       └── Belum ditambahkan
│
├── utils/
│   └── pelajaran.py
│
└── riwayat.txt
```

## Cara Menjalankan
```bash
python fquiz.py
```

## Catatan

Script masih dalam tahap awal - beberapa fitur mungkin berubah

## Pengembang

Fenrix

## Penulis

Fenrix

**License**: Open-source
