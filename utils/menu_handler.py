import os
import time
import random
from .path_explorer import Telusur
from .riwayat_handler import riwayat
from .rowbot import VerticalTable

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
        table = VerticalTable()
        os.system("cls" if os.name == "nt" else "clear")
        table.add_properties(dict_target)
        table.lebar_manual(5, 25)
        table.show(header=f"{msg}", align="center"); print()
        plh_mnu = table.get_input("Apa yang ingin anda lakukan",info="n")
        arg = ["start", "main", "history", "riwayat", "exit", "keluar"]
        opt = list(dict_target.keys())
        if plh_mnu in arg or opt:
            return plh_mnu

def olah_menu():
    while True:
        user = menu_utama()
        match user:
            case "1" | "start" | "main":
                while True:
                    src = Telusur()
                    kelas = src.input_user(
                        msg_head="Daftar Kelas",
                        msg_prompt="Pilih Jenjang Kelas"
                    )
                    if not kelas:
                        break
                    while True:
                        src.set_target(kelas)
                        src.set_pola("*.json")
                        src.set_jenis("file")
                        mapel = src.input_user(
                            msg_head="Daftar Pelajaran",
                            msg_prompt="Pilih Mata Pelajaran"
                        )
                        if not mapel:
                            break
                        return mapel

            case "2" | "history" | "riwayat":
                riwayat()
            case "0" | "exit" | "keluar":
                return
            case _:
                pass

if __name__ == "__main__":
    print("jnck")
