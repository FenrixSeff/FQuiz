import subprocess
from threading import Thread
from .loading import Loading

def update_repo():
    load = Loading()
    try:
        Thread(target=load.spiner, daemon=True).start()
        up = subprocess.run(
            ["git", "pull"],
            capture_output=True, text=True, check=True
            )
        load.done = True
        print(f"\rFQuiz {up.stdout}")
    except subprocess.CalledProcessError as e:
        print("\rUpdate gagal")

if __name__ == "__main__":
    update_repo()
