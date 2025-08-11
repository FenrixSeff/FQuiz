import os
import sys
import time
import random
from threading import Thread, Event
from pathlib import Path
from utils import pelajaran
from utils import jumlah_waktu, sisa_waktu
from utils import DatabaseHandler, RiwayatHandler
from utils import parse_json

DatabaseHandler().init_db()
koreksi = []
wadah = [0]
stop = Event()

mapel = pelajaran()
isi = parse_json(mapel) if mapel else sys.exit(0)

wkt = jumlah_waktu()
s_w = Thread(
    target=sisa_waktu,
    args=(wkt, wadah, stop),
    daemon=True
    ).start()

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
    if wadah[0] == 0:
        break
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\n[Waktu : {wadah[0]}]\n[Benar : {benar}] {pg_bn}"
          f"\n[Salah : {salah}] {pg_sh}")
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

stop.set()
os.system("cls" if os.name == "nt" else "clear")
selesai = time.strftime("%H:%M")
nilai = 100 / len(isi) * benar
print("\n")
print(f"[{y}❒{R}] {'Selesai..' if wadah[0] != 0 else 'Waktu habis..'}")
print(f"[{g}✔{R}] Total benar: {benar}")
print(f"[{r}✘{R}] Total salah: {salah}")
print(f"[{g}⇆{R}] Total nilai: {nilai}")
print(f"[{y}Ω{R}] {mulai} - {selesai}")

if koreksi:
    cek = input(f"[{c}?{R}] Koreksi jawaban? (y/n): ").strip().lower()
    if cek == "y":
        print(f"\n\n[{c}≡{R}] Hasil koreksi "
              f"{c}{mapel.stem.title()}{R}\n")
        for i in koreksi:
            print(f"[{i['no']}] {i['soal']}\n")
            time.sleep(random.uniform(0.01, 0.100))

            print(f"  [{g}✔{R}] Jawaban benar: "
                  f"{i['kunci_jawaban'].upper()}. {i['isi_jawaban']}")

            print(f"  [{r}✘{R}] Jawaban salah: "
                  f"{i['kunci_user'].upper()}. {i['isi_user']}     "
                  f"{r}<~{R} Jawabanmu\n")
    else:
        print(f"[{g}✔{R}] Makasih dah coba project gabut ini brooo")
else:
    print(f"[{g}✔{R}] Mantap lu brooo..")

tgl = time.strftime("%A, %d %B %Y")
RiwayatHandler().simpan_riwayat(tgl, mapel.stem, wkt, wadah[0],
                                f"{mulai} - {selesai}", benar,
                                salah, nilai)

quote = parse_json(Path(__file__).parent / ".quote/quote.json")
print(f"\n[{g}φ{R}] Motivation: {c}{random.choice(quote)}{R}")
print(f"\n[{c}≡{R}] Corrected By Fenrix")
print(f"[{c}={R}] Instagram: {g}@seff_hi7{R}")
print(f"[{c}-{R}] FQuiz v1.49.42")
