import os
import sys
import json
from pathlib import Path

lok = Path(__file__).resolve().parent.parent
sys.path.append(str(lok))
from utils import RiwayatHandler
from utils import Telusur
from utils import VerticalTable

def _buka_file(target):
    with open(target, "r") as f:
        isi = json.load(f)
    return isi

def info_soal(target):
    file = _buka_file(target)
    table = VerticalTable()
    os.system("clear")
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in file:
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
    dft = {
        "Jumlah soal": len(file),
        "Jawaban A": a,
        "Jawaban B": b,
        "Jawaban C": c,
        "Jawaban D": d,
        "Jawaban E": e
    }
    table.add_properties(dft)
    table.lebar_manual(13, 13)
    table.show(header="Daftar distribusi"); print()
    table.clear()

def rapihkan(target, spasi=2):
    file = _buka_file(target)
    with open(target, "w") as lokasi:
        json.dump(file, lokasi, indent=spasi)

dft = {"1": "Cek distribusi jawaban",
       "2": "Set indentasi format json",
       "3": "Hapus riwayat",
       "0": "Keluar"
    }

while True:
    table = VerticalTable()
    src = Telusur()
    os.system("clear")
    table.add_properties(dft)
    table.lebar_manual(5, 37)
    table.show(header="DevTools", align="center"); print()
    table.clear()
    user = int(table.get_input("Pilih opsi", "normal"))
    if user == 0:
        print("\nDevTools v1.6.14")
        exit(0)

    elif user == 1:
        os.system("clear")
        k = src.input_user("Daftar Kelas", "Pilih kelas")
        if k:
            src.set_target(k)
            src.set_pola("*.json")
            src.set_jenis("file")
            p = src.input_user("Daftar pelajaran", "Pilih mapel")
            if p:
                info_soal(p)
                table.get_input("Tekan Enter untuk melanjutkan")
            else:
                pass
        else:
            pass

    elif user == 2:
        os.system("clear")
        k = src.input_user("Daftar kelas", "Pilih kelas")
        if k:
            src.set_target(k)
            src.set_pola("*.json")
            src.set_jenis("file")
            p = src.input_user("Daftar pelajaran", "Pilih Mapel")
            if p:
                rapihkan(p)
                table.get_input("Succes, Enter untuk melanjutkan")
            else:
                pass
        else:
            pass

    elif user == 3:
        table = VerticalTable()
        os.system("clear")
        RiwayatHandler().hapus_semua_riwayat()
        table.get_input("Succes, Enter untuk melanjutkan")
