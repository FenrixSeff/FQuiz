import os
import time
from threading import Event, Thread

class Loading:
    def __init__(self, stopper: Event=None):
        self.__stop = stopper

    @property
    def _size_terminal(self):
        try:
            p_max = os.get_terminal_size().columns
        except OSError:
            p_max = 70
        return p_max

    def spiner(self, msg="Loading", delay=0.5):
        spin = ["|", "/", "-", "\\"]
        i = 0
        while not self.__stop.is_set():
            print(f"\r{msg} {spin[i % len(spin)]} ",
            end="", flush=True)
            i += 1
            time.sleep(delay)

    def bars(self, msg="Loading", delay=0.5):
        bar = "="
        for i in range(21):
            if self.__stop.is_set() or i == 20:
                print(f"\r{msg} [{(bar*20):<20}] (100%) ",
                end="", flush=True)
                break
            print(f"\r{msg} [{(bar* i)+'>':<20}] ({i*5}%) ",
            end="", flush=True)
            time.sleep(delay)

    def fquiz(self, delay: int=0.5):
        p_max = self._size_terminal
        title = "F Q U I Z"
        sep_at_bw = '█' * p_max
        sep_kosong = f"█{' ' * (p_max - 2)}█"
        judul = f"█{title:^{p_max - 2}}█"

        print(sep_at_bw); time.sleep(delay)
        print(sep_kosong); time.sleep(delay)
        print(judul); time.sleep(delay)
        print(sep_kosong); time.sleep(delay)
        print(sep_at_bw); time.sleep(delay)


if __name__ == "__main__":
    stop = Event()
    load = Loading(stop)
    # Thread(target=load.bars, daemon=True).start()
    # time.sleep(1)
    # stop.set()
    print("\n")
    load.fquiz()
    print("\n\n")
    input()
