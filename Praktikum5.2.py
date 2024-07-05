def selection_sort(daftar):
    n = len(daftar)
    for i in range(n // 2):
        indeks_minimum = i
        indeks_maksimum = i
        for j in range(i + 1, n - i): 
            if daftar[j] < daftar[indeks_minimum]:
                indeks_minimum = j
            elif daftar[j] > daftar[indeks_maksimum]:
                indeks_maksimum = j

        if indeks_minimum != i:
            daftar[i], daftar[indeks_minimum] = daftar[indeks_minimum], daftar[i]
        if indeks_maksimum != n - i - 1:
            daftar[n - i - 1], daftar[indeks_maksimum] = daftar[indeks_maksimum], daftar[n - i - 1]

        print("Iterasi ke-", i+1, ":", daftar)

# Contoh penggunaan:
daftar_angka = [14, 8, 78, 32, 67, 22, 75]
print("Array sebelum diurutkan:", daftar_angka)
selection_sort(daftar_angka)
print("Array setelah diurutkan:", daftar_angka)