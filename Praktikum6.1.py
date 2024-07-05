def cari_sekuensial(daftar, target):
    jumlah_iterasi = 0
    indeks = []

    for i in range(len(daftar)):
        jumlah_iterasi += 1
        if daftar[i] == target:
            indeks.append(i)

    if indeks:  # Memeriksa apakah list indeks tidak kosong
        return indeks, jumlah_iterasi
    else:
        return "Data tidak ada", jumlah_iterasi

data = [1, 5, 9, 8, 1, 5, 10, 26, 5, 12]
hasil, jumlah_iterasi = cari_sekuensial(data, 5)
print("Posisi Data:", hasil)
print("Jumlah iterasi:", jumlah_iterasi)
