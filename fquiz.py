import os
import sys
import time
import random
from threading import Thread, Event
from pathlib import Path
from utils import main
from utils import hitung_mundur
from utils import RiwayatHandler
from utils import parse_json
from utils import VerticalTable

save = RiwayatHandler()
save.init_db()

mapel, durasi_waktu = main()
soal = parse_json(mapel)

waktu_tersisa = [0]
stop = Event()
Thread(
    target=hitung_mundur,
    args=(durasi_waktu, waktu_tersisa, stop),
    daemon=True).start()

for _ in range(random.randint(1, 100)):
    random.shuffle(soal)

benar = 0
salah = 0
table = VerticalTable()
mulai = time.strftime("%H:%M")
daftar_koreksi = []

for no, i in enumerate(soal, 1):
    if waktu_tersisa[0] == 0:
        break
    os.system("cls" if os.name == "nt" else "clear")
    bars = {"Waktu": waktu_tersisa[0], "Benar": benar, "Salah": salah}
    table.add_properties(bars)
    table.lebar_manual(10, 4)
    table.show()
    table.clear()

    table.single_colum(f"{no}. {i['pertanyaan']}", align="left")
    opsi = {p: j for p, j in i["pilihan"].items()}
    table.add_properties(opsi)
    table.lebar_hybrid(auto="kanan", manual=3)
    table.show(); print()
    table.clear()

    msg, icon = "Kunci jawaban anda", "normal"
    while True:
        user = table.get_input(msg_prompt=msg, info=icon)
        opsi = list(i["pilihan"].keys())
        if user not in[x.lower() for x in opsi]:
            msg, icon = "Masukan pilihan yang tersedia", "error"
        else:
            break

    if user == i["jawaban"]:
        benar += 1
    else:
        salah += 1
        k = i["jawaban"]
        daftar_koreksi.append({
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
nilai = 100 / len(soal) * benar

shio = {
    "FQuiz":
        f"{'Selesai..' if waktu_tersisa[0] != 0 else 'Waktu habis..'}",
    "Total benar": f"{benar}",
    "Total salah": f"{salah}",
    "Total nilai": f"{nilai}",
    "Waktu mulai": f"{mulai} - {selesai}"
    }
table.add_properties(shio)
table.lebar_manual(13, 15)
table.show(); print()
table.clear()

if daftar_koreksi:
    cek = table.get_input(msg_prompt="Koreksi Jawaban anda (y/n)",
                          info="normal")
    if cek == "y":
        table.single_colum(f"Hasil Koreksi {mapel.stem.title()}",
            align="center"); print("\n")
        for i in daftar_koreksi:
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

tanggal = time.strftime("%A, %d %B %Y")
save.simpan_riwayat(tanggal, mapel.stem, durasi_waktu,
                    waktu_tersisa[0], f"{mulai} - {selesai}",
                    benar, salah, nilai)

quote = parse_json(Path(__file__).parent / ".quote/quote.json")
table.single_colum(
    f">> Motivation  : {random.choice(quote)}",
    ">> Devloper    : Makasih dah coba project gabut ini brooo",
    ">> Corrected   : Fenrix",
    ">> Instagram   : @seff_hi7",
    ">> Version     : FQuiz v1.58.48",
    align="left")
