def gpp(daftar):
    n = len(daftar)
    for i in range(1, n):
        kunci = daftar[i]
        j = i - 1 
        if daftar[j] <= kunci:
            continue
        while j >= 0 and daftar[j] > kunci:
            daftar[j + 1] = daftar[j]
            j -= 1 
        daftar[j + 1] = kunci
        print("Iterasi ke-", i, ":", daftar)

daftar_angka = [47, 25, 31, 12, 78, 11, 82]
print("Array sebelum diurutkan:", daftar_angka)
gpp(daftar_angka)
print("Array setelah diurutkan:", daftar_angka)