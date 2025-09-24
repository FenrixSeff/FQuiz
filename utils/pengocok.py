import random
from .settings_loader import setting

k_q = setting.get("fquiz", {}).get("kocok_quiz", True)
k_k = setting.get("fquiz", {}).get("kocok_keys", False)

def kocok_urutan_soal(target: list[dict]=None, y=k_q) -> list[dict]:
    file = target
    if y:
        random.shuffle(file)
        return file
    return file


def kocok_kunci_jawaban(target: list[dict]=None, y=k_k) -> list[dict]:
    file = target
    if y:
        for n, soal in enumerate(file, 1):
            k_bnr = soal.get("jawaban").lower()
            v_bnr = soal.get("pilihan").get(k_bnr)
            d_key = list(soal.get("pilihan").keys())
            d_vle = list(soal.get("pilihan").values())
            random.shuffle(d_vle)
            convert = {k.lower(): y for k, y in zip(d_key, d_vle)}
            for k, v in convert.items():
                if v == v_bnr:
                    soal["jawaban"] = k.lower()
                    break
            soal["pilihan"] = convert
        return file
    return file
