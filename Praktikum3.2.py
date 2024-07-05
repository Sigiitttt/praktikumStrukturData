def cek_kurung(ekspresi):
    tumpukan_buka = []  
    log_proses = [] 
    daftar_error = [] 
    for indeks, karakter in enumerate(ekspresi):
        if karakter in '([{':
            tumpukan_buka.append(karakter) 
            log_proses.append(f"push stack with --> {tumpukan_buka}")  
        elif karakter in ')]}':
            if tumpukan_buka:
                kurung_terakhir = tumpukan_buka.pop()
                log_proses.append(f"pop stack --> {tumpukan_buka}")
                if kurung_terakhir == '(' and karakter != ')':
                    daftar_error.append(f"Kurung buka '{kurung_terakhir}' tidak cocok dengan kurung tutup '{karakter}'")
                elif kurung_terakhir == '[' and karakter != ']':
                    daftar_error.append(f"Kurung buka '{kurung_terakhir}' tidak cocok dengan kurung tutup '{karakter}'")
                elif kurung_terakhir == '{' and karakter != '}':
                    daftar_error.append(f"Kurung buka '{kurung_terakhir}' tidak cocok dengan kurung tutup '{karakter}'")
            else:
                daftar_error.append(f"Kurung tutup '{karakter}' tidak memiliki pasangan")
    if tumpukan_buka:
        while tumpukan_buka:
            daftar_error.append(f"Kurung buka '{tumpukan_buka.pop()}' tidak memiliki pasangan")

    return not bool(tumpukan_buka), log_proses, daftar_error

string_ekspresi = "([4+5]/{9+8]*(3+2]}"

valid, log_proses, error = cek_kurung(string_ekspresi)

print(valid)
print('Proses cek :')
for i, proses in enumerate(log_proses, 1):
    print(f"{i}. {proses}")
print('Daftar Error:')
for i, kesalahan in enumerate(error, 1):
    print(f"{i}. {kesalahan}")