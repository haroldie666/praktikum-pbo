class NotifikasiEmail:
    def kirim_pesan(self, pengguna, pesan):
        print(f"Mengirim notifikasi email ke {pengguna.nama}: {pesan}")

class NotifikasiWA:
    def kirim_pesan(self, pengguna, pesan):
        print(f"Mengirim notifikasi WA ke {pengguna.nama}: {pesan}")

def kirim_notifikasi_sistem(kanal_notifikasi, pengguna, pesan):
    # Duck typing dan DIP
    kanal_notifikasi.kirim_pesan(pengguna, pesan)