class CatatanDonasi:
    def __init__(self, id_catatan, jumlah, keterangan):
        self.id_catatan = id_catatan
        self.jumlah = jumlah
        self.keterangan = keterangan
        
    def __str__(self):
        return f"[{self.id_catatan}] +{self.jumlah} kantong | Ket: {self.keterangan}"

class BankDarah:
    nama_instansi = "Bank Darah Mulawarman"
    total_kantong_darah = 0

    def __init__(self, lokasi_cabang, kapasitas_tampung):
        self.lokasi_cabang = lokasi_cabang
        self.kapasitas_tampung = kapasitas_tampung
        self.__stok_darah = 0
        self._daftar_petugas = [] 
        self._riwayat_donasi = [] 

    @property
    def stok_darah(self):
        return self.__stok_darah

    @stok_darah.setter
    def stok_darah(self, jumlah):
        if jumlah < 0:
            raise ValueError("Stok darah tidak boleh bernilai negatif")
        if jumlah > self.kapasitas_tampung:
            raise ValueError(f"Kapasitas di {self.lokasi_cabang} tidak memadai.")
        
        selisih = jumlah - self.__stok_darah
        if selisih > 0:
            self._buat_catatan(selisih, "Penambahan stok donasi darah")
            
        self.__stok_darah = jumlah
        BankDarah.update_total_global(selisih)

    def _buat_catatan(self, jumlah, keterangan):
        id_baru = f"DON-{len(self._riwayat_donasi) + 1:04d}"
        catatan = CatatanDonasi(id_baru, jumlah, keterangan)
        self._riwayat_donasi.append(catatan)

    def tambah_petugas(self, petugas):
        self._daftar_petugas.append(petugas)
        print(f"Petugas {petugas.nama} ditugaskan di {self.lokasi_cabang}")

    def info_cabang(self):
        print(f"Stok Tersedia: {self.stok_darah}/{self.kapasitas_tampung} kantong")
        print(f"Total Petugas: {len(self._daftar_petugas)} orang")
        print("Riwayat Donasi:")
        if not self._riwayat_donasi:
            print("Belum ada riwayat masuk")
        for catatan in self._riwayat_donasi:
            print(catatan)

    @classmethod
    def update_total_global(cls, jumlah):
        cls.total_kantong_darah += jumlah