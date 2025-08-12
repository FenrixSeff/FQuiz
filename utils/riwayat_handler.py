import os
import time
import random
from .db_handler import RiwayatHandler

g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

def riwayat():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\n\n[{c}≡{R}] History\n ")
    log = RiwayatHandler().buka_riwayat()
    sep = "+" + '—' * 19 + "+" + "—" * 35 + "+"
    for tg, pl, bw, sw, wm, bn, sl, nl in log:
        dft = [
            ("Tanggal", tg),
            ("Mata Pelajaran", pl.title()),
            ("Batas Waktu", f"{bw} Menit"),
            ("Waktu Tersisa", f"{sw} Menit"),
            ("Mulai Mengerjakan", wm),
            ("Jumlah Benar", bn),
            ("Jumlah Salah", sl),
            ("Nilai Akhir (%)", nl)
                ]
        for label, val in dft:
            print(sep, flush=True)
            print(f"| {label[:17]:<17} | "
                  f"{str(val)[:33]:<33} |", flush=True)
            time.sleep(random.uniform(0.01, 0.100))
        print(sep + "\n", flush=True)
        time.sleep(random.uniform(0.01, 0.100))
    input("[?] Kembali? ")
