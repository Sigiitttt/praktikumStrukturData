def temukan_indeks_maksimal(angka):
    hasil_kali_terbesar = 0
    pasangan_indeks_terbesar = [0, 0]

    for i in range(len(angka)):
        for j in range(i + 1, len(angka)):
            hasil_kali = (angka[i] - 1) * (angka[j] - 1)
            if hasil_kali > hasil_kali_terbesar:
                hasil_kali_terbesar = hasil_kali
                pasangan_indeks_terbesar = [i, j]
    return pasangan_indeks_terbesar

data = [1, 5, 9, 10, 8]
indeks = temukan_indeks_maksimal(data)
hasil_kali_maksimal = (data[indeks[0]] - 1) * (data[indeks[1]] - 1)
print("input : data=", data)
print("Output : ", temukan_indeks_maksimal(data))
print("penjelasan : data pada indeks", indeks[0], "dan indeks", indeks[1],
      "menghasilkan perkalian maksimal, yaitu", (data[indeks[0]] - 1), "x", (data[indeks[1]] - 1))