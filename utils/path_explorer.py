import os
from pathlib import Path
from typing import Generator, Optional
from .rowbot import VerticalTable

g = "\033[92m"   # Hijau
y = "\033[93m"   # Kuning
c = "\033[96m"   # Cyan
R = "\033[0m"    # Reset Warna

DEFAULT = {
    "data": Path(__file__).parent.parent / "data"   # Default target
    }

class Telusur:
    """
    Kelas utilitas untuk menelusuri, menyaring, dan memilih
    file atau direktori.

    Kelas ini dirancang untuk menyederhanakan navigasi sistem
    file dengan memungkinkan pengguna untuk mengatur direktori
    target, pola pencarian (glob),
    dan jenis item (file/direktori) yang akan ditampilkan.

    Attributes:
        path_target (Path): Lokasi direktori yang menjadi
            target penelusuran.
    """
    def __init__(self, target=DEFAULT["data"]):
        """
        Menginisialisasi objek Telusur.

        Args:
            target: Path awal untuk direktori target.
                Default ke `DEFAULT["data"]`.
        """
        self.path_target = Path(target)
        self._saring_pola = "*/"
        self._saring_jenis = "dir"


    @property
    def hasil_pencarian(self) -> Generator[Path, None, None]:
        """
        Generator yang menghasilkan item dari `path_target`
        sesuai `_saring_pola`.

        Properti ini melakukan pencarian menggunakan `glob`
        secara *lazy*. Jika `path_target` bukan direktori
        yang valid, properti ini akan menghasilkan generator kosong.

        Returns:
            Generator[Path, None, None]: Generator yang Berisi objek
                Path dari hasil pencarian.
        """
        if not self.path_target.is_dir():
            return []
        return self.path_target.glob(self._saring_pola)


    @property
    def daftar_tersaring(self) -> list[Path]:
        """
        Daftar item yang telah disaring berdasarkan jenis (file atau
        direktori).

        Properti ini mengambil hasil dari `hasil_pencarian` dan
        menyaringnya lebih lanjut sesuai dengan nilai `_saring_jenis`.

        Returns:
            list[Path]: Daftar objek Path yang sudah final dan siap
                ditampilkan.
        """
        hasil = self.hasil_pencarian
        match self._saring_jenis:
            case "file":
                return [k for k in hasil if k.is_file()]
            case "dir":
                return [k for k in hasil if k.is_dir()]
            case _:
                return list(hasil)


    def set_target(self, path_baru):
        """
        Mengubah direktori target untuk penelusuran.

        Args:
            path_baru: Path direktori baru yang akan
                ditelusuri.
        """
        self.path_target = Path(path_baru)


    def set_pola(self, pola_baru="*/"):
        """
        Mengatur pola pencarian (glob) yang akan digunakan.

        Contoh: "*.txt" untuk semua file teks, "data_*" untuk item yang
        berawalan "data_".

        Args:
            pola_baru (str, optional): Pola glob baru. Default ke "*/".
        """
        self._saring_pola = pola_baru


    def set_jenis(self, jenis_baru="dir"):
        """
        Mengatur jenis item yang akan disaring ('dir', 'file', atau
        'semua').

        Metode ini menerima berbagai alias (seperti 'folder',
        'berkas') dan mengonversinya ke nilai standar ('dir', 'file',
        'semua').

        Args:
            jenis_baru (str, optional): Jenis item yang diinginkan.
                Contoh: "dir", "file", "semua". Default ke "dir".
        """
        parse_jenis = {
            "dir": "dir", "direktori": "dir", "directory": "dir",
            "folder": "dir","katalog": "dir", "file": "file",
            "files": "file", "berkas": "file", "dokumen": "file",
            "semua": "semua", "all": "semua"
            }
        self._saring_jenis = parse_jenis.get(jenis_baru.lower(),"semua")


    def tampilkan_daftar(self, msg_head="Folder") -> list[Path]:
        """
        Menampilkan daftar item yang telah disaring.

        Args:
            msg_head (str, optional): Judul yang akan ditampilkan
                di atas daftar. Default ke "Folder".

        Returns:
            list[Path]: Daftar item yang ditampilkan, untuk digunakan
                oleh metode lain.
        """
        table = VerticalTable()
        dft_item = self.daftar_tersaring
        os.system("cls" if os.name == "nt" else "clear")
        opsi = {str(no): fld.name.title() if fld.is_dir() else
            fld.stem.title() for no, fld in enumerate(dft_item, 1)}
        opsi["0"] = "Kembali"
        table.add_properties(opsi)
        table.lebar_manual(5, 37)
        table.show(header=f"{msg_head}", align="center"); print()
        table.clear()
        return dft_item


    def input_user(self,
                   msg_head="Folder",
                   msg_prompt="pilh salah satu") -> Optional[Path]:
        """
        Menampilkan daftar dan meminta input dari pengguna.

        Metode ini mengelola seluruh alur interaksi: menampilkan daftar,
        memvalidasi input, dan mengembalikan pilihan pengguna.

        Args:
            msg_head (str, optional): Judul untuk daftar.
                Default ke "Folder".

            msg_prompt (str, optional): Pesan untuk meminta input.
                Default ke "Pilih salah satu".

        Returns:
            Optional[Path]: Objek Path dari item yang dipilih, atau None
                jika pengguna memilih kembali atau daftar kosong.
        """
        table = VerticalTable()
        daftar = self.tampilkan_daftar(msg_head)
        if not daftar:
            table.get_input("Tekan Enter untuk kembali", info="n")
            return None
        while True:     # validasi input user
            pilih_target = table.get_input(f"{msg_prompt}", info="n")
            if pilih_target.isdigit():
                no_target = int(pilih_target)
                if 0 < no_target <= len(daftar):
                    return daftar[no_target -1]
                elif no_target == 0:
                    return None
            print(f"\n[{y}!{R}] Pilih opsi yang tersedia!")


if __name__ == "__main__":
    print("hancoooookwwh")
