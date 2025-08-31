import json
import random

with open("soal.json", "r") as f:
    soal = json.load(f)

for s in soal:
    k_bnr = s.get("jawaban")
    v_bnr = s["pilihan"].get(k_bnr)
    # print(v_bnr)
    print("="*77)
    print("sebelum kocok")
    dft = list(s["pilihan"].values())
    print(dft)
    print("-"*77)
    print("sesudah kocok")
    random.shuffle(dft)
    print(dft)

    dft_key = list(s["pilihan"].keys())
    print(dft_key)
