import json
from pathlib import Path

fld = Path(__file__).parent.parent / "data"
kls = list(fld.glob("*/"))
for nu, z in enumerate(kls, 1):
    print(f"[{nu}] {z.name}")

user = int(input("\nKelas berapa? "))
jalur = fld / kls[user -1]
trg = list(jalur.glob("*.json"))
for no, i in enumerate(trg, 1):
    print(f"[{no}] {i.stem}")

usr = int(input("\nPelajaran apa? "))
with open(trg[usr -1], "r") as f:
    isi = json.load(f)

a = 0
b = 0
c = 0
d = 0
e = 0
for i in isi:
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
print(f"Jumlah soal: {len(isi)}")
print("Distribusi jawaban")
print(f"Jawaban A: {a}")
print(f"Jawaban B: {b}")
print(f"Jawaban C: {c}")
print(f"Jawaban D: {d}")
print(f"Jawaban E: {e}")

with open(trg[usr - 1], "w") as f:
    json.dump(isi, f, indent=2)
