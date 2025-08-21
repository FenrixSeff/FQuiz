import sqlite3
from pathlib import Path

DEFAULT = {
    "folder_qy": Path(__file__).parent / "query",
    "folder_db": Path(__file__).parent.parent / ".riwayat/riwayat.db",
    "init": "schema.sql",
    "simpan": "add_logs.sql",
    "buka": "open_logs.sql",
    "hapus": "del_logs.sql"
    }

class DatabaseHandler:
    def __init__(self,
                 lokasi_db=DEFAULT["folder_db"],
                 lokasi_qy=DEFAULT["folder_qy"]):

        self.db = Path(lokasi_db)
        self.qy = Path(lokasi_qy)
        self.db.parent.mkdir(parents=True, exist_ok=True)

    def _konek_db(self):
        return sqlite3.connect(self.db)

    def _parse_sql(self, nama_file):
        lokasi = self.qy / nama_file
        try:
            with open(lokasi, "r", encoding="utf-8") as f:
                query = f.read()
            return query
        except FileNotFoundError:
            raise FileNotFoundError(
                f"file SQL tidak ditemukan di: {lokasi}")

    def execute_script(self, query):
        with self._konek_db() as konek:
            konek.executescript(query)

    def execute_query(self, query, param=(), fetch=None):
        with self._konek_db() as konek:
            kursor = konek.cursor()
            kursor.execute(query, param)
            if fetch == "one":
                return kursor.fetchone()
            elif fetch == "all":
                return kursor.fetchall()

class RiwayatHandler(DatabaseHandler):
    def __init__(self,
                 lokasi_db=DEFAULT["folder_db"],
                 lokasi_qy=DEFAULT["folder_qy"]):

        super().__init__(lokasi_db, lokasi_qy)
        self.fqy_init = DEFAULT["init"]
        self.fqy_simpan = DEFAULT["simpan"]
        self.fqy_buka = DEFAULT["buka"]
        self.fqy_hapus = DEFAULT["hapus"]

    def init_db(self):
        query = self._parse_sql(self.fqy_init)
        self.execute_script(query)

    def simpan_riwayat(self, tanggal, pelajaran, batas_waktu,
                       waktu_tersisa, mulai_mengerjakan,
                       benar, salah, nilai):

        query = self._parse_sql(self.fqy_simpan)
        param = (tanggal, pelajaran, batas_waktu, waktu_tersisa,
                 mulai_mengerjakan, benar, salah, nilai)
        self.execute_query(query, param)

    def buka_riwayat(self, tampilkan="all"):
        query = self._parse_sql(self.fqy_buka)
        return self.execute_query(query, fetch=tampilkan)

    def hapus_semua_riwayat(self):
        query = self._parse_sql(self.fqy_hapus)
        self.execute_query(query)

if __name__ == "__main__":
    print("jqq10qjsb")
