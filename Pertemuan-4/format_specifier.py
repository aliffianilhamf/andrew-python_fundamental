import math
nilai_pi = math.pi
harga_barang = 1250000
persentase_diskon = 0.20 #20% 

# Mengatur presisi (jumlah angka dibelakang koma)
print(f"Nilai PI (Asli) : {nilai_pi}")
print(f"Nilai PI (2 desimal) : {nilai_pi:.2f}")
print(f"Nilai PI (10 desimal) : {nilai_pi:.10f}")

# Menambah koma sebagai ribuan 
print(f"harga brang : Rp {harga_barang:,.2f}")

# Menampilkan persentase 
print(f"Diskon : {persentase_diskon:.0%}")

# Perataan dan lebar kolom 
nama = "Ilham"
print(f"Nama Siswa (Rata Kiri) : '{nama:<10}'")
print(f"Nama Siswa (Rata Kanan) : '{nama:>10}'")
print(f"Nama Siswa (Rata Kanan) : '{nama:^10}'")
