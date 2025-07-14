import os
from pathlib import Path

g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

def pelajaran():
    data_fld = Path(__file__).parent.parent / "data" # parsing folder
    kelas_fld = list(data_fld.glob("*/"))

    os.system("cls" if os.name == "nt" else "clear")
    dft_kls = [k.name for k in kelas_fld if k.is_dir()] # angkut folder
    print(f"\n\n[{c}≡{R}] Daftar Kelas\n ")
    for no, kelas in enumerate(dft_kls, 1):
        print(f"  [{g}{no}{R}] {kelas.upper()}")

    while True:     # validasi input user
        pilih_kelas = input(f"\n[{g}↑{R}] Pilih kelas: ").strip()
        if pilih_kelas.isdigit():
            no_kls = int(pilih_kelas)
            if 0 < no_kls <= len(dft_kls):
                break
        print(f"\n[{y}!{R}] Pilih kelas yang tersedia!")

    mapel_fld = data_fld / dft_kls[no_kls - 1]   # folder target
    mapel_file = list(mapel_fld.glob("*.json"))     # isi folder target

    # daftar untuk di lihat user
    os.system("cls" if os.name == "nt" else "clear")
    dft_mapel = [m.stem for m in mapel_file]
    print(f"\n\n[{c}≡{R}] Daftar Pelajaran\n ")
    for no, mapel in enumerate(dft_mapel, 1):
        print(f"  [{g}{no}{R}] {mapel.upper()}")

    while True:
        pilih_mapel = input(f"\n[{g}↑{R}] Pilih mapel: ").strip()
        if pilih_mapel.isdigit():
            no_mapel = int(pilih_mapel)
            if 0 < no_mapel <= len(mapel_file):
                break
        print(f"\n[{y}!{R}] Pilih mapel yang tersedia!")

    return mapel_file[no_mapel - 1] # lempar hasil ke script utama

if __name__ == "__main__":
    pelajaran()
