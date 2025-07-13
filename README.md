# FQuiz

Aplikasi kuis berbasis CLI (Command Line Interface) untuk pembelajaran interaktif. Pengguna dapat memilih kelas dan mata pelajaran. 'Beberapa soal mungkin ada yang muncul di test semester'

## Fitur
- **Pemilihan Kelas & Mapel**: Baru tersedia untuk kelas 11 dan beberapa pelajaran saja
- **Sistem Penilaian Otomatis**:
  - Hitung nilai akhir (persentase)
  - Durasi pengerjaan
- **Pencatatan Riwayat**: Simpan hasil ke `riwayat.txt`

## Dependensi
- Python 3.x+

## Instalasi
```bash
pkg install git
git clone https://github.com/FenrixSeff/DoTask.git
```

## Struktur File Proyek
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

