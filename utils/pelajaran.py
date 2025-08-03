import os
import sys
from pathlib import Path
from .db_handler import buka_riwayat

g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

def pelajaran():
    data_fld = Path(__file__).parent.parent / "data" # parsing folder
    kelas_fld = list(data_fld.glob("*/"))

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        dft_kls = [k for k in kelas_fld if k.is_dir()] # angkut fld
        print(f"\n\n[{c}≡{R}] Daftar Kelas\n ")
        for no, kelas in enumerate(dft_kls, 1):
            print(f"  [{no}] {kelas.name.title()}")

        print("  [0] Keluar\n"
              "  [$] Riwayat")
        while True:     # validasi input user
            pilih_kelas = input(f"\n[{g}↑{R}] Pilih kelas: ").strip()
            if pilih_kelas in["riwayat", "logs", "$"]:
                log = buka_riwayat()
                for tg, pl, bw, sw, bn, sl, nl in log:
                    print(f"{tg} | {pl} | {bw} | {sw} "
                          f"| {bn} | {sl} | {nl}")
                return
            if pilih_kelas.isdigit():
                no_kls = int(pilih_kelas)
                if 0 < no_kls <= len(dft_kls):
                    break
                elif no_kls == 0:
                    return
            print(f"\n[{y}!{R}] Pilih kelas yang tersedia!")

        mapel_fld = data_fld / dft_kls[no_kls - 1]   # folder target
        mapel_file = list(mapel_fld.glob("*.json"))  # isi folder target

        # daftar untuk di lihat user
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n\n[{c}≡{R}] Daftar Pelajaran "
              f"{c}{mapel_fld.name}{R}\n ")

        for no, mapel in enumerate(mapel_file, 1):
            print(f"  [{no}] {mapel.stem.title()}")

        print(f"  [0] Kembali")
        while True:
            pilih_mapel = input(f"\n[{g}↑{R}] Pilih mapel: ").strip()
            if pilih_mapel.isdigit():
                no_mapel = int(pilih_mapel)
                if 0 < no_mapel <= len(mapel_file):
                    return mapel_file[no_mapel - 1]

                elif no_mapel == 0:
                    break
            print(f"\n[{y}!{R}] Pilih mapel yang tersedia!")


if __name__ == "__main__":
    pelajaran()
