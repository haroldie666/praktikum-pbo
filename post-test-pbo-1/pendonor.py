class Pendonor:
    total_pendonor = 0
    umur_minimal = 17

    def __init__(self, nama, umur, golongan_darah, ktp_pendonor):
        self.nama = nama
        self.umur = umur
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
        if self.umur >= Pendonor.umur_minimal:
            return True
        print(f"Maaf {self.nama}, umur pendonor minimal {Pendonor.umur_minimal} tahun")
        return False