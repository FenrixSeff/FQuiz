import os
import sqlite3
from pathlib import Path

lokasi_db = Path(__file__).parent.parent / ".riwayat/riwayat.db"

def konek_db():
    konek = sqlite3.connect(lokasi_db)
    kursor = konek.cursor()
    return konek, kursor

def simpan_riwayat(tgl, plj, bts_wkt, wkt_sisa, benar, salah, nilai):
    konek, kursor = konek_db()
    kursor.execute("""
        INSERT INTO riwayat
        (tanggal, pelajaran, batas_waktu, waktu_tersisa,
        benar, salah, nilai)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (tgl, plj, bts_wkt, wkt_sisa, benar, salah, nilai)
    )
    konek.commit()
    konek.close()

def buka_riwayat():
    _, kursor = konek_db()
    log = kursor.execute("""
        SELECT tanggal, pelajaran, batas_waktu,
        waktu_tersisa, benar, salah, nilai FROM riwayat
    """)
    os.system("clear")
    print("\n\n[≡] Riwayat\n")
    for tg, pl, bt_wk, wk_ss, bn, sl, nil in log.fetchall():
        print(
            f"| {tg} | {pl} | {bt_wk} | {wk_ss} | {bn} | {sl} | {nil} |")
    print()

def hapus_semua_riwayat():
    konek, kursor = konek_db()
    kursor.execute("""
        DELETE FROM riwayat
    """)
    konek.commit()
    konek.close()

def init_db():
    lokasi_db.touch(exist_ok=True)
    konek, kursor = konek_db()
    kursor.execute("""
        CREATE TABLE IF NOT EXISTS riwayat(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            pelajaran TEXT,
            batas_waktu TEXT,
            waktu_tersisa TEXT,
            benar INTEGER,
            salah INTEGER,
            nilai REAL
        )
    """)
    konek.commit()
    konek.close()

if __name__ == "__main__":
    simpan_riwayat()
    buka_riwayat()
    hapus_semua_riwayat()
    init_db()
