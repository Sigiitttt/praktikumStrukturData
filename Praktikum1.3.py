def elemen_paling_umum(daftar_angka):
    jumlah_terbanyak = 0
    angka_terumum = None

    for angka in daftar_angka:
        jumlah = sum(1 for elemen in daftar_angka if elemen == angka)
        if jumlah > jumlah_terbanyak:
            angka_terumum = angka
            jumlah_terbanyak = jumlah

    return angka_terumum

daftar_angka = [4, 1, 4, 6]
print("Input:", daftar_angka)
print("Output:", elemen_paling_umum(daftar_angka))
print("Penjelasan: angka", elemen_paling_umum(daftar_angka), "paling sering muncul dalam list.")