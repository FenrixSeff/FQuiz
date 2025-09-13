import os
import subprocess
from threading import Thread
from .loading import Loading
from .rowbot import VerticalTable

def update_repo():
    load = Loading()
    try:
        t = Thread(
            target=load.bars,
            kwargs={"msg": "Checking update..", "delay": 0.5},
            daemon=True)
        t.start()
        up = subprocess.run(
            ["git", "pull"],
            capture_output=True, text=True, check=True)
        load.done()
        t.join()
        print(f"\nFQuiz {up.stdout}")
    except subprocess.CalledProcessError as e:
        print("\nUpdate gagal")

def logs(limit=5):
    os.system("cls" if os.name == "nt" else "clear")
    table = VerticalTable()
    up = subprocess.run(
        ["git", "log", "--oneline", "--graph"],
        capture_output=True, text=True
    )
    dft = {}
    for k, v in enumerate(up.stdout.splitlines(), 1):
        if k > limit:
            break
        dft[k] = v

    table.add_properties(dft)
    table.lebar_hybrid(auto="right", manual=5)
    table.show(header="Riwayat Update baru-baru ini",
        align="center"); print()

if __name__ == "__main__":
    update_repo()
    logs()
