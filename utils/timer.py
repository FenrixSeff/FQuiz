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
        user = int(input("[!] Pilih tingkat kesulitan: "))
        if 0 < user <= len(dft_lv):
            break
        print("\n[!] Pilih tingkat kesulitan yang tersedia!!")
    return dft_lv[user -1]

def batas_waktu(waktu):
    time.sleep(waktu * 60)
    os._exit(0)

def sisa_waktu(waktu, wadah):
    for i in range(waktu, 0, -1):
        wadah[0] = i
        time.sleep(60)

if __name__ == "__main__":
    jumlah_waktu()
    batas_waktu()
    sisa_waktu()
