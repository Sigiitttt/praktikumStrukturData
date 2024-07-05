class Node:
    def __init__(self, data):
        self.data = data
        self.berikutnya = None

class DaftarTertaut:
    def __init__(self):
        self.kepala = None

    def tambah_di_akhir(self, data):
        simpul_baru = Node(data)
        if not self.kepala:
            self.kepala = simpul_baru
            return
        simpul_terakhir = self.kepala
        while simpul_terakhir.berikutnya:
            simpul_terakhir = simpul_terakhir.berikutnya
        simpul_terakhir.berikutnya = simpul_baru

    def tambah_di_awal(self, data):
        simpul_baru = Node(data)
        simpul_baru.berikutnya = self.kepala
        self.kepala = simpul_baru

    def sisipkan_setelah_simpul(self, data_simpul_sebelumnya, data):
        simpul_saat_ini = self.kepala
        while simpul_saat_ini and simpul_saat_ini.data != data_simpul_sebelumnya:
            simpul_saat_ini = simpul_saat_ini.berikutnya
        if not simpul_saat_ini:
            print("Simpul dengan data", data_simpul_sebelumnya, "tidak ditemukan.")
            return
        simpul_baru = Node(data)
        simpul_baru.berikutnya = simpul_saat_ini.berikutnya
        simpul_saat_ini.berikutnya = simpul_baru

    def hapus_simpul(self, kunci):
        simpul_saat_ini = self.kepala
        if simpul_saat_ini and simpul_saat_ini.data == kunci:
            self.kepala = simpul_saat_ini.berikutnya
            simpul_saat_ini = None
            return
        simpul_sebelumnya = None
        while simpul_saat_ini and simpul_saat_ini.data != kunci:
            simpul_sebelumnya = simpul_saat_ini
            simpul_saat_ini = simpul_saat_ini.berikutnya
        if not simpul_saat_ini:
            print("Simpul dengan data", kunci, "tidak ditemukan.")
            return
        simpul_sebelumnya.berikutnya = simpul_saat_ini.berikutnya
        simpul_saat_ini = None

    def hapus_depan(self):
        if not self.kepala:
            return
        sementara = self.kepala
        self.kepala = self.kepala.berikutnya
        sementara = None

    def hapus_akhir(self):
        if not self.kepala:
            return
        if not self.kepala.berikutnya:
            self.kepala = None
            return
        simpul_kedua_terakhir = self.kepala
        while simpul_kedua_terakhir.berikutnya.berikutnya:
            simpul_kedua_terakhir = simpul_kedua_terakhir.berikutnya
        simpul_kedua_terakhir.berikutnya = None

    def cetak_daftar(self):
        simpul_saat_ini = self.kepala
        while simpul_saat_ini:
            print(simpul_saat_ini.data, end=" -> ")
            simpul_saat_ini = simpul_saat_ini.berikutnya
        print("None")

# Inisialisasi linked list
daftar = DaftarTertaut()

# Menambahkan node awal
daftar.tambah_di_akhir(100)
daftar.tambah_di_akhir(200)
daftar.tambah_di_akhir(300)
daftar.tambah_di_akhir(400)

# Menambahkan node baru sesuai instruksi
daftar.tambah_di_akhir(500)  # Tambah 500 di belakang
daftar.tambah_di_awal(50)  # Tambah 50 di depan
daftar.sisipkan_setelah_simpul(200, 250)  # Tambah 250 setelah 200

# Menghapus node sesuai instruksi
# daftar.hapus_depan()  # Hapus node depan
# daftar.hapus_akhir()  # Hapus node belakang
# daftar.hapus_simpul(300)  # Hapus node dengan data 300

# Akses semua data
daftar.cetak_daftar()  # Output: 100 -> 200 -> 250 -> 400 -> None