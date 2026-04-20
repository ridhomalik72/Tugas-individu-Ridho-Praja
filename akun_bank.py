class AkunBank:
  def __init__(self, nomor, pemilik, saldo_awal):
    self.nomor = nomor 
    self.pemilik = pemilik
    self.saldo = saldo_awal
    self.riwayat = []
  
  def cek_saldo(self):
    print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
  def tarik_tunai(self, jumlah):
    if jumlah <= self.saldo and jumlah > 0:
      self.saldo -= jumlah
      pesan = (f"{self.pemilik} menarik Rp{jumlah}")
      self.riwayat.append(pesan)
      print(pesan)
    else:
      print("Saldo tidak cukup!")
  
  def transfer(self, tujuan, jumlah):
    if self.saldo >= jumlah and jumlah > 0:
      self.saldo -= jumlah
      tujuan.saldo += jumlah
      self.saldo -= 2500
      pesan = (f"Transfer Rp{jumlah} ke {tujuan.pemilik} Berhasil!")
      self.riwayat.append(pesan)
      print(pesan)
    else:
      print("Transfer Gagal: Saldo tidak cukup.")
    
  def tampilkan_riwayat(self):
    print(f"Riwayat Transaksi {self.pemilik}")
    for r in self.riwayat:
      print("-", r)