# Sistem Manajemen Bank Darah

> **Nama:** Syarafina Nur Amalia (NIM: 2509106016)
>
> **NIM:** NIM: 2509106016
>
> **Mata Kuliah:** Pemrograman Berorientasi Objek
>
> **Bahasa Pemrograman:** Python

---

## Daftar Isi

1. [Deskripsi Proyek](#deskripsi-proyek)
2. [Struktur Proyek](#struktur-proyek)
3. [Arsitektur & Desain OOP](#arsitektur--desain-oop)
4. [Penjelasan Kelas](#penjelasan-kelas)
5. [Fitur Aplikasi](#fitur-aplikasi)
6. [Alur Program](#alur-program)
7. [Cara Menjalankan](#cara-menjalankan)
8. [Contoh Penggunaan](#contoh-penggunaan)

---

## Deskripsi Proyek

Program **Sistem Manajemen Bank Darah** ini mensimulasikan operasional bank darah di mana petugas melayani pendonor, memvalidasi kelayakan, dan memperbarui ketersediaan kantong darah di berbagai cabang.

---

## Struktur Proyek

```
praktikum-pbo/
├── bank_darah.py      # Class BankDarah
├── pendonor.py        # Class Pendonor
├── petugas.py         # Class Petugas
├── main.py            # File eksekusi utama
└── README.md
```

---

## Arsitektur & Desain OOP

Proyek ini mengimplementasikan prinsip-prinsip OOP sebagai berikut:

### 1. Class & Object
Pembuatan cetak biru (*blueprint*) entitas sistem melalui class utama, di mana objek-objek berinteraksi satu sama lain (misalnya, objek `Petugas` berinteraksi dengan objek `Pendonor` dan `BankDarah` saat proses donor dilakukan).

### 2. Atribut (Instance & Kelas)
- **Atribut Kelas:** Variabel yang digunakan bersama oleh seluruh objek (seperti `total_kantong_darah`, `total_pendonor`, dan `total_petugas`).
- **Atribut Instance:** Data unik milik setiap objek yang diinisialisasi melalui konstruktor `__init__()`.

### 3. Encapsulation (Private & Validasi)
Penggunaan *access modifier* *Private* (menggunakan *double underscore* `__`) untuk menyembunyikan data sensitif seperti `__stok_darah`, `__ktp_pendonor`, dan `__id_petugas`. Akses data diatur melalui decorator `@property` (*Getter*) dan `@<nama_properti>.setter` (*Setter*) yang dilengkapi dengan validasi ketat dan *Exception Handling* (`raise ValueError`).

### 4. Jenis Method
- **Instance Method:** Mengolah data spesifik objek (contoh: `layani_donor()`).
- **Class Method (`@classmethod`):** Memodifikasi atribut kelas secara global menggunakan parameter `cls` (contoh: `update_total_global()`).
- **Static Method (`@staticmethod`):** Fungsi utilitas yang tidak terikat pada instance atau kelas (contoh: `validasi_format_id()`).

---

## Penjelasan Kelas

### 1. `BankDarah.py`
Merepresentasikan cabang bank darah yang menyimpan stok kantong darah.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `nama_instansi` | `String` | Atribut Kelas: Nama instansi utama bank darah |
| `total_kantong_darah` | `Integer` | Atribut Kelas: Total keseluruhan darah secara global |
| `lokasi_cabang` | `String` | Nama atau lokasi cabang bank darah |
| `kapasitas_tampung` | `Integer` | Kapasitas maksimum penyimpanan darah di cabang |
| `__stok_darah` | `Integer` | (Private) Jumlah stok darah saat ini. Memiliki validasi tidak boleh negatif dan tidak boleh melebihi kapasitas |

### 2. `Pendonor.py`
Merepresentasikan orang yang mendaftar untuk mendonorkan darahnya.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `total_pendonor` | `Integer` | Atribut Kelas: Total akumulasi pendonor terdaftar |
| `umur_minimal` | `Integer` | Atribut Kelas: Standar minimal umur pendonor (17 tahun) |
| `nama` | `String` | Nama lengkap pendonor |
| `umur` | `Integer` | Umur pendonor |
| `golongan_darah` | `String` | Golongan darah pendonor (A, B, AB, O) |
| `__ktp_pendonor` | `String` | (Private) Nomor KTP pendonor. Divalidasi minimal 5 karakter |

### 3. `Petugas.py`
Merepresentasikan admin/petugas yang melayani jalannya donor darah.

| Atribut | Tipe | Keterangan |
|---|---|---|
| `total_petugas` | `Integer` | Atribut Kelas: Total akumulasi petugas aktif |
| `nama` | `String` | Nama petugas |
| `__id_petugas` | `String` | (Private) ID petugas. Divalidasi wajib menggunakan awalan "PTG" |

---

## Fitur Aplikasi

| No | Fitur | Deskripsi |
|---|---|---|
| 1 | **Validasi Kelayakan Umur** | Menolak proses donor jika umur pendonor berada di bawah batas umur minimal. |
| 2 | **Layanan Proses Donor** | Petugas melayani pendonor, jika valid maka stok pada cabang bank darah akan otomatis bertambah. |
| 3 | **Rekapitulasi Data Terstruktur** | Menampilkan tabel rapi berisikan data pendonor, data cabang bank darah, dan rekap sistem global (menggunakan `PrettyTable`). |
| 4 | **Keamanan Data (Setter Validation)** | Menolak input stok darah berlebih/negatif, menolak format KTP salah, dan memvalidasi format ID Petugas. |

---

## Alur Program

```text
[Inisialisasi Objek]
    ├── Objek BankDarah (Pusat & Fakultas)
    ├── Objek Petugas (3 Petugas)
    └── Objek Pendonor (4 Pendonor)
         |
         v
[Proses Layanan]
    ├── Petugas memanggil metode layani_donor()
    ├── Cek umur minimal pendonor melalui cek_kelayakan()
    └── Jika layak, update jumlah stok di objek BankDarah terkait
         |
         v
[Tampilkan Laporan (PrettyTable)]
    ├── Cetak Tabel Data Pendonor (dengan status kelayakan)
    ├── Cetak Tabel Stok Bank Darah
    └── Cetak Tabel Rekapitulasi Global (dari Atribut Kelas)
         |
         v
[Uji Coba Validasi]
    ├── Test ubah KTP menjadi format salah -> Tampil Error (ValueError)
    ├── Test isi stok melebihi kapasitas -> Tampil Error (ValueError)
    └── Test input ID Petugas tanpa awalan "PTG" -> Tampil Error (ValueError)
```

---

## Cara Menjalankan

### Prasyarat
*Library* `prettytable` sudah terinstal. Jika belum, jalankan perintah berikut di terminal:
  ```bash
  pip install prettytable
  ```

### Langkah-langkah Menjalankan Program
1. *Clone* repositori ini (atau *download* file proyek):
   ```bash
   git clone https://github.com/haroldie666/praktikum-pbo.git
   ```
2. Buka terminal atau *command prompt*, lalu navigasikan ke dalam direktori proyek tempat file berada.
3. Jalankan file eksekusi utama dengan perintah:
   ```bash
   python main.py
   ```

---

## Contoh Penggunaan

```text
PROSES LAYANAN
Petugas Joko Anwar sedang memproses donor atas nama Senku
Proses donor darah O berhasil dilakukan

DATA PENDONOR TERDAFTAR
+--------------+--------+------+------------+------------------+
| KTP Pendonor |  Nama  | Umur | Gol. Darah | Status Kelayakan |
+--------------+--------+------+------------+------------------+
|    98712     | Senku  |  19  |     O      |      Layak       |
|    12345     | Kohaku |  16  |     A      |   Tidak Layak    |
+--------------+--------+------+------------+------------------+

Validasi melebihi kapasitas
Error : Kapasitas di Cabang Fakultas tidak memadai. Jumlah maksimalnya adalah 5
```