import time
import os

class VerticalTable:
    def __init__(self):
        self._items = []
        self.p_kiri = 11
        self.p_kanan = 35

    def add_properties(self, data):
        for k, v in data.items():
            self._items.append((k, v))

    def clear(self):
        self._items = []

    def lebar_auto(self):
        p = os.get_terminal_size().columns
        self.p_kiri = (p // 3) - 2
        self.p_kanan = p - self.p_kiri - 3

    def lebar_manual(self, panjang_kiri, panjang_kanan):
        self.p_kiri = panjang_kiri
        self.p_kanan = panjang_kanan

    def show(self, align="<", delay=0):
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
        print(sep_atas)
        for i, (k, v) in enumerate(self._items):
            print(f"│ {str(k)[:l_ki -2]:{rata}{l_ki -2}} "
                  f"│ {str(v)[:l_ka -2]:<{l_ka -2}} │")
            time.sleep(delay)
            if i < len(self._items) - 1:
                print(sep_tngh)
        print(sep_bawh)


if __name__ == "__main__":
    print("Hoammmmmmm")
