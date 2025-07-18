import os
import json
import time
import random
from pathlib import Path
from utils import pelajaran


target = pelajaran()
with open(target, "r") as f:
    isi = json.load(f)

koreksi = []
mulai = time.strftime("%H:%M")
benar = 0
salah = 0
pg_bn = ""
pg_sh = ""
for i in range(random.randint(1, 100)):
    random.shuffle(isi)

r = "\033[91m"
g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

for no, i in enumerate(isi, 1):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\n\n[Benar : {benar}] {pg_bn}\n[Salah : {salah}] {pg_sh}")
    print(f"\n[{no}] {i['pertanyaan']}\n")

    for opsi, nilai in i["pilihan"].items():
        print(f"  {opsi}. {nilai}")

    while True:
        user = input(f"\n[{g}↑{R}] Pilih salah satu: ").strip().lower()
        opsi = list(i["pilihan"].keys())
        if user not in[x.lower() for x in opsi]:
            print(f"[{y}!{R}] Masukan pilihan yang tersedia!!")
        else:
            break

    if user == i["jawaban"]:
        benar += 1
        pg_bn = "+" * pg_bn.count("+")
        pg_bn += f"{g}+{R}"
        pg_sh = ""
    else:
        salah += 1
        pg_sh = "+" * pg_sh.count("+")
        pg_sh += f"{r}+{R}"
        pg_bn = ""
        k = i["jawaban"]
        koreksi.append({
            "no": no,
            "soal": i["pertanyaan"],
            "kunci_jawaban": i["jawaban"],
            "isi_jawaban": i["pilihan"][k.upper()],
            "kunci_user": user,
            "isi_user": i["pilihan"][user.upper()]
        })

os.system("cls" if os.name == "nt" else "clear")
selesai = time.strftime("%H:%M")
print("\n")
print(f"[{y}❒{R}] Selesai.."); time.sleep(0.5)
print(f"[{g}✔{R}] Total benar: {benar}")
print(f"[{r}✘{R}] Total salah: {salah}")
print(f"[{g}⇆{R}] Total nilai: {100 / len(isi) * benar}")
print(f"[{y}Ω{R}] {mulai} - {selesai}")

if koreksi:
    cek = input(f"[{c}?{R}] Koreksi jawaban? (y/n): ").strip().lower()
    if cek == "y":
        print(f"\n\n[{c}≡{R}] Hasil koreksi "
              f"{c}{target.stem.title()}{R}\n")
        for i in koreksi:
            print(f"[{i['no']}] {i['soal']}\n")
            time.sleep(random.uniform(0.01, 0.100))

            print(f"  [{g}✔{R}] Jawaban benar: "
                  f"{i['kunci_jawaban'].upper()}. {i['isi_jawaban']}")

            print(f"  [{r}✘{R}] Jawaban salah: "
                  f"{i['kunci_user'].upper()}. {i['isi_user']}     "
                  f"{r}<~{R} Jawabanmu\n")

        print(f"\n[{c}≡{R}] Corrected By Fenrix")
    else:
        print(f"[{g}✔{R}] Makasih dah coba project gabut ini brooo")
else:
    print(f"[{g}✔{R}] Mantap lu bro")

tgl = time.strftime("%d/%m/%y")
with open("riwayat.txt", "a") as f:
    f.write(f"[{mulai}/{tgl}] {target.stem.title()} "
            f"Total benar: {benar}, Total salah: {salah}, "
            f"Total nilai: {100 / len(isi) * benar}\n")

print(f"[{c}={R}] Instagram: {g}@f.hi_7{R}")
print(f"[{c}-{R}] FQuiz v1.23.34")
