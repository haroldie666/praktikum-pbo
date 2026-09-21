class BankDarah:
    # Atribut Kelas
    nama_instansi = "PMI Mulawarman"
    total_kantong_darah = 0

    def __init__(self, lokasi_cabang, kapasitas_tampung):
        self.lokasi_cabang = lokasi_cabang
        self.kapasitas_tampung = kapasitas_tampung
        self.__stok_darah = 0

    @property
    def stok_darah(self):
        return self.__stok_darah

    @stok_darah.setter
    def stok_darah(self, jumlah):
        if jumlah < 0:
            raise ValueError("Stok darah tidak boleh bernilai negatif!")
        if jumlah > self.kapasitas_tampung:
            raise ValueError(f"Kapasitas di {self.lokasi_cabang} tidak cukup! Maksimal: {self.kapasitas_tampung}")
        
        selisih = jumlah - self.__stok_darah
        self.__stok_darah = jumlah
        BankDarah.update_total_global(selisih)

    def info_cabang(self):
        print(f"[{self.lokasi_cabang}] Stok: {self.stok_darah}/{self.kapasitas_tampung} kantong.")

    @classmethod
    def update_total_global(cls, jumlah):
        cls.total_kantong_darah += jumlah