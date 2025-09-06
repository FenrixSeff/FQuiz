SELECT tanggal, pelajaran,
    batas_waktu, waktu_tersisa,
    mulai_mengerjakan, benar, salah, nilai
    FROM riwayat ORDER BY id {sorting} LIMIT ?;
