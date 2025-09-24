import os
import sys
import json
from pathlib import Path

lok = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(lok))
from utils import RiwayatHandler
from utils import Telusur
from utils import VerticalTable
from utils import parse_json
from utils import kocok_kunci_jawaban

def _buka_file(target):
    return parse_json(target)

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

def reset_kunci_jawaban(target):
    file = _buka_file(target)
    kocok_kunci_jawaban(file, y=True)
    _simpan(target, file)


RiwayatHandler = RiwayatHandler
Telusur = Telusur
VerticalTable = VerticalTable


if __name__ == "__main__":
    print("hooooo")
