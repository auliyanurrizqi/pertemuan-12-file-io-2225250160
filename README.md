
# Tugas 5 - Rekap Nilai dari File

## Identitas Mahasiswa
- **Nama:** Aulia Nurrizqi
- **NIM:** 2225250160
- **Kelas:** 3A

## Mata Kuliah
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Program Studi:** S1 Pendidikan Matematika
- **Pertemuan:** 12
- **Materi:** File Input-Output dan Penanganan Error Dasar

## Deskripsi Program
Program ini dibuat menggunakan Python untuk membaca, memvalidasi, dan mengolah data nilai mahasiswa dari file teks. Program menghitung jumlah data valid, rata-rata nilai, nilai minimum, nilai maksimum, serta jumlah mahasiswa yang lulus dan belum lulus.

Program menerapkan konsep file input-output dan penanganan error menggunakan `try-except` agar data yang tidak valid dapat dilewati tanpa menghentikan seluruh proses.

## Tujuan
1. Memahami penggunaan file input-output pada Python.
2. Membaca data dari file teks.
3. Memvalidasi format data mahasiswa.
4. Menangani error menggunakan `try-except`.
5. Menghitung statistik nilai mahasiswa.
6. Menyimpan hasil rekap ke dalam file teks.

## Struktur Folder

```text
pertemuan-12-file-io-NIM/
├── README.md
├── .gitignore
├── data/
│   ├── nilai.txt
│   └── hasil_rekap.txt
└── tugas/
    └── rekap_nilai_file.py
```

## Format File Input

Data disimpan dalam file `data/nilai.txt` dengan format NIM,nilai.

Contoh:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Data yang tidak valid, seperti nilai berupa teks `abc`, akan dilewati dan dilaporkan oleh program.

## Fitur Program
- Membaca data dari file `data/nilai.txt`.
- Melewati baris kosong.
- Memvalidasi format NIM dan nilai.
- Menangani `FileNotFoundError` dan `ValueError`.
- Menghitung jumlah data valid.
- Menghitung rata-rata nilai.
- Menentukan nilai minimum dan maksimum.
- Menghitung jumlah mahasiswa lulus dengan nilai minimal 60.
- Menyimpan hasil rekap ke `data/hasil_rekap.txt`.

## Cara Menjalankan Program

1. Buka folder proyek melalui Visual Studio Code.
2. Pastikan Python 3 sudah terpasang.
3. Siapkan file `data/nilai.txt`.
4. Buka terminal pada folder utama proyek.
5. Jalankan perintah berikut:

```bash
python tugas/rekap_nilai_file.py
```

Hasil rekap akan tersimpan pada file `data/hasil_rekap.txt`.

## Test Case

| Kasus | Kondisi | Hasil |
|---|---|---|
| Normal | Semua data valid | Data diproses dan statistik dihitung. |
| File hilang | File input tidak tersedia | Pesan file tidak ditemukan ditampilkan. |
| Nilai tidak valid | Nilai berisi teks `abc` | Baris dilewati, data lainnya tetap diproses. |
| Baris kosong | Terdapat baris kosong | Baris kosong dilewati. |
| Batas kelulusan | Nilai 60 | Mahasiswa dihitung lulus. |

## Hasil Pengujian

Berdasarkan data contoh pada file input:
- Jumlah data valid: 5
- Rata-rata nilai: 83.40
- Nilai minimum: 74.00
- Nilai maksimum: 92.00
- Jumlah mahasiswa lulus: 5
- Jumlah mahasiswa belum lulus: 0

## Error Handling

Program menangani beberapa kondisi error:
- **FileNotFoundError:** Terjadi ketika file input tidak ditemukan.
- **ValueError:** Terjadi ketika format data tidak sesuai atau nilai tidak dapat dikonversi menjadi angka.

Dengan penanganan error tersebut, data yang tidak valid dapat dilewati sehingga data lainnya tetap diproses.

## Refleksi

Melalui tugas ini, saya mempelajari cara membaca dan menulis file menggunakan Python, memvalidasi data, menghitung statistik nilai, serta menangani error menggunakan `try-except`. Saya juga memahami pentingnya penggunaan fungsi agar program lebih terstruktur dan mudah dipahami.

## Teknologi yang Digunakan
- Python 3
- Visual Studio Code
- Git
- GitHub

## Catatan
Program ini dibuat untuk memenuhi Tugas 5 pada materi Pertemuan 12 mata kuliah Algoritma dan Pemrograman. Data yang digunakan merupakan data contoh untuk keperluan pembelajaran.
