def pencarian_biner_dimodifikasi(daftar_data, data_dicari):
    indeks_ditemukan = []
    jumlah_iterasi = 0
    batas_bawah = 0
    batas_atas = len(daftar_data) - 1

    while batas_bawah <= batas_atas:
        tengah = (batas_bawah + batas_atas) // 2
        nilai_tengah = daftar_data[tengah]

        if nilai_tengah == data_dicari:
            indeks_ditemukan.append(tengah)
            jumlah_iterasi += 1

            # Cari ke kiri untuk menemukan semua elemen yang sama
            kiri = tengah - 1
            while kiri >= 0 and daftar_data[kiri] == data_dicari:
                indeks_ditemukan.append(kiri)
                kiri -= 1
                jumlah_iterasi += 1

            # Cari ke kanan untuk menemukan semua elemen yang sama
            kanan = tengah + 1
            while kanan <= batas_atas and daftar_data[kanan] == data_dicari:
                indeks_ditemukan.append(kanan)
                kanan += 1
                jumlah_iterasi += 1

            return indeks_ditemukan, jumlah_iterasi

        elif nilai_tengah < data_dicari:
            batas_bawah = tengah + 1
            jumlah_iterasi += 1
        else:
            batas_atas = tengah - 1
            jumlah_iterasi += 1

    return 'Data tidak ada', jumlah_iterasi

# Contoh penggunaan fungsi pencarian_biner_dimodifikasi
data = [1, 1, 5, 5, 5, 8, 9, 10, 12, 26]
hasil, iterasi = pencarian_biner_dimodifikasi(data, 5)
print("Posisi Data:", hasil)
print("Jumlah iterasi:", iterasi)
