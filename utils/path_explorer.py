import os
import sys
import time
import random
from pathlib import Path

g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

DEFAULT = {
    "data": Path(__file__).parent.parent / "data"
    }

class Telusur:
    def __init__(self, target=DEFAULT["data"], saring="*/"):
        self.saring = saring
        self.target = target
        self.folder_target = list(self.target.glob(self.saring))
        self.daftar_kelas = [k for k in self.folder_target if k.is_dir()]

    def set_exstensi(self, ganti):
        self.saring = ganti
        self.folder_target = list(self.target.glob(self.saring))

    def set_target(self, ganti):
        self.target = ganti

    def set_daftar(self, jenis="file"):
        match jenis:
            case "file":
                self.daftar_kelas = [
                   k for k in self.folder_target if k.is_file()]

    def daftar(self, msg="Folder"):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n\n[{c}≡{R}] {msg}\n ")
        for no, opsi in enumerate(self.daftar_kelas, 1):
            print(f"  [{no}] "
                  f"{opsi.name if opsi.is_dir() else opsi.stem.title()}"
                  )
        print("  [0] Kembali")

    def angkut_user(self, msg="pilh salah satu"):
        while True:     # validasi input user
            pilih_target = input(f"\n[{g}↑{R}] {msg}: ").strip()
            if pilih_target.isdigit():
                no_target = int(pilih_target)
                if 0 < no_target <= len(self.daftar_kelas):
                    return self.daftar_kelas[no_target -1]
                elif no_target == 0:
                    return
            print(f"\n[{y}!{R}] Pilih opsi yang tersedia!")


if __name__ == "__main__":
    print("hancoooookwwh")
