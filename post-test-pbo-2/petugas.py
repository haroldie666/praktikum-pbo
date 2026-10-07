from pengguna import Pengguna

class Petugas(Pengguna):
    total_petugas = 0

    def __init__(self, username, nama, umur, id_petugas):
        # Memanggil konstruktor superclass Pengguna menggunakan super()
        super().__init__(username, nama, umur)
        
        # Atribut tambahan spesifik milik subclass
        self.__id_petugas = None
        self.id_petugas = id_petugas
        
        Petugas.total_petugas += 1

    @property
    def id_petugas(self):
        return self.__id_petugas

    @id_petugas.setter
    def id_petugas(self, id_baru):
        if not Petugas.validasi_format_id(id_baru):
            raise ValueError("ID petugas tidak valid (harus diawali dengan 'PTG')")
        self.__id_petugas = id_baru

    @staticmethod
    def validasi_format_id(id_teks):
        return str(id_teks).startswith("PTG")

    # Relasi Asosiasi
    def layani_donor(self, pendonor, bank_darah):
        print(f"\nPetugas {self._nama} sedang memproses donor atas nama {pendonor.nama}")
        if pendonor.cek_kelayakan():
            try:
                bank_darah.stok_darah = bank_darah.stok_darah + 1
                print(f"Proses donor darah {pendonor.golongan_darah} berhasil dilakukan")
            except ValueError as e:
                print(f"Proses gagal karena {e}")

    def info_profil(self):
        return f"[Petugas] {self._nama} (@{self._username}) dengan ID: {self.id_petugas}"