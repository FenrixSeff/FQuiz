import sqlite3
from pathlib import Path

lokasi_db = Path(__file__).parent.parent / ".riwayat/riwayat.db"
lokasi_qy = Path(__file__).parent / "query"

DEFAULT_LOC_DB = {
    "default": lokasi_db
    }

DEFAULT_QUERY = {
    "folder_qy": lokasi_qy,
    "init": "schema.sql",
    "simpan": "add_logs.sql",
    "buka": "open_logs.sql",
    "hapus": "del_logs.sql"
    }

class DatabaseHandler:
    def __init__(self, lokasi_db=DEFAULT_LOC_DB["default"],
                 lokasi_qy=DEFAULT_QUERY["folder_qy"]):
        self.db = Path(lokasi_db)
        self.qy = Path(lokasi_qy)
        self.konek = sqlite3.connect(self.db)
        self.kursor = self.konek.cursor()

    def finalize(self):
        self.konek.commit()
        self.konek.close()

    def parse_sql(self, target):
        try:
            with open(target, "r", encoding="utf-8") as f:
                query = f.read()
            return query
        except FileNotFoundError:
            raise FileNotFoundError(f"file SQL {target} tidak ditemukan")

    def init_db(self, fqy_init=DEFAULT_QUERY["init"]):
        self.db.touch(exist_ok=True)
        query = self.parse_sql(self.qy / fqy_init)
        self.kursor.executescript(query)
        self.finalize()

class RiwayatHandler(DatabaseHandler):
    def __init__(self,
                 lokasi_db=DEFAULT_LOC_DB["default"],
                 lokasi_qy=DEFAULT_QUERY["folder_qy"],
                 fqy_simpan=DEFAULT_QUERY["simpan"],
                 fqy_buka=DEFAULT_QUERY["buka"],
                 fqy_hapus=DEFAULT_QUERY["hapus"]):

        super().__init__(lokasi_db, lokasi_qy)
        self.fqy_simpan = Path(lokasi_qy / fqy_simpan)
        self.fqy_buka = Path(lokasi_qy / fqy_buka)
        self.fqy_hapus = Path(lokasi_qy / fqy_hapus)

    def simpan_riwayat(self, tanggal, pelajaran, batas_waktu,
                       waktu_tersisa, mulai_mengerjakan,
                       benar, salah, nilai):

        query = super().parse_sql(self.fqy_simpan)
        self.kursor.execute(query,(
            tanggal, pelajaran, batas_waktu,
            waktu_tersisa, mulai_mengerjakan,
            benar, salah, nilai
        ))
        super().finalize()

    def buka_riwayat(self):
        query = super().parse_sql(self.fqy_buka)
        return self.kursor.execute(query).fetchall()

    def hapus_semua_riwayat(self):
        query = super().parse_sql(self.fqy_hapus)
        self.kursor.execute(query)
        super().finalize()

if __name__ == "__main__":
    simpan_riwayat()
    buka_riwayat()
    hapus_semua_riwayat()
    init_db()
