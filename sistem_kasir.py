class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok


class Keranjang:
    def __init__(self):
        self.daftar_barang = []

    def tambah_produk(self, produk_baru, jumlah):
        if produk_baru.stok >= jumlah:
            barang = {
                "produk": produk_baru,
                "jumlah": jumlah
            }
            self.daftar_barang.append(barang)
            print(f"{produk_baru.nama} berhasil ditambahkan sebanyak {jumlah}")
        else:
            print("Stok kurang, produk gagal ditambahkan")

    def hitung_total(self):
        total = 0
        for barang in self.daftar_barang:
            total_harga = barang["produk"].harga * barang["jumlah"]
            total += total_harga
        return total
    
    def hitung_total_setelah_diskon(self):
        total = self.hitung_total()
        if total > 100000:
            total -= total * 0.1  
        return total
    
    def cetak_struk(self):
        print("\n=== Struk Belanja ===")
        for barang in self.daftar_barang:
            produk = barang["produk"]
            jumlah = barang["jumlah"]
            subtotal = produk.harga * jumlah
            print(f"{produk.nama} x{jumlah} : Rp{subtotal}")

        total_akhir = self.hitung_total()

        # Diskon 10% jika total lebih dari 100000
        if total_akhir > 100000:
            diskon = total_akhir * 0.1
            print(f"\nDiskon (10%) : -Rp{diskon}")
            total_akhir -= diskon

        print(f"Total Akhir : Rp{total_akhir}")

    def bayar(self):
        total_akhir = self.hitung_total_setelah_diskon()
        print(f"\nTotal yang harus dibayar: Rp{int(total_akhir)}")

        while True:
            try:
                uang_diterima = int(input("Masukkan uang yang diterima: Rp"))
                if uang_diterima < total_akhir:
                    print("Uang tidak cukup! Silakan masukkan jumlah yang mencukupi.")
                else:
                    kembalian = uang_diterima - total_akhir
                    print(f"Uang diterima : Rp{uang_diterima}")
                    print(f"Kembalian     : Rp{int(kembalian)}")
                    print("Terima kasih telah berbelanja!")
                    break
            except ValueError:
                print("Input tidak valid! Masukkan angka yang benar.")
