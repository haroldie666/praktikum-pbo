from abc import ABC, abstractmethod

class Pengguna(ABC):
    def __init__(self, id_pengguna, nama):
        self._id_pengguna = id_pengguna  # Protected attribute
        self.nama = nama

    def tampilkan_info_umum(self):
        # Method konkret, dipakai oleh semua subclass
        return f"ID: {self._id_pengguna} | Nama: {self.nama}"

    @abstractmethod
    def tampilkan_peran(self):
        # Harus diimplementasikan oleh subclass
        pass

    @abstractmethod
    def verifikasi_data(self):
        # Harus diimplementasikan oleh subclass
        pass