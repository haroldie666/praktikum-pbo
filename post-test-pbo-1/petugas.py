class Petugas:
    total_petugas = 0

    def __init__(self, nama, id_petugas):
        self.nama = nama
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

    def layani_donor(self, pendonor, bank_darah):
        print(f"\nPetugas {self.nama} sedang memproses donor atas nama {pendonor.nama}")
        if pendonor.cek_kelayakan():
            print(f"Proses donor darah {pendonor.golongan_darah} berhasil dilakukan")
            bank_darah.stok_darah = bank_darah.stok_darah + 1