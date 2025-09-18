## Langkah langkah

1. Instal ChatBot bebas (ChatGpt, Manus atau DeepSeek)

2. Siapkan materi referensi

3. Tempelkan matari referensi tersebut bersama prompt dibawah ini

## Prompt generate soal format json

```
Buatkan saya soal pilihan ganda untuk pelajaran [MASUKKAN_MAPEL_DAN_KELAS] dengan materi:
[MASUKKAN_MATERI_REFERENSI].

Instruksi:

1. Gunakan informasi hanya dari sumber terpercaya dan terverifikasi, agar tidak ada kesalahan pemahaman konsep.


2. Buat 50 soal pilihan ganda.


3. Format hasilnya dalam bentuk JSON dengan struktur list of dict seperti contoh berikut:



[
  {
    "pertanyaan": "Masa Demokrasi Terpimpin (1959-1965) ditandai dengan?",
    "pilihan": {
      "a": "Dominasi parlemen",
      "b": "Sistem multipartai kuat",
      "c": "Kekuasaan terpusat pada presiden",
      "d": "Kebebasan pers tanpa batas",
      "e": "Desentralisasi kekuasaan"
    },
    "jawaban": "c"
  }
]

4. Pastikan setiap soal memiliki 5 pilihan jawaban (a–e).


5. Kunci jawaban ditulis dengan huruf kecil sesuai abjad pilihan yang benar (misalnya "jawaban": "c").


6. Semua soal harus relevan dengan materi yang saya berikan.


7. Tidak boleh ada duplikasi soal.
```
