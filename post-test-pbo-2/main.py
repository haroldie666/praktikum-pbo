from bank_darah import BankDarah
from pendonor import Pendonor
from petugas import Petugas

bank_pusat = BankDarah("Cabang Pusat", 100)
bank_fakultas = BankDarah("Cabang Fakultas", 5)

petugas1 = Petugas("joko_ptg", "Joko Anwar", 35, "PTG-001")
petugas2 = Petugas("yoga_ptg", "Yoga Ananda", 28, "PTG-002")

bank_pusat.tambah_petugas(petugas1)
bank_fakultas.tambah_petugas(petugas2)

donor1 = Pendonor("senku123", "Senku", 19, "O", "98712")
donor2 = Pendonor("kohaku_chan", "Kohaku", 16, "A", "12345")

print(petugas1.info_profil()) 
print(donor1.info_profil())   

petugas1.layani_donor(donor1, bank_pusat) 
petugas2.layani_donor(donor2, bank_fakultas) 

bank_pusat.info_cabang()
bank_fakultas.info_cabang()

print(petugas1.tampilkan_id_sistem())