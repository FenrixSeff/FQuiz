import os
import time
import random
from threading import Thread, Event
from pathlib import Path
from utils import main
from utils import hitung_mundur
from utils import RiwayatHandler
from utils import parse_json
from utils import VerticalTable
from utils import kocok_urutan_soal, kocok_kunci_jawaban
from utils import Loading

stop = Event()
save = RiwayatHandler()
load = Loading()
table = VerticalTable()
benar = 0
salah = 0
waktu_tersisa = [0]
daftar_koreksi = []

save.init_db()
mapel, durasi_waktu = main()

soal = parse_json(mapel)
kocok_urutan_soal(soal)
kocok_kunci_jawaban(soal)

os.system("cls" if os.name == "nt" else "clear")
load.fquiz(delay=0); print("\n")
table.get_input("Tekan Enter untuk melanjutkan")

Thread(
    target=hitung_mundur,
    args=(durasi_waktu, waktu_tersisa, stop),
    daemon=True).start()

mulai = time.strftime("%H:%M")

for no, i in enumerate(soal, 1):
    if waktu_tersisa[0] == 0:
        break
    os.system("cls" if os.name == "nt" else "clear")
    table.single_colum(f"{no}. {i.get('pertanyaan')}", align="left")
    opsi = {p.upper(): j for p, j in i.get("pilihan").items()}
    table.add_properties(opsi)
    table.lebar_hybrid(auto="kanan", manual=3)
    table.show(); print()
    table.clear()

    msg, icon = (f" Time: {waktu_tersisa[0]}m | "
                f"Correct: {benar} | Incorrect: {salah} ", "normal")
    while True:
        user = table.get_input(msg_prompt=msg, info=icon)
        opsi = list(i.get("pilihan").keys())
        if user not in[x.lower() for x in opsi]:
            msg, icon = "Masukan pilihan yang tersedia", "error"
        else:
            break

    if user == i.get("jawaban"):
        benar += 1
    else:
        salah += 1
        daftar_koreksi.append({
            "no": no,
            "soal": i.get("pertanyaan"),
            "kunci_jawaban": i.get("jawaban"),
            "isi_jawaban": i.get("pilihan").get(i.get("jawaban")),
            "kunci_user": user,
            "isi_user": i.get("pilihan").get(user)
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
        os.system("cls" if os.name == "nt" else "clear")
        table.single_colum(
            f"Hasil Koreksi Mata Pelajaran {mapel.stem.title()}",
            align="center"); print("\n")
        for i in daftar_koreksi:
            table.single_colum(f"{i.get('no')}. {i.get('soal')}")
            kunci_benar = {f"✔": f"{i.get('kunci_jawaban').upper()}. "
                   f"{i.get('isi_jawaban')}"}
            kunci_salah = {f"✘": f"{i.get('kunci_user').upper()}. "
                   f"{i.get('isi_user')}    << Jawaban anda"}
            table.add_properties(kunci_benar)
            table.add_properties(kunci_salah)
            table.lebar_hybrid(auto="kanan", manual=3)
            table.show(delay=random.uniform(0.01, 0.010)); print("\n")
            table.clear()

tanggal = time.strftime("%A, %d %B %Y")
save.simpan_riwayat(tanggal, mapel.parent.name, mapel.stem,
                    durasi_waktu, waktu_tersisa[0],
                    f"{mulai} - {selesai}", benar, salah, nilai)

quote = parse_json(Path(__file__).parent / ".quote/quote.json")
table.single_colum(
    f">> Motivation  : {random.choice(quote)}",
    ">> Devloper    : Makasih dah coba project gabut ini brooo",
    ">> Corrected   : Fenrix",
    ">> Instagram   : @seff_hi7",
    ">> Version     : FQuiz v1.73.50",
    align="left")
