from prettytable import PrettyTable
from bank_darah import BankDarah
from pendonor import Pendonor
from petugas import Petugas

# membuat objek
bank_pusat = BankDarah("Cabang Pusat", 100)
bank_fakultas = BankDarah("Cabang Fakultas", 5)

petugas1 = Petugas("Joko Anwar", "PTG-001")
petugas2 = Petugas("Yoga Ananda", "PTG-002")
petugas2 = Petugas("Yoga Ananda", "PTG-003")

donor1 = Pendonor("Senku", 19, "O", "98712")
donor2 = Pendonor("Kohaku", 16, "A", "12345")
donor3 = Pendonor("Gen", 20, "AB", "33445")
donor4 = Pendonor("Krotago", 21, "B", "88776")

print("PROSES LAYANAN")
petugas1.layani_donor(donor1, bank_pusat) 
petugas2.layani_donor(donor2, bank_fakultas) 
print()

print("DATA PENDONOR TERDAFTAR")
tabel_donor = PrettyTable()
tabel_donor.field_names = ["KTP Pendonor", "Nama", "Umur", "Gol. Darah", "Status Kelayakan"]

tabel_donor.add_row([donor1.ktp_pendonor, donor1.nama, donor1.umur, donor1.golongan_darah, "Layak" if donor1.umur >= Pendonor.umur_minimal else "Tidak Layak"])
tabel_donor.add_row([donor2.ktp_pendonor, donor2.nama, donor2.umur, donor2.golongan_darah, "Layak" if donor2.umur >= Pendonor.umur_minimal else "Tidak Layak"])
print(tabel_donor)
print()

print("DATA STOK BANK DARAH")
tabel_bank = PrettyTable()
tabel_bank.field_names = ["Lokasi Cabang", "Kapasitas Tampung", "Stok Tersedia"]
tabel_bank.add_row([bank_pusat.lokasi_cabang, bank_pusat.kapasitas_tampung, bank_pusat.stok_darah])
tabel_bank.add_row([bank_fakultas.lokasi_cabang, bank_fakultas.kapasitas_tampung, bank_fakultas.stok_darah])
print(tabel_bank)
print()

print("REKAPITULASI SISTEM")
tabel_rekap = PrettyTable()
tabel_rekap.field_names = ["Keterangan", "Total"]
tabel_rekap.add_row(["Total Kantong Darah Global", f"{BankDarah.total_kantong_darah} kantong"])
tabel_rekap.add_row(["Total Pendonor Terdaftar", f"{Pendonor.total_pendonor} orang"])
tabel_rekap.add_row(["Total Petugas Aktif", f"{Petugas.total_petugas} orang"])
print(tabel_rekap)

print("\nValidasi KTP pendonor yang berhasil")
donor1.ktp_pendonor = "22334"
print(f"KTP Pendonor {donor1.nama} berhasil diperbarui menjadi {donor1.ktp_pendonor}")

print("\nValidasi KTP pendonor yang salah")
try:
    donor1.ktp_pendonor = "DNR"
except ValueError as e:
    print(f"Error : {e}")

print("\nValidasi melebihi kapasitas")
try:
    bank_fakultas.stok_darah = 10 
except ValueError as e:
    print(f"Error : {e}")

print("\nID petugas tidak valid")
try:
    petugas2.id_petugas = "ADMIN-02"
except ValueError as e:
    print(f"Error : {e}")