import os
import sys
import json
import random
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
        match i["jawaban"].lower():
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

def _simpan(target, change, spasi=2):
    with open(target, "w") as lokasi:
        json.dump(change, lokasi, indent=spasi)

def reset_kunci_jawaban(target, verbose=False):
    file = _buka_file(target)
    for n, soal in enumerate(file, 1):
        k_bnr = soal.get("jawaban").lower()
        v_bnr = soal["pilihan"].get(k_bnr)
        d_key = list(soal["pilihan"].keys())
        d_vle = list(soal["pilihan"].values())
        random.shuffle(d_vle)
        convert = {k.lower(): y for k, y in zip(d_key, d_vle)}
        for k, v in convert.items():
            if v == v_bnr:
                soal["jawaban"] = k.lower()
                break
        soal["pilihan"] = convert
    _simpan(target, file)

dft = {"1": "Cek distribusi jawaban",
       "2": "Set indentasi format json",
       "3": "Hapus riwayat",
       "4": "Reset kunci jawaban",
       "0": "Keluar"
    }

DEFAULT = {
    "data": Path(__file__).parent.parent / "data"
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
        print("\nDevTools v1.7.15")
        exit(0)

    elif user == 1:
        while True:
            os.system("clear")
            src.set_target(DEFAULT["data"])
            src.set_pola("*/")
            src.set_jenis("dir")
            k = src.input_user("Distribusi Jawaban", "Pilih kelas")
            if not k:
                break
            while True:
                src.set_target(k)
                src.set_pola("*.json")
                src.set_jenis("file")
                p = src.input_user("Distribusi Jawaban", "Pilih mapel")
                if not p:
                    break
                info_soal(p)
                table.get_input("Tekan Enter untuk melanjutkan")

    elif user == 2:
        while True:
            os.system("clear")
            src.set_target(DEFAULT["data"])
            src.set_pola("*/")
            src.set_jenis("dir")
            k = src.input_user("Set Indentasi", "Pilih kelas")
            if not k:
                break
            while True:
                src.set_target(k)
                src.set_pola("*.json")
                src.set_jenis("file")
                p = src.input_user("Set Indentasi", "Pilih Mapel")
                if not p:
                    break
                c = _buka_file(p)
                _simpan(p, c)
                table.get_input("Success, Enter untuk melanjutkan")
                break

    elif user == 3:
        table = VerticalTable()
        os.system("clear")
        RiwayatHandler().hapus_semua_riwayat()
        table.get_input("Succes, Enter untuk melanjutkan")

    elif user == 4:
        while True:
            os.system("clear")
            src.set_target(DEFAULT["data"])
            src.set_pola("*/")
            src.set_jenis("dir")
            k = src.input_user("Reset Kunci Jawaban", "Pilih kelas")
            if not k:
                break
            while True:
                src.set_target(k)
                src.set_pola("*.json")
                src.set_jenis("file")
                p = src.input_user("Reset Kunci Jawaban", "Pilih Mapel")
                if not p:
                    break
                reset_kunci_jawaban(p, verbose=True)
                table.get_input("Success, Enter untuk melanjutkan")
                break
