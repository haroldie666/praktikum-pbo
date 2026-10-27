from prettytable import PrettyTable
from kantong_darah import KantongDarah
from petugas import Petugas

class BankDarah:
    def __init__(self, nama_cabang):
        self.nama_cabang = nama_cabang
        self._daftar_petugas = [] # Agregasi 
        self._stok_darah = []     # Komposisi 

    def tambah_petugas(self, petugas):
        # Petugas ditambahkan dari luar sistem, penerapan agregasi
        if isinstance(petugas, Petugas):
            self._daftar_petugas.append(petugas)
            print(f"Petugas {petugas.nama} ditugaskan ke {self.nama_cabang}.")

    def proses_donor(self, gol_darah, volume):
        # KantongDarah dibuat di dalam kelas parent, penerapan komposisi
        id_baru = f"KD-{len(self._stok_darah) + 1:03d}"
        kantong = KantongDarah(id_baru, gol_darah, volume)
        self._stok_darah.append(kantong)
        print(f"Stok masuk: {kantong}")

    def tampilkan_daftar_petugas(self):
        tabel = PrettyTable()
        tabel.field_names = ["ID Petugas", "Nama", "Shift"]
        
        for petugas in self._daftar_petugas:
            # Mengakses atribut protected _id_pengguna dari parent class
            tabel.add_row([petugas._id_pengguna, petugas.nama, petugas.shift])
            
        print(tabel)

    def tampilkan_stok_darah(self):
        tabel = PrettyTable()
        tabel.title = f"Stok Kantong Darah - {self.nama_cabang}"
        tabel.field_names = ["ID Kantong", "Golongan Darah", "Volume (ml)"]
        
        for kantong in self._stok_darah:
            tabel.add_row([kantong.id_kantong, kantong.gol_darah, kantong.volume])
            
        print(tabel)

    def __len__(self):
        # Operator overloading
        return len(self._stok_darah)