import time

class Loading:
    def __init__(self):
        self.__finished = False

    def done(self):
        self.__finished = True

    def spiner(self, msg="Loading", delay=0.5):
        spin = ["|", "/", "-", "\\"]
        i = 0
        while not self.__finished:
            print(f"\r{msg} {spin[i % len(spin)]} ",
            end="", flush=True)
            i += 1
            time.sleep(delay)

    def bars(self, msg="Loading", delay=0.5):
        bar = "="
        for i in range(21):
            if self.__finished or i == 20:
                print(f"\r{msg} [{(bar*20):<20}] (100%) ",
                end="", flush=True)
                break
            print(f"\r{msg} [{(bar* i)+'>':<20}] ({i*5}%) ",
            end="", flush=True)
            time.sleep(delay)

if __name__ == "__main__":
    load = Loading()
    threading.Thread(target=load.bars, daemon=True).start()
    time.sleep(5)
    load.done()
    input()
