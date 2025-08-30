import os
import time
import random
from .db_handler import RiwayatHandler
from .rowbot import VerticalTable

def riwayat(mode="all"):
    table = VerticalTable()
    os.system("cls" if os.name == "nt" else "clear")
    log = RiwayatHandler().buka_riwayat()
    if isinstance(log, tuple):
        logs = [log]
    else:
        logs = log
    for tg, pl, bw, sw, wm, bn, sl, nl in logs:
        dft = {
            "Tanggal": tg,
            "Mata Pelajaran": pl.title(),
            "Batas Waktu": f"{bw} Menit",
            "Waktu Tersisa": f"{sw} Menit",
            "Mulai Mengerjakan": wm,
            "Jumlah Benar": bn,
            "Jumlah Salah": sl,
            "Nilai Akhir (%)": nl
        }
        table.add_properties(dft)
        table.lebar_manual(19, 35)
        table.show(header="History", align="left", delay=0.01); print()
        table.clear(); time.sleep(random.uniform(0.1, 0.10))
    print()
    table.get_input("Tekan Enter untuk kembali", info="normal")

