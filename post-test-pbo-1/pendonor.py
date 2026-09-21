class Pendonor:
    # Atribut Kelas
    total_pendonor = 0
    umur_minimal = 17

    def __init__(self, nama, umur, golongan_darah, id_pendonor):
        self.nama = nama
        self.umur = umur
        self.golongan_darah = golongan_darah
        self.__id_pendonor = None 
        self.id_pendonor = id_pendonor 
        
        Pendonor.total_pendonor += 1

    @property
    def id_pendonor(self):
        return self.__id_pendonor

    @id_pendonor.setter
    def id_pendonor(self, id_baru):
        if not id_baru or len(id_baru) < 5:
            raise ValueError("ID Pendonor tidak valid! Minimal harus 5 karakter.")
        self.__id_pendonor = id_baru

    def cek_kelayakan(self):
        if self.umur >= Pendonor.umur_minimal:
            return True
        print(f"Maaf, {self.nama} belum cukup umur (Minimal {Pendonor.umur_minimal} tahun).")
        return False