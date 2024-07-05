def temukan_semua_jalur(graf, mulai, akhir, jalur=[]):
    jalur = jalur + [mulai]
    if mulai == akhir:
        return [jalur]
    if mulai not in graf:
        return []
    semua_jalur = []
    for simpul in graf[mulai]:
        if simpul not in jalur:
            jalur_baru = temukan_semua_jalur(graf, simpul, akhir, jalur)
            for jalur_baru_tunggal in jalur_baru:
                semua_jalur.append(jalur_baru_tunggal)
    return semua_jalur

def temukan_jalur_terpendek(jalur):
    panjang_minimum = min(len(jalur_tunggal) for jalur_tunggal in jalur)
    jalur_terpendek = [jalur_tunggal for jalur_tunggal in jalur if len(jalur_tunggal) == panjang_minimum]
    return jalur_terpendek

def temukan_jalur_terpanjang(jalur):
    panjang_maksimum = max(len(jalur_tunggal) for jalur_tunggal in jalur)
    jalur_terpanjang = [jalur_tunggal for jalur_tunggal in jalur if len(jalur_tunggal) == panjang_maksimum]
    return jalur_terpanjang

# Definisikan graf berdasarkan gambar yang diberikan
graf = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['a', 'c', 'e'],
    'e': ['b', 'c', 'd']
}

# Contoh penggunaan
simpul_awal = 'a'
simpul_akhir = 'e'
semua_jalur = temukan_semua_jalur(graf, simpul_awal, simpul_akhir)
jalur_terpendek = temukan_jalur_terpendek(semua_jalur)
jalur_terpanjang = temukan_jalur_terpanjang(semua_jalur)

print("Semua Jalur:")
for jalur in semua_jalur:
    print(jalur)

print("\nJalur Terpendek:")
for jalur in jalur_terpendek:
    print(jalur)

print("\nJalur Terpanjang:")
for jalur in jalur_terpanjang:
    print(jalur)