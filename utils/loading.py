import time

class Loading:
    def __init__(self):
        self.spin = ["|", "/", "-", "\\"]
        self.done = False

    def spiner(self):
        spin = self.spin
        i = 0
        while not self.done:
            print(f"\rLoading.. {spin[i % len(spin)]} ", end="")
            i += 1
            time.sleep(0.5)

if __name__ == "__main__":
    load = Loading()
    threading.Thread(target=load.spiner, daemon=True).start()
    time.sleep(10)
    load.done = True
