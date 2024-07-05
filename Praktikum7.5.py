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

def cari_dalam_hash(nilai, tabel_hash):
    indeks = fungsi_hash(nilai, len(tabel_hash))
    slot = tabel_hash[indeks]
    if slot is not None:
        try:
            sub_indeks = slot.index(nilai)
            return f"Data berada di slot ke-{indeks}, dan indeks ke-{sub_indeks}"
        except ValueError:
            return False
    return False

# Contoh penggunaan
daftar_angka = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ukuran_tabel_hash = 11
tabel_hash = buat_tabel_hash(ukuran_tabel_hash)
chaining(daftar_angka, tabel_hash)

# Mencari data dalam tabel hash
print(cari_dalam_hash(66, tabel_hash))
print(cari_dalam_hash(54, tabel_hash))
print(cari_dalam_hash(20, tabel_hash))
print(cari_dalam_hash(55, tabel_hash))
print(cari_dalam_hash(100, tabel_hash))