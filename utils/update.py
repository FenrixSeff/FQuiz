import os
import time
import subprocess
from threading import Thread, Event
from .loading import Loading
from .rowbot import VerticalTable

def _run_command(cmd):
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
        )

def update_repo():
    stop = Event()
    load = Loading(stop)
    try:
        t = Thread(
            target=load.bars,
            kwargs={"msg": "Checking update..", "delay": 0.5},
            daemon=True)

        t.start()
        cek_status = _run_command(["git", "status", "--porcelain"])
        if cek_status.stdout:
            time.sleep(1)
            stop.set()
            t.join()
            print("\nFQuiz: Anda memiliki perubahan lokal yang belum "
                  "di-commit")
            return

        _run_command(["git", "fetch"])
        lokal = _run_command(["git", "rev-parse", "HEAD"]).strip()
        remot = _run_command(["git", "rev-parse", "origin/main"]).strip()
        if lokal == remot:
            time.sleep(1)
            stop.set()
            t.join()
            print("\nFQuiz: Anda sudah di versi terbaru")
            return

        _run_command(["git", "pull", "origin", "main"])
        print("FQuiz: Update berhasil")
        stop.set()
        t.join()

    except subprocess.CalledProcessError as e:
        print(f"\nFQuiz: Update gagal\n {e}")
    except FileNotFoundError:
        print("\nFQuiz: Trjadi kesalah pada git")
    finally:
        stop.set()
        t.join()

def logs(limit=5):
    os.system("cls" if os.name == "nt" else "clear")
    table = VerticalTable()
    log_format = "--pretty=format:%s (%cr)"
    try:
        log_update = _run_command(
            ["git", "log", log_format, f"-n{limit}"])

        log_lines = log_update.stdout.splitlines()
        dft = {i: line for i, line in enumerate(log_lines, 1)}
        table.add_properties(dft)
        table.lebar_hybrid(auto="right", manual=5)
        table.show(header="Riwayat Update baru-baru ini",
            align="center"); print()

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"\nFQuiz: Gagal mengambil riwayat update: {e}")

if __name__ == "__main__":
    update_repo()
    logs()
