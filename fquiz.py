import os
import sys
import time
import random
from threading import Thread, Event
from pathlib import Path
from utils import olah_menu
from utils import pilih_durasi_waktu, hitung_mundur
from utils import RiwayatHandler
from utils import parse_json
from utils import VerticalTable

save = RiwayatHandler()
save.init_db()
koreksi = []
wadah = [0]
stop = Event()

mapel = olah_menu()
isi = parse_json(mapel) if mapel else sys.exit(0)

wkt = pilih_durasi_waktu()
s_w = Thread(
    target=hitung_mundur,
    args=(wkt, wadah, stop),
    daemon=True
    ).start()

mulai = time.strftime("%H:%M")
benar = 0
salah = 0
for i in range(random.randint(1, 100)):
    random.shuffle(isi)

r = "\033[91m"
g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

table = VerticalTable()
for no, i in enumerate(isi, 1):
    if wadah[0] == 0:
        break
    os.system("cls" if os.name == "nt" else "clear")
    info = {"Waktu": wadah[0], "Benar": benar, "Salah": salah}
    table.add_properties(info)
    table.lebar_manual(10, 4)
    table.show()
    table.clear()

    table.single_colum(f"{no}. {i['pertanyaan']}", align="left")
    opsi = {p: j for p, j in i["pilihan"].items()}
    table.add_properties(opsi)
    table.lebar_hybrid(auto="kanan", manual=3)
    table.show()
    table.clear()

    while True:
        user = input(f"\n[{g}↑{R}] Pilih salah satu: ").strip().lower()
        opsi = list(i["pilihan"].keys())
        if user not in[x.lower() for x in opsi]:
            print(f"[{y}!{R}] Masukan pilihan yang tersedia!!")
        else:
            break

    if user == i["jawaban"]:
        benar += 1
    else:
        salah += 1
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

shio = {
    "FQuiz": f"{'Selesai..' if wadah[0] != 0 else 'Waktu habis..'}",
    "Total benar": f"{benar}",
    "Total salah": f"{salah}",
    "Total nilai": f"{nilai}",
    "Waktu mulai": f"{mulai} - {selesai}"
    }
table.add_properties(shio)
table.lebar_manual(13, 15)
table.show(); print()
table.clear()

if koreksi:
    cek = input(f"[{c}?{R}] Koreksi jawaban? (y/n): ").strip().lower()
    if cek == "y":
        table.single_colum(f"Hasil Koreksi {mapel.stem.title()}",
            align="center"); print("\n")
        for i in koreksi:
            table.single_colum(f"{i['no']}. {i['soal']}")
            kunci_benar = {f"✔": f"{i['kunci_jawaban'].upper()}. "
                   f"{i['isi_jawaban']}"}
            kunci_salah = {f"✘": f"{i['kunci_user'].upper()}. "
                   f"{i['isi_user']}    << Jawaban anda"}
            table.add_properties(kunci_benar)
            table.add_properties(kunci_salah)
            table.lebar_hybrid(auto="kanan", manual=3)
            table.show(delay=random.uniform(0.01, 0.010)); print("\n")
            table.clear()

tgl = time.strftime("%A, %d %B %Y")
save.simpan_riwayat(tgl, mapel.stem, wkt, wadah[0],
                    f"{mulai} - {selesai}", benar,
                    salah, nilai)

quote = parse_json(Path(__file__).parent / ".quote/quote.json")
table.single_colum(
    f">> Motivation  : {random.choice(quote)}",
    ">> Devloper    : Makasih dah coba project gabut ini brooo",
    ">> Corrected   : Fenrix",
    ">> Instagram   : @seff_hi7",
    ">> Version     : FQuiz v1.56.47",
    align="left")
