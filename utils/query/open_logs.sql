SELECT tanggal, kelas, pelajaran,
    batas_waktu, waktu_tersisa,
    mulai_mengerjakan, benar, salah, nilai
    FROM riwayat ORDER BY {base} {sorting} LIMIT ?;
