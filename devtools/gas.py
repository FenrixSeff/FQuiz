import os
import sys
import json
from pathlib import Path

lok = Path(__file__).resolve().parent.parent
sys.path.append(str(lok))
from utils import pelajaran, hapus_semua_riwayat

def buka_file(target):
    with open(target, "r") as f:
        isi = json.load(f)
    return isi

def info_soal(target, kelas):
    os.system("clear")
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in target:
        match i["jawaban"]:
            case "a":
                a += 1
            case "b":
                b += 1
            case "c":
                c += 1
            case "d":
                d += 1
            case _:
                e += 1

    print(f"\n\n[≡] {kelas.stem}\n\n"
          f"  [-] Jumlah soal: {len(target)}\n"
          f"  [-] Jawaban A: {a}\n"
          f"  [-] Jawaban B: {b}\n"
          f"  [-] Jawaban C: {c}\n"
          f"  [-] Jawaban D: {d}\n"
          f"  [-] Jawaban E: {e}\n")

def rapihkan(target, isi, spasi=2):
    with open(target, "w") as f:
        json.dump(isi, f, indent=spasi)

dft = {"1": "Cek distribusi jawaban",
       "2": "Set indentasi file",
       "3": "Hapus riwayat",
       "0": "Keluar"
    }

while True:
    os.system("clear")
    print("\n\n[≡] DevTools\n\n"
          "  [0] Nggak jadi..\n")
    user = input("[!] Masukan password untuk mengakses: ").strip()
    if user == "seffhii":    # Tuh gw spil password nya
        break
    elif user == "0":
        exit(0)

while True:
    os.system("clear")
    print("\n\n[≡] Option\n")
    for no, i in dft.items():
        print(f"  [{no}] {i}")
    user = int(input("\n[↑] Pilih opsi: "))
    if user == 0:
        print("\nDevTools v1.4.13")
        exit(0)

    elif user == 1:
        os.system("clear")
        d = pelajaran()
        if d:
            f = buka_file(d)
            info_soal(f, d)
            y = input("[?] Kembali? ")
        else:
            pass

    elif user == 2:
        os.system("clear")
        d = pelajaran()
        if d:
            f = buka_file(d)
            rapihkan(d, f)
            y = input("[?] Kembali? ")
        else:
            pass
    elif user == 3:
        os.system("clear")
        hapus_semua_riwayat()
        print("\n")
        y = input("[?] Kembali? ")
