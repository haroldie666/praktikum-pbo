# Clas super yang akan diwarisi oleh petugas dan donor
class Pengguna:
    def __init__(self, username, nama, umur):
        self._username = username
        self._nama = nama
        self._umur = umur
        self.__id_sistem = f"SYS-{id(self)}"

    @property
    def nama(self):
        return self._nama

    @property
    def umur(self):
        return self._umur

    def info_profil(self):
        return f"Username: {self._username} | Nama: {self._nama}, Umur: {self._umur} tahun"

    def tampilkan_id_sistem(self):
        return self.__id_sistem