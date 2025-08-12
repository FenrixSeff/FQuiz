import os
import time
import random
from .mapel_handler import pelajaran
from .riwayat_handler import riwayat

g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

menu = {
    "1": "Main",
    "2": "History",
    "0": "Keluar"
    }

def menu_utama(dict_target=menu, msg="Menu"):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n\n[{c}≡{R}] {msg}\n ")
        for no, dft in dict_target.items():
            print(f"  [{no}] {dft}")
        plh_mnu = input(f"\n[{g}↑{R}] Pilih menu: ").strip().lower()
        arg = ["start", "main", "history", "riwayat", "exit", "keluar"]
        opt = list(dict_target.keys())
        if plh_mnu in arg or opt:
            return plh_mnu

def olah_menu():
    while True:
        user = menu_utama()
        match user:
            case "1" | "start" | "main":
                return pelajaran()
            case "2" | "history" | "riwayat":
                riwayat()
            case "0" | "exit" | "keluar":
                return
            case _:
                pass

if __name__ == "__main__":
    print("jnck")
