import time
from threading import Event, Thread

class Loading:
    def __init__(self, stopper: Event):
        self.__stop = stopper

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

if __name__ == "__main__":
    stop = Event()
    load = Loading(stop)
    Thread(target=load.bars, daemon=True).start()
    time.sleep(5)
    stop.set()
    input()
