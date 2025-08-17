import os
from pathlib import Path

g = "\033[92m"
y = "\033[93m"
c = "\033[96m"
R = "\033[0m"

DEFAULT = {
    "data": Path(__file__).parent.parent / "data"
    }

class Telusur:
    def __init__(self, target=DEFAULT["data"]):
        self.path_target = target
        self._saring_pola = "*/"
        self._saring_jenis = "dir"

    @property
    def hasil_pencarian(self):
        if not self.path_target.is_dir():
            return []
        return self.path_target.glob(self._saring_pola)

    @property
    def daftar_tersaring(self):
        hasil = self.hasil_pencarian
        match self._saring_jenis:
            case "file":
                return [k for k in hasil if k.is_file()]
            case "dir":
                return [k for k in hasil if k.is_dir()]
            case _:
                return list(hasil)

    def set_target(self, path_baru):
        self.path_target = path_baru

    def set_pola(self, pola_baru="*/"):
        self._saring_pola = pola_baru

    def set_jenis(self, jenis_baru="dir"):
        parse_jenis = {
            "dir": "dir", "direktori": "dir", "directory": "dir",
            "folder": "dir", "file": "file", "files": "file",
            "semua": "semua", "all": "semua"
            }
        self._saring_jenis = parse_jenis.get(jenis_baru.lower(), "semua")

    def tampilkan_daftar(self, msg="Folder"):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n\n[{c}≡{R}] {msg}\n ")
        dft_item = self.daftar_tersaring
        for no, opsi in enumerate(dft_item, 1):
            parse = opsi.name if opsi.is_dir() else opsi.stem.title()
            print(f"  [{no}] {parse}")
        print("  [0] Kembali")
        return dft_item

    def input_user(self, msg="pilh salah satu"):
        dft = self.tampilkan_daftar()
        if not dft:
            input("Tekan Enter untuk melanjutkan..")
            return None
        while True:     # validasi input user
            pilih_target = input(f"\n[{g}↑{R}] {msg}: ").strip()
            if pilih_target.isdigit():
                no_target = int(pilih_target)
                if 0 < no_target <= len(dft):
                    return dft[no_target -1]
                elif no_target == 0:
                    return None
            print(f"\n[{y}!{R}] Pilih opsi yang tersedia!")


if __name__ == "__main__":
    print("hancoooookwwh")
