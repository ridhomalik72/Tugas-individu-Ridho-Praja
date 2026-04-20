from pmu import Siswa, Universitas

siswa1 = Siswa("Ido", "12 RPL 2", [80, 82, 78, 85, 87, 90], True)
siswa2 = Siswa("doi", "12 RPL 1", [70, 75, 72, 74, 76, 78], False)

univ1 = Universitas("Universitas UPI", 90)
univ2 = Universitas("Universitas ITB", 92)
univ3 = Universitas("Universitas POLBAN", 85)

daftar_univ = [univ1, univ2, univ3]


for siswa in [siswa1, siswa2]:
    rata = siswa.hitung_rata_rata

    print("\n=== DATA SISWA ===")
    print("Nama  :", siswa.nama)
    print("Kelas :", siswa.kelas)
    print("Rata-rata :", round(rata, 2))

    print("Hasil Seleksi:")
    for u in daftar_univ:
        print(f"{u.nama} : {u.cek(rata)}")
