def buat_tabel_hash(ukuran):
    return [None] * ukuran

def fungsi_hash(nilai, ukuran):
    return nilai % ukuran

def chaining(daftar_data, tabel_hash):
    for nilai in daftar_data:
        indeks = fungsi_hash(nilai, len(tabel_hash))
        if tabel_hash[indeks] is None:
            tabel_hash[indeks] = [nilai]
        else:
            tabel_hash[indeks].append(nilai)

# Contoh penggunaan
daftar_angka = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ukuran_tabel_hash = 11
tabel_hash = buat_tabel_hash(ukuran_tabel_hash)

chaining(daftar_angka, tabel_hash)
print(tabel_hash)