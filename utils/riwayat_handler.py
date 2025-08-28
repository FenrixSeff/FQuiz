import os
import time
import random
from .db_handler import RiwayatHandler
from .rowbot import VerticalTable

g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

def riwayat(mode="all"):
    os.system("cls" if os.name == "nt" else "clear")
    log = RiwayatHandler().buka_riwayat()
    if isinstance(log, tuple):
        logs = [log]
    else:
        logs = log
    table = VerticalTable()
    for tg, pl, bw, sw, wm, bn, sl, nl in logs:
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
        convert = dict(dft)
        table.add_properties(convert)
        table.lebar_manual(19, 35)
        table.show(header="History", align="left", delay=0.01); print()
        table.clear(); time.sleep(random.uniform(0.1, 0.10))
    input("[?] Kembali? ")

