from pengguna import Pengguna

class Petugas(Pengguna):
    def __init__(self, id_pengguna, nama, shift):
        super().__init__(id_pengguna, nama)
        self.shift = shift

    # Method overriding diubah menjadi return
    def tampilkan_peran(self):
        return f"Petugas shift {self.shift}."

    def verifikasi_data(self):
        return len(self._id_pengguna) >= 3