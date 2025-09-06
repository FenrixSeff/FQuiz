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
    """
    Kelas dasar generik untuk menangani operasi database SQLite.

    Kelas ini menyediakan fungsionalitas inti seperti koneksi ke
    database, membaca file query SQL, dan mengeksekusi query tersebut.
    Tujuannya adalah untuk diabstraksi oleh kelas lain yang
    lebih spesifik.

    Attributes:
        db (Path): Objek Path yang menunjuk ke file database SQLite.
        qy (Path): Objek Path yang menunjuk ke folder berisi file
            query SQL.
    """
    def __init__(self,
                 lokasi_db=DEFAULT["folder_db"],
                 lokasi_qy=DEFAULT["folder_qy"]):
        """
        Menginisialisasi DatabaseHandler.

        Args:
            lokasi_db (Path, optional): Path ke file database.
                Default ke `DEFAULT["folder_db"]`.

            lokasi_qy (Path, optional): Path ke folder query SQL.
                Default ke `DEFAULT["folder_qy"]`.
        """
        self.db = Path(lokasi_db)
        self.qy = Path(lokasi_qy)
        self.db.parent.mkdir(parents=True, exist_ok=True)


    def _konek_db(self):
        """
        Membuka koneksi ke database SQLite.
        """
        return sqlite3.connect(self.db)


    def _parse_sql(self, nama_file: str) -> str:
        """
        Membaca file .sql dan mengembalikan isinya sebagai string.

        Args:
            nama_file (str): Nama file SQL yang berada di dalam
                folder query.

        Returns:
            str: Isi dari file SQL sebagai string.

        Raises:
            FileNotFoundError: Jika file SQL yang ditentukan tidak
                ditemukan.
        """
        lokasi = self.qy / nama_file
        try:
            with open(lokasi, "r", encoding="utf-8") as f:
                query = f.read()
            return query
        except FileNotFoundError:
            raise FileNotFoundError(
                f"file SQL tidak ditemukan di: {lokasi}")


    def execute_script(self, query: str):
        """
        Mengeksekusi sebuah skrip SQL yang bisa berisi
            beberapa statement.

        Args:
            query (str): String SQL yang akan dieksekusi.
        """
        with self._konek_db() as konek:
            konek.executescript(query)


    def execute_query(self, query: str, param: tuple=()):
        """
        Mengeksekusi satu statement SQL, dengan dukungan parameter
            dan fetch.

        Args:
            query (str): String SQL tunggal yang akan dieksekusi.

            param (tuple, optional): Parameter untuk query
                (mencegah SQL Injection).
                Default ke tuple kosong.

        Returns:
            Semua baris table.
        """
        with self._konek_db() as konek:
            kursor = konek.cursor()
            kursor.execute(query, param)
            return kursor.fetchall()


class RiwayatHandler(DatabaseHandler):
    """
    Handler spesifik untuk mengelola data riwayat kuis dalam database.

    Kelas ini mewarisi `DatabaseHandler` dan mengimplementasikan
    metode-metode konkret untuk operasi CRUD (Create, Read, Update,
    Delete) pada tabel riwayat.
    """
    def __init__(self,
                 lokasi_db=DEFAULT["folder_db"],
                 lokasi_qy=DEFAULT["folder_qy"]):
        """
        Menginisialisasi RiwayatHandler.

        Args:
            lokasi_db (Path, optional): Path ke file database.

            lokasi_qy (Path, optional): Path ke folder query SQL.
        """
        super().__init__(lokasi_db, lokasi_qy)
        self.fqy_init = DEFAULT["init"]
        self.fqy_simpan = DEFAULT["simpan"]
        self.fqy_buka = DEFAULT["buka"]
        self.fqy_hapus = DEFAULT["hapus"]


    def init_db(self):
        """
        Menginisialisasi database dengan membuat tabel jika belum ada.

        Membaca `schema.sql` dan mengeksekusinya.
        """
        query = self._parse_sql(self.fqy_init)
        self.execute_script(query)


    def simpan_riwayat(self, tanggal: str, pelajaran: str,
                       batas_waktu: int, waktu_tersisa: int,
                       mulai_mengerjakan: str, benar: int,
                       salah: int, nilai: float):
        """
        Menyimpan satu record riwayat kuis ke dalam database.

        Args:
            tanggal (str): Tanggal kuis diselesaikan (format teks).

            pelajaran (str): Nama pelajaran atau topik kuis.

            batas_waktu (int): Durasi waktu yang diberikan (menit).

            waktu_tersisa (int): Sisa waktu saat kuis selesai (menit).

            mulai_mengerjakan (str): Waktu mulai kuis (format teks).

            benar (int): Jumlah jawaban benar.

            salah (int): Jumlah jawaban salah.

            nilai (float): Skor akhir yang didapat.
        """
        query = self._parse_sql(self.fqy_simpan)
        param = (tanggal, pelajaran, batas_waktu, waktu_tersisa,
                 mulai_mengerjakan, benar, salah, nilai)
        self.execute_query(query, param)


    def baca_riwayat(self, urutkan: str="terlama") -> list[tuple]:
        """
        Mengambil semua data riwayat dari database.

        Returns:
            List[Tuple]: Sebuah list berisi tuple, di mana setiap tuple
                merepresentasikan satu baris data riwayat.
        """
        parse = {
            "terbaru": "DESC", "baru": "DESC", "new": "DESC",
            "terlama": "ASC", "lama": "ASC", "old": "ASC"
        }
        urut = parse.get(urutkan.strip().lower(), "terlama")
        q = self._parse_sql(self.fqy_buka)
        query = q.format(sorting=urut)  # inject
        return self.execute_query(query, (20,)) # sementara max 20


    def hapus_semua_riwayat(self):
        """
        Menghapus semua record dari tabel riwayat.
        """
        query = self._parse_sql(self.fqy_hapus)
        self.execute_query(query)

if __name__ == "__main__":
    print("jqq10qjsb")
