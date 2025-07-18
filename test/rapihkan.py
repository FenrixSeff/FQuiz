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

with open(trg[usr - 1], "w") as f:
    json.dump(isi, f, indent=2)
