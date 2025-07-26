import os
import time
import threading
import queue

sisa = [0]
q = queue.Queue()
wkt = int(input("Hitung mundur dari: "))

def cek_waktu():
    time.sleep(wkt)
    os._exit(0)

def sisa_waktu(target):
    for i in range(wkt, 0, -1):
        # print(f"Sisa waktu {i}")
        target[0] = i
        time.sleep(1)
        # q.put(i)

t1 = threading.Thread(target=cek_waktu, daemon=True)
t2 = threading.Thread(target=sisa_waktu, args=(sisa,), daemon=True)

t1.start()
t2.start()

while True:
    # print(q.get())
    print(sisa[0])
    time.sleep(1)

usr = input("Tunggu bentar! ")
