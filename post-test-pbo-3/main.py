from pengguna import Pengguna
from pendonor import Pendonor
from petugas import Petugas
from bank_darah import BankDarah
from notifikasi import NotifikasiEmail, NotifikasiWA, kirim_notifikasi_sistem
from prettytable import PrettyTable

def main():
    print("\nPembuktian abstract class (pengguna) tidak bisa diinisiasi")
    try:
        user_anonim = Pengguna("U000", "Anonim")
    except TypeError as e:
        print(f"TypeError terjadi: {e}\n")

    bank_darah_mulawarman = BankDarah("PMI Samarinda")
    petugas1 = Petugas("P001", "Andi", "Pagi")
    petugas2 = Petugas("P002", "Budi", "Malam")
    pendonor1 = Pendonor("D001", "Syarafina Nur Amalia", "B", "1234000000000001")

    print("Relasi agregasi")
    bank_darah_mulawarman.tambah_petugas(petugas1)
    bank_darah_mulawarman.tambah_petugas(petugas2)

    print("\nPolimorfisme (pewarisan)")
    tabel_polimorfisme = PrettyTable()
    tabel_polimorfisme.title = "Data Pengguna & Role"
    tabel_polimorfisme.field_names = ["ID", "Nama", "Detail Peran"]
    tabel_polimorfisme.align = "l"

    daftar_pengguna = [petugas1, pendonor1]
    for user in daftar_pengguna:
        tabel_polimorfisme.add_row([user._id_pengguna, user.nama, user.tampilkan_peran()])

    print(tabel_polimorfisme)

    print("\nMethod konkret (diwariskan ke semua subclass)")
    tabel_konkret = PrettyTable()
    tabel_konkret.field_names = ["Kelas", "Info Umum"]
    tabel_konkret.align = "l"
    for user in daftar_pengguna:
        tabel_konkret.add_row([user.__class__.__name__, user.tampilkan_info_umum()])
    print(tabel_konkret)

    print("\nRelasi asosiasi dan komposisi")
    pendonor1.lakukan_donor(bank_darah_mulawarman, 350)
    pendonor1.lakukan_donor(bank_darah_mulawarman, 200)

    print("\nDaftar petugas di cabang")
    bank_darah_mulawarman.tampilkan_daftar_petugas()
    print()
    bank_darah_mulawarman.tampilkan_stok_darah()

    print("\nOperator overloading")
    print(pendonor1)
    print(f"Total kantong darah saat ini adalah: {len(bank_darah_mulawarman)}")

    print("\nAtribut private")
    try:
        print(pendonor1.__nik)
    except AttributeError as e:
        print(f"AttributeError terjadi: {e}")
        print("Atribut __nik bersifat private dan tidak bisa diakses langsung dari luar.")

    print("\nDuck typing dan solid")
    email = NotifikasiEmail()
    WA = NotifikasiWA()
    kirim_notifikasi_sistem(email, pendonor1, "Terima kasih atas donasi Anda.")
    kirim_notifikasi_sistem(WA, petugas1, "Shift pagi telah selesai.")

if __name__ == "__main__":
    main()