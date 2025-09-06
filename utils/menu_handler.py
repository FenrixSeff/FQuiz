import os
import sys
import time
import random
from .path_explorer import Telusur
from .riwayat_handler import riwayat
from .rowbot import VerticalTable
from .timer import pilih_durasi_waktu

menu_utama = {
    "1": "Main",
    "2": "History",
    "0": "Keluar"
    }

menu_riwayat = {
    "1": "Terbaru",
    "2": "Terlama",
    "0": "Kembali"
    }

def menus(dict_target=menu_utama, head="Menu", msg="Pilih opsi"):
    table = VerticalTable()
    os.system("cls" if os.name == "nt" else "clear")
    table.add_properties(dict_target)
    table.lebar_manual(5, 37)
    table.show(header=f"{head}", align="center"); print()
    plh_mnu = table.get_input(msg_prompt=msg, info="normal")
    num, arg = list(dict_target.keys()), list(dict_target.values())
    if plh_mnu in num or arg:
        return plh_mnu

def olah_menu():
    while True:
        user = menus(menu_utama, head="Menu",
                     msg="Apa yang ingin anda lakukan")
        match user:
            case "1":
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
                        while True:
                            batas_waktu = pilih_durasi_waktu()
                            if not batas_waktu:
                                break
                            else:
                                return mapel, batas_waktu

            case "2":
                while True:
                    user = menus(menu_riwayat, head="History",
                                 msg="Urutkan berdasarkan")
                    match user:
                        case "1":
                            riwayat(mode="terbaru")
                        case "2":
                            riwayat(mode="terlama")
                        case "0":
                            break
            case "0":
                sys.exit(0)
            case _:
                pass

def main():
    return olah_menu()


if __name__ == "__main__":
    print("jnck")
