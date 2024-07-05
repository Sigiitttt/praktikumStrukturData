class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

class Antriann:
    def __init__(self):
        self.antrian = Stack()
        self.nomor_berikutnya = 1  

    def tambah_pelanggan(self, nama_pelanggan):
        self.antrian.push((self.nomor_berikutnya, nama_pelanggan)) 
        print(f"Pelanggan {nama_pelanggan} dengan nomor antrian {self.nomor_berikutnya} telah ditambahkan ke antrian.")
        self.nomor_berikutnya += 1 # ditambah 1

    def layani_pelanggan(self): #lifo
        if not self.antrian.is_empty():
            nomor, nama_pelanggan = self.antrian.pop() 
            print(f"Melayani pelanggan {nama_pelanggan} dengan nomor antrian {nomor}.")
        else:
            print("Tidak ada pelanggan yang sedang menunggu.")

    def tampilkan_antrian(self):
        if self.antrian.is_empty(): 
            print("Antrian kosong.")
        else:
            print("Status Antrian Saat Ini:")
            temp_stack = Stack()
            while not self.antrian.is_empty():
                nomor, nama_pelanggan = self.antrian.pop()
                print(f"Nomor Antrian: {nomor}, Nama Pelanggan: {nama_pelanggan}")
                temp_stack.push((nomor, nama_pelanggan))
            while not temp_stack.is_empty():
                nomor, nama_pelanggan = temp_stack.pop()
                self.antrian.push((nomor, nama_pelanggan))

# Simulasi Antrian
restoran = Antriann()

while True:
    opsi = input("1. Tambah Pelanggan\n2. Layani Pelanggan\n3. Tampilkan Antrian\n4. Keluar\nPilih operasi (1/2/3/4): ")
    if opsi == '1':
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        restoran.tambah_pelanggan(nama_pelanggan)
    elif opsi == '2':
        restoran.layani_pelanggan()
    elif opsi == '3':
        restoran.tampilkan_antrian()
    elif opsi == '4':
        print("ws hop baliko sesok")
        break
    else:
        print("Input tidak valid, mohon masukkan pilihan yang benar.")