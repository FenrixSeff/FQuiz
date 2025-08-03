import os
import sqlite3
from pathlib import Path

lokasi_db = Path(__file__).parent.parent / ".riwayat/riwayat.db"
lokasi_qy = Path(__file__).parent / "query"

def konek_db():
    konek = sqlite3.connect(lokasi_db)
    kursor = konek.cursor()
    return konek, kursor

def parse_sql(target):
    with open(target, "r", encoding="utf-8") as f:
        query = f.read()
    return query

def simpan_riwayat(tgl, plj, bts_wkt, wkt_sisa, benar, salah, nilai):
    konek, kursor = konek_db()
    query = parse_sql(lokasi_qy / "add_logs.sql")
    kursor.execute(query,(
        tgl, plj, bts_wkt, wkt_sisa, benar, salah, nilai
    ))
    konek.commit()
    konek.close()

def buka_riwayat():
    _, kursor = konek_db()
    query = parse_sql(lokasi_qy / "open_logs.sql")
    log = kursor.execute(query)
    return log.fetchall()

def hapus_semua_riwayat():
    konek, kursor = konek_db()
    query = parse_sql(lokasi_qy / "del_logs.sql")
    kursor.execute(query)
    konek.commit()
    konek.close()

def init_db():
    lokasi_db.touch(exist_ok=True)
    konek, kursor = konek_db()
    query = parse_sql(lokasi_qy / "schema.sql")
    kursor.executescript(query)
    konek.commit()
    konek.close()

if __name__ == "__main__":
    simpan_riwayat()
    buka_riwayat()
    hapus_semua_riwayat()
    init_db()
