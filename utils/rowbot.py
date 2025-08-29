from textwrap import wrap
import time
import sys
import os

class VerticalTable:
    def __init__(self):
        self._items = []
        self.p_kiri = 11
        self.p_kanan = 35

    @property
    def size_terminal(self):
        try:
            p_max = os.get_terminal_size().columns
        except OSError:
            p_max = 70
        return p_max

    def add_properties(self, data):
        for k, v in data.items():
            self._items.append((k, v))

    def clear(self):
        self._items = []

    def lebar_auto(self):
        p_max = self.size_terminal
        self.p_kiri = (p_max // 3) - 2
        self.p_kanan = p_max - self.p_kiri - 3

    def lebar_manual(self, panjang_kiri, panjang_kanan):
        self.p_kiri = panjang_kiri
        self.p_kanan = panjang_kanan

    def lebar_hybrid(self, auto="left", manual=35):
        parse = {
            "kiri": "kiri", "left": "kiri", "kiwe": "kiri",
            "kanan": "kanan", "right": "kanan", "tengen": "kanan"
        }
        kika = parse.get(auto.strip().lower(), "left")
        match kika:
            case "kiri":
                p_max = self.size_terminal
                self.p_kanan = manual
                self.p_kiri = p_max - self.p_kanan - 3
            case _:
                p_max = self.size_terminal
                self.p_kiri = manual
                self.p_kanan = p_max - self.p_kiri - 3

    def show(self, header=None, align="left", delay=0):
        l_ki = self.p_kiri
        l_ka = self.p_kanan
        parse = {
            "kiri": "<", "left": "<", "<": "<",
            "kanan": ">", "right": ">", ">": ">",
            "tengah": "^", "center": "^", "^": "^"
        }
        # sementara cuman buat element kiri set rata nya
        rata = parse.get(align.strip().lower(), "left")
        sep_atas = "╭" + ("─" *l_ki) + "┬" + ("─" *l_ka) + "╮"
        sep_tngh = "├" + ("─" *l_ki) + "┼" + ("─" *l_ka) + "┤"
        sep_bawh = "╰" + ("─" *l_ki) + "┴" + ("─" *l_ka) + "╯"
        if header:
            print(f"╭" + ("─" *(l_ki + l_ka + 1)) + "╮", flush=True)
            print(f"│ {str(header)[:l_ki +l_ka -1]:^{l_ki +l_ka -1}} │",
                flush=True)
            print(f"├" + ("─" *(l_ki + l_ka + 1)) + "┤", flush=True)
        else:
            print(sep_atas)

        for i, (k, v) in enumerate(self._items):
            time.sleep(delay)
            sl_v = wrap(str(v), width=l_ka)
            print(f"│ {str(k)[:l_ki -2]:{rata}{l_ki -2}} "
                  f"│ {str(sl_v[0])[:l_ka -2]:<{l_ka -2}} │",
                  flush=True)
            if len(sl_v) > 1:
                for n, b in enumerate(sl_v):
                    if n == 0:
                        continue
                    print(sep_tngh, flush=True)
                    print(f"│ {" ":^{l_ki -2}} "
                          f"│ {str(b):<{l_ka -2}} │", flush=True)
            if i < len(self._items) - 1:
                print(sep_tngh, flush=True)
        print(sep_bawh, flush=True)

    def single_colum(self, *data, manual=False, align="left"):
        if manual:
            p_max = manual
        else:
            p_max = self.size_terminal
        parse = {
            "kiri": "<", "left": "<", "<": "<",
            "kanan": ">", "right": ">", ">": ">",
            "tengah": "^", "center": "^", "^": "^"
        }
        rata = parse.get(align.strip().lower(), "left")
        p_txt = p_max - 4
        sep_atas = "╭" + ("─" *(p_max - 2)) + "╮"
        sep_bawh = "╰" + ("─" *(p_max - 2)) + "╯"
        print(sep_atas, flush=True)
        for d in data:
            bungkus = wrap(str(d), width=p_txt)
            for b in bungkus:
                print(f"│ {b:{rata}{p_txt}} │", flush=True)
        print(sep_bawh, flush=True)

    def get_input(self, msg_prompt="Masukan pilihan", info="normal"):
        r = "\033[91m"
        g = "\033[92m"
        y = "\033[93m"
        R = "\033[0m"

        p_max = self.size_terminal
        parse = {
            "normal": "✔", "n": "✔", "error": "✘", "e": "✘",
            "peringatan": "!", "warning": "!", "w": "!"
        }
        icon = parse.get(info.strip().lower(), "normal")
        info_ki = f"╭─[{msg_prompt}]"
        info_ka = f"[{icon}]"
        p_garis = p_max - len(info_ki) - len(info_ka)
        match icon:
            case "✘":
                info_ka = f"[{r}{icon}{R}]"
            case "!":
                info_ka = f"[{y}{icon}{R}]"
            case _:
                info_ka = f"[{g}{icon}{R}]"
        sep_atas = f"{info_ki}{'─' *p_garis}{info_ka}"
        sep_bawh = "╰─ "
        print(sep_atas, flush=True)
        try:
            user = input(sep_bawh).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("fquiz: User memaksa keluar. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"fquiz: Terjadi kesalahan tidak terduga:\n{e}")
            sys.exit(0)
        return user

if __name__ == "__main__":
    print("Hoammmmmmm")
    yy = "oaahbsusis"
    table = VerticalTable()
    table.single_colum(yy)
    table.get_input(msg_prompt="Jawaban anda", info="e")
