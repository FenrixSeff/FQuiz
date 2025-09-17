import os
import sys
import json
import random
from pathlib import Path

lok = Path(__file__).resolve().parent.parent.parent
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
    os.system("cls" if os.name == "nt" else "clear")
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in file:
        match i.get("jawaban").lower():
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
        "Jawaban (A)": a,
        "Jawaban (B)": b,
        "Jawaban (C)": c,
        "Jawaban (D)": d,
        "Jawaban (E)": e
    }
    table.add_properties(dft)
    table.lebar_manual(13, 13)
    table.show(header="Daftar distribusi"); print()
    table.clear()

def _simpan(target, change, spasi=2):
    with open(target, "w") as lokasi:
        json.dump(change, lokasi, indent=spasi)

def reset_kunci_jawaban(target, veborse=False):
    file = _buka_file(target)
    for n, soal in enumerate(file, 1):
        k_bnr = soal.get("jawaban").lower()
        v_bnr = soal.get("pilihan").get(k_bnr)
        d_key = list(soal.get("pilihan").keys())
        d_vle = list(soal.get("pilihan").values())
        random.shuffle(d_vle)
        convert = {k.lower(): y for k, y in zip(d_key, d_vle)}
        for k, v in convert.items():
            if v == v_bnr:
                soal["jawaban"] = k.lower()
                break
        soal["pilihan"] = convert
    _simpan(target, file)


RiwayatHandler = RiwayatHandler
Telusur = Telusur
VerticalTable = VerticalTable


if __name__ == "__main__":
    print("hooooo")
