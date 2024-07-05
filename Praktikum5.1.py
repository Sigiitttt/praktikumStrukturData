def bubble_sort(daftar):
    n = len(daftar)
    ditukar = True
    while ditukar:
        ditukar = False
        for i in range(n-1):
            if daftar[i] < daftar[i+1]:
                daftar[i], daftar[i+1] = daftar[i+1], daftar[i] 
                ditukar = True 
                print("Pertukaran:", daftar)
        n -= 1  
        print("Iterasi berikutnya:", daftar)

# Contoh penggunaan:
daftar_angka = [23, 47, 21, 12, 22, 11, 78]
print("Array sebelum diurutkan:", daftar_angka)
bubble_sort(daftar_angka)
print("Array setelah diurutkan:", daftar_angka)