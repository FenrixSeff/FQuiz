import json
from pathlib import Path

lok = Path(__file__).resolve().parent.parent / "data/kelas_12"
dft_p = list(lok.glob("*.json"))

for p in dft_p:
    with open(p, "r") as f:
        soal = json.load(f)

    for s in soal:
        dft_k = s["pilihan"].keys()
        convert = {k.lower(): v for k, v in zip(dft_k,
                   s["pilihan"].values())}
        s["pilihan"] = convert

    with open(p, "w") as f:
        json.dump(soal, f, indent=2)
