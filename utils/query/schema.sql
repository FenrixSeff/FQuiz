CREATE TABLE IF NOT EXISTS riwayat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT,
    pelajaran TEXT,
    batas_waktu TEXT,
    waktu_tersisa TEXT,
    mulai_mengerjakan TEXT,
    benar INTEGER,
    salah INTEGER,
    nilai REAL
    );
