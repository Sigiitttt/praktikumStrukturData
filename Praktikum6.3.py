def ordered_sequential(daftar, cari):
    jumlah_iterasi = 1
    ditemukan = [] # posisi
    indeks = 9  # loop
    while indeks > 0 and daftar[indeks] >= cari:
        if daftar[indeks] == cari:
            ditemukan.append(indeks)
        indeks -= 1
        jumlah_iterasi += 1

    if ditemukan:
        return ditemukan, jumlah_iterasi
    else:
        return "Data tidak ada", jumlah_iterasi

daftar = [1, 1, 5, 5, 5, 8, 9, 10, 12, 26]
hasil, iterasi = ordered_sequential(daftar, 5)
print("Posisi Data:", hasil)
print("Jumlah iterasi:", iterasi)