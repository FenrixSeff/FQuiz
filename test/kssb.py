tg = 10
df = [
    ("Tanggal", tg),
    ("Bulan", tg)
]

val = dict(df)
print(val)
for k, v in df:
    pass

yy = [
    "katon", "jinton", "futon"
]
for n, v in enumerate(yy, 1):
    dft = [
        (n, v)
    ]
    gateng = dict(dft)
    print(gateng)

def sh(*uu):
    print(len(uu))

sh("wuwhwg", "ihevwwh")

def gen():
    for i in range(1_000):
        yield i
