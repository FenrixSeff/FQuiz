import os
from pathlib import Path

import handlers


dft = {"1": "Cek distribusi jawaban",
       "2": "Reset kunci jawaban",
       "3": "Hapus riwayat",
       "0": "Keluar"
    }

DEFAULT = {
    "data": Path(__file__).parent.parent / "data"
    }

while True:
    table = handlers.VerticalTable()
    src = handlers.Telusur()
    os.system("cls" if os.name == "nt" else "clear")
    table.add_properties(dft)
    table.lebar_manual(5, 37)
    table.show(header="DevTools", align="center"); print()
    table.clear()
    user = int(table.get_input("Pilih opsi", "normal"))
    if user == 0:
        print("\nDevTools v1.8.17")
        exit(0)

    elif user == 1:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            src.set_target(DEFAULT["data"])
            src.set_pola("*/")
            src.set_jenis("dir")
            k = src.input_user("Distribusi Jawaban", "Pilih kelas")
            if not k:
                break
            while True:
                src.set_target(k)
                src.set_pola("*.json")
                src.set_jenis("file")
                p = src.input_user("Distribusi Jawaban", "Pilih mapel")
                if not p:
                    break
                handlers.info_soal(p)
                table.get_input("Tekan Enter untuk melanjutkan")

    elif user == 2:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            src.set_target(DEFAULT["data"])
            src.set_pola("*/")
            src.set_jenis("dir")
            k = src.input_user("Reset Kunci Jawaban", "Pilih kelas")
            if not k:
                break
            while True:
                src.set_target(k)
                src.set_pola("*.json")
                src.set_jenis("file")
                p = src.input_user("Set Indentasi", "Pilih Mapel")
                if not p:
                    break
                handlers.reset_kunci_jawaban(p)
                table.get_input("Success, Enter untuk melanjutkan")
                break

    elif user == 3:
        table = handlers.VerticalTable()
        os.system("cls" if os.name == "nt" else "clear")
        RiwayatHandler().hapus_semua_riwayat()
        table.get_input("Succes, Enter untuk melanjutkan")
