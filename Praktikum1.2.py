def apakah_palindrom(angka):
    angka_str = str(angka)
    if angka_str == angka_str[::-1]:
        return True
    else:
        return False

angka = -125521
print("input : ", angka)
print("output : ", apakah_palindrom(angka))