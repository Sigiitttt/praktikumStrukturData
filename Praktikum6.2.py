def pencarian_sekuensial(angka, data_dicari):
    indeks_ditemukan = []
    jumlah_iterasi = 0

    for indeks, nilai in enumerate(angka):
        jumlah_iterasi += 1
        if nilai == data_dicari:
            indeks_ditemukan.append(indeks)

    # for indeks in range(len(angka)):
    #     jumlah_iterasi += 1
    #     if angka[indeks] == data_dicari:
    #         indeks_ditemukan.append(indeks)

    if indeks_ditemukan:  #memeriksa list indeks tidak kosong
        return indeks_ditemukan, jumlah_iterasi
    else:
        return 'data tidak ada', jumlah_iterasi

# Contoh penggunaan fungsi pencarian_sekuensial
angka = [1, 5, 9, 8, 1, 5, 10, 26, 5, 12]
hasil, iterasi = pencarian_sekuensial(angka, 0)
print("Posisi data =", hasil)
print("Jumlah iterasi =", iterasi)