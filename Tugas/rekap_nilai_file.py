
from pathlib import Path


# Menentukan lokasi folder dan file
FOLDER_DATA = Path("data")
FILE_INPUT = FOLDER_DATA / "nilai.txt"
FILE_OUTPUT = FOLDER_DATA / "hasil_rekap.txt"


# Data contoh yang akan digunakan jika file input belum ada
DATA_CONTOH = """A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
"""


def siapkan_data():
    """Membuat folder dan file input jika belum tersedia."""
    FOLDER_DATA.mkdir(parents=True, exist_ok=True)

    if not FILE_INPUT.exists():
        with open(FILE_INPUT, "w", encoding="utf-8") as file:
            file.write(DATA_CONTOH)


def baca_data(nama_file):
    """Membaca dan memvalidasi data nilai dari file."""
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Melewati baris kosong
                if not baris:
                    continue

                try:
                    # Memisahkan NIM dan nilai
                    bagian = baris.split(",")

                    if len(bagian) != 2:
                        raise ValueError

                    nim = bagian[0].strip()
                    nilai = float(bagian[1].strip())

                    if not nim:
                        raise ValueError

                    # Menyimpan data yang valid
                    data.append((nim, nilai))

                except ValueError:
                    print(
                        f"Baris {nomor} dilewati: "
                        f"data tidak valid ({baris})"
                    )

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    """Menghitung statistik dan menyimpan hasil rekap."""
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return False

    # Mengambil seluruh nilai yang valid
    daftar_nilai = [item[1] for item in data]

    jumlah_data = len(daftar_nilai)
    rata_rata = sum(daftar_nilai) / jumlah_data
    nilai_minimum = min(daftar_nilai)
    nilai_maksimum = max(daftar_nilai)

    # Nilai minimal 60 dinyatakan lulus
    jumlah_lulus = sum(
        1 for nilai in daftar_nilai if nilai >= 60
    )

    # Menulis hasil rekap ke file output
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("===== REKAP NILAI MAHASISWA =====\n")
        file.write(f"Jumlah data valid : {jumlah_data}\n")
        file.write(f"Rata-rata nilai   : {rata_rata:.2f}\n")
        file.write(f"Nilai minimum     : {nilai_minimum:.2f}\n")
        file.write(f"Nilai maksimum    : {nilai_maksimum:.2f}\n")
        file.write(f"Jumlah mahasiswa lulus: {jumlah_lulus}\n")
        file.write("\nDaftar Nilai Valid:\n")

        for nim, nilai in data:
            status = "Lulus" if nilai >= 60 else "Tidak Lulus"
            file.write(f"{nim}, {nilai:g}, {status}\n")

    # Menampilkan ringkasan ke terminal
    print("\n===== REKAP NILAI MAHASISWA =====")
    print(f"Jumlah data valid : {jumlah_data}")
    print(f"Rata-rata nilai   : {rata_rata:.2f}")
    print(f"Nilai minimum     : {nilai_minimum:.2f}")
    print(f"Nilai maksimum    : {nilai_maksimum:.2f}")
    print(f"Jumlah mahasiswa lulus: {jumlah_lulus}")
    print(f"\nHasil rekap tersimpan di: {nama_file}")

    return True


def main():
    """Menjalankan seluruh proses rekap nilai."""
    siapkan_data()

    print("PROGRAM REKAP NILAI MAHASISWA")
    print(f"File input: {FILE_INPUT}")

    data = baca_data(FILE_INPUT)

    if data:
        tulis_rekap(FILE_OUTPUT, data)


if __name__ == "__main__":
    main()
