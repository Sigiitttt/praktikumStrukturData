def cek_prefix(ekspresi):
    saldo = 0 
    karakter_diperbolehkan = set("0123456789+-*/")
    for karakter in reversed(ekspresi):
      #pemeriksaan karakter
        if karakter not in karakter_diperbolehkan:
            return False
        if karakter.isdigit(): 
            saldo += 1
        else:                  
            saldo -= 1
          #pemeriksaan saldo
        if saldo <= 0: 
            return False
    return saldo == 1  

def konversi_prefix_infix(ekspresi):
    tumpukan_infix = []
    langkah = 1
    for karakter in reversed(ekspresi):
        print("Langkah", langkah, ":")
        print("Tumpukan Infix:", tumpukan_infix)
        if karakter.isdigit():  
            tumpukan_infix.append(karakter)
        else:                    
            operan1 = tumpukan_infix.pop()
            operan2 = tumpukan_infix.pop()
            tumpukan_infix.append(f"({operan1} {karakter} {operan2})") 
        langkah += 1
    return tumpukan_infix.pop()

# Contoh penggunaan
ekspresi_prefix = "-+2*234"
if cek_prefix(ekspresi_prefix):
    print((ekspresi_prefix),"Konversi ke Infix:", konversi_prefix_infix(ekspresi_prefix))
else:
    print("Ekspresi tidak valid")
