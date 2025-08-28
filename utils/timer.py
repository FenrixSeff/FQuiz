import os
import sys
import time
from .rowbot import VerticalTable

def pilih_durasi_waktu() -> int:
    """
    Menampilkan menu tingkat kesulitan dan meminta input dari pengguna.

    waktu (dalam menit), dan terus meminta input hingga pengguna
    memasukkan pilihan yang valid.

    Returns:
        int: Durasi waktu dalam satuan menit yang dipilih oleh pengguna.
    """
    table = VerticalTable()
    os.system("cls" if os.name == "nt" else "clear")
    level = {
        "1": {"label": "Santai (50 menit)", "nilai": 50},
        "2": {"label": "Sedang (35 menit)", "nilai": 35},
        "3": {"label": "Cepat (25 menit)", "nilai": 25},
        "4": {"label": "Expert (15 menit)", "nilai": 15}
    }
    opsi = {str(no): lv["label"] for no, lv in level.items()}
    table.add_properties(opsi)
    table.lebar_manual(5, 25)
    table.show(header="Difficulty", align="center"); print()
    while True:
        try:
            user = input("[!] Pilih tingkat kesulitan: ")
            if user in level:
                return level[user]["nilai"]
            else:
                if user.isdigit():
                    print("\n[!] Pilih tingkat kesulitan yang tersedia!")
                else:
                    print("\n[!] Masukan pilihan yang valid!!")
        except (EOFError, KeyboardInterrupt):
            print("\n[!] User memaksa keluar. Exiting...")
            sys.exit()


def hitung_mundur(durasi_waktu: int, wadah_output: list[int], berhenti):
    """
    Menjalankan timer hitung mundur per menit di background.

    Fungsi ini dirancang untuk dijalankan di dalam sebuah
    thread terpisah.

    Setiap menit, ia akan memperbarui nilai di `wadah_output` dengan
    sisa waktu. Timer akan berhenti jika sudah mencapai nol atau
    jika `berhenti_event` di-set dari thread lain.

    Args:
        durasi_menit (int): Total waktu hitung mundur dalam satuan menit.

        output_wadah (list[int]): Sebuah list atau objek mutable
            lainnya dengan minimal satu elemen, yang akan digunakan
            untuk menyimpan sisa waktu. `wadah_output[0]`akan di-update
            setiap menit.

        berhenti: Objek Event yang digunakan untuk memberi sinyal
            agar timer berhenti sebelum waktunya habis.
    """
    for i in range(durasi_waktu, -1, -1):
        if berhenti.is_set():
            break
        wadah_output[0] = i
        time.sleep(60)

if __name__ == "__main__":
    print("jsbsh1havs")
