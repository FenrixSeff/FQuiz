import json
import random

with open("soal.json", "r") as f:
    soal = json.load(f)

for s in soal:
    k_bnr = s.get("jawaban").upper()
    v_bnr = s["pilihan"].get(k_bnr)
    print("="*77)
    print("sebelum kocok")
    dft = list(s["pilihan"].values())
    print(dft)
    print(k_bnr, v_bnr)
    print("-"*77)
    print("sesudah kocok")
    random.shuffle(dft)
    print(dft)

    dft_key = list(s["pilihan"].keys())
    convert = {k: v for k, v in zip(dft_key, dft)}
    s["pilihan"] = convert
    for k, v in convert.items():
        if v == v_bnr:
            s["jawaban"] = k.lower()

with open("soal.json", "w") as f:
    json.dump(soal, f, indent=2)
