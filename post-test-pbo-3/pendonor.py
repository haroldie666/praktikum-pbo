from pengguna import Pengguna

class Pendonor(Pengguna):
    def __init__(self, id_pengguna, nama, gol_darah, nik):
        super().__init__(id_pengguna, nama)
        self.gol_darah = gol_darah
        self.__nik = nik  # Atribut Private

    def tampilkan_peran(self):
        return f"Pendonor dengan golongan darah {self.gol_darah}."

    def verifikasi_data(self):
        # NIK hanya bisa diakses dari dalam metode kelas ini sendiri
        return len(self.nama) > 0 and self.gol_darah in ["A", "B", "AB", "O"] and len(self.__nik) == 16

    def lakukan_donor(self, bank_darah, volume):
        print(f"\n{self.nama} sedang mendonorkan {volume} ml darah...")
        bank_darah.proses_donor(self.gol_darah, volume)

    def __str__(self):
        return f"Pendonor({self.nama}, Gol={self.gol_darah})"