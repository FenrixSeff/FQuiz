import os
import time
import threading

wkt = int(input("Hitung mundur dari: "))

def cek_waktu():
    time.sleep(wkt)
    os._exit(0)

t = threading.Thread(target=cek_waktu, daemon=True)
t.start()
usr = input("Tunggu bentar! ")
