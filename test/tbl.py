

def tabel(header=("Opsi", "Rincian"),
          data=None, kiri=11, kanan=35,
          angka=True, manual=None):
    if angka:
        daftar = [(i, v) for i, v in enumerate(data, 1)]
    elif manual:
        daftar = [(i, v) for i, v in zip(manual, data)]
    sep_atas = "╭" + ("─" *kiri) + "┬" + ("─" *kanan) + "╮"
    sep_tngh = "├" + ("─" *kiri) + "┼" + ("─" *kanan) + "┤"
    sep_bawh = "╰" + ("─" *kiri) + "┴" + ("─" *kanan) + "╯"
    print(sep_atas, flush=True)
    if header:
        head_ki, head_ka = header
        print(f"│ {head_ki:^{kiri -2}} │ {head_ka:^{kanan -2}} │",
              flush=True)
        print(sep_tngh, flush=True)

    for i, (idx, val) in enumerate(daftar):
        print(f"│ >> {idx:<{kiri -5}} │ {val:<{kanan -2}} │", flush=True)
        if i < len(daftar) -1:
            print(sep_tngh, flush=True)
    print(sep_bawh, flush=True)

    # debug
    print(daftar)
    print(i, idx, val)
    print(i, (idx, val))
    print(len(daftar))

x = ["data1", "data2", "data3", "data4"]
y = ["A", "B", "C", "D"]
tabel(header=None, data=x, angka=False, manual=y)

# 2 jam bikin kayak ginian doanggg, haaahhhhhhhhhh mending turu
