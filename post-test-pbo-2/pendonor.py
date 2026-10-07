from pengguna import Pengguna

class Pendonor(Pengguna):
    total_pendonor = 0
    umur_minimal = 17

    def __init__(self, username, nama, umur, golongan_darah, ktp_pendonor):
        # Memanggil konstruktor superclass Pengguna menggunakan super()
        super().__init__(username, nama, umur)
        
        # Atribut tambahan spesifik milik subclass
        self.golongan_darah = golongan_darah
        self.__ktp_pendonor = None 
        self.ktp_pendonor = ktp_pendonor 
        Pendonor.total_pendonor += 1

    @property
    def ktp_pendonor(self):
        return self.__ktp_pendonor

    @ktp_pendonor.setter
    def ktp_pendonor(self, id_baru):
        if not id_baru or len(id_baru) < 5:
            raise ValueError("Nomor KTP tidak valid")
        self.__ktp_pendonor = id_baru

    def cek_kelayakan(self):
        if self._umur >= Pendonor.umur_minimal:
            return True
        print(f"Maaf {self._nama}, umur pendonor minimal {Pendonor.umur_minimal} tahun")
        return False
    
    def info_profil(self):
        return f"[Pendonor] {self._nama} (@{self._username}) | Gol Darah: {self.golongan_darah} | KTP: {self.ktp_pendonor}"