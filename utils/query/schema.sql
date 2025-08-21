CREATE TABLE IF NOT EXISTS riwayat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT,
    pelajaran TEXT,
    batas_waktu INTEGER,
    waktu_tersisa INTEGER,
    mulai_mengerjakan TEXT,
    benar INTEGER,
    salah INTEGER,
    nilai REAL
    );
