import os
import time

def jumlah_waktu():
    os.system("cls" if os.name == "nt" else "clear")
    level = {
        "1": "Santai (50 menit)",
        "2": "Sedang (35 menit)",
        "3": "Cepat (25 menit)",
        "4": "Expert (15 menit)"
    }
    print("\n\n[≡] Difficulty\n")
    for no, lv in level.items():
        print(f"  [{no}] {lv}")
    dft_lv = [50, 35, 25, 15, 1]
    print()
    while True:
        try:
            user = int(input("[!] Pilih tingkat kesulitan: "))
            if 0 < user <= len(dft_lv):
                return dft_lv[user -1]

            print("\n[!] Pilih tingkat kesulitan yang tersedia!!")
        except ValueError:
            print("\n[!] Masukin angka brooo..")

def sisa_waktu(waktu, wadah, berhenti):
    for i in range(waktu, -1, -1):
        if berhenti.is_set():
            break
        wadah[0] = i
        time.sleep(60)

if __name__ == "__main__":
    print("jsbsh1havs")
