from sistem_kasir import Produk, Keranjang

p1 = Produk("Kopi Kenangan", 25000, 4)
p2 = Produk("Susu UHT", 18000, 5)
p3 = Produk("Keyboard Gaming", 250000, 6)

# del p3

keranjang_saya = Keranjang()
keranjang_saya.tambah_produk(p1,2)
keranjang_saya.tambah_produk(p2,5)
keranjang_saya.tambah_produk(p3,4)

keranjang_saya.cetak_struk()
keranjang_saya.bayar()