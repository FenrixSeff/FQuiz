import os
import sys
import time
import random
from .path_explorer import Telusur
from .riwayat_handler import riwayat
from .rowbot import VerticalTable
from .timer import pilih_durasi_waktu
from .update import update_repo, logs
from .settings_loader import setting

menu_utama = {
    "1": "Main",
    "2": "History",
    "3": "Update",
    "0": "Keluar"
    }

menu_riwayat = {
    "1": "Terbaru",
    "2": "Terlama",
    "3": "Nilai Tertinggi",
    "4": "Nilai Terendah",
    "0": "Kembali"
    }

menu_update = {
    "1": "Riwayat Update",
    "2": "Update Repository",
    "0": "Kembali"
    }

def menus(dict_target=menu_utama, head="Menu",
          msg="Pilih opsi", info="normal"):
    table = VerticalTable()
    os.system("cls" if os.name == "nt" else "clear")
    table.add_properties(dict_target)
    table.lebar_manual(5, 37)
    table.show(header=f"{head}", align="center"); print()
    plh_mnu = table.get_input(msg_prompt=msg, info=info)
    num, arg = list(dict_target.keys()), list(dict_target.values())
    if plh_mnu in num or arg:
        return plh_mnu

def olah_menu():
    msg, icon = "Apa yang ingin anda lakukan", "normal"
    while True:
        user = menus(menu_utama, head="Menu",
                     msg=msg, info=icon)
        match user:
            case "1" | "main":
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

            case "2" | "history":
                msg, icon = "Urut berdasarkan", "normal"
                while True:
                    user = menus(menu_riwayat, head="History",
                                 msg=msg, info=icon)
                    limit = setting.get("riwayat_main", {}).get(
                        "limit", 20)
                    match user:
                        case "1" | "terbaru":
                            riwayat(mode="terbaru", dasar="id",
                            limit=limit)
                            msg, icon = "Urut berdasarkan", "normal"

                        case "2" | "terlama":
                            riwayat(mode="terlama", dasar="id",
                            limit=limit)
                            msg, icon = "Urut berdasarkan", "normal"

                        case "3" | "nilai tertinggi":
                            riwayat(mode="tertinggi", dasar="nilai",
                            limit=limit)
                            msg, icon = "Urut berdasarkan", "normal"

                        case "4" | "nilai terendah":
                            riwayat(mode="terendah", dasar="nilai",
                            limit=limit)
                            msg, icon = "Urut berdasarkan", "normal"

                        case "0" | "kembali":
                            msg, icon = ("Apa yang ingin anda lakukan",
                                        "normal")
                            break
                        case _:
                            msg, icon = "Masukan opsi yg tersedia", "e"
            case "3" | "update":
                table = VerticalTable()
                msg, icon = "Apa yang ingin anda lakukan", "normal"
                while True:
                    user = menus(menu_update, head="Update",
                        msg=msg, info=icon)
                    limit = setting.get("riwayat_update", {}).get(
                        "limit", 5)
                    match user:
                        case "1" | "riwayat":
                            logs(limit=limit)
                            table.get_input(
                                "Tekan Enter untuk melanjutkan")

                        case "2" | "update":
                            update_repo()
                            table.get_input(
                                "Tekan Enter untuk melanjutkan")

                        case "0" | "kembali":
                            break
                        case _:
                            msg, icon = "Masukan opsi yg tersedia", "e"
            case "0" | "keluar":
                sys.exit(0)
            case _:
                msg, icon = "Masukan opsi yg tersedia", "error"

def main():
    return olah_menu()


if __name__ == "__main__":
    print("jnck")
