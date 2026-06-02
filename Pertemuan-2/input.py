""" 
Input pada python digunakan untuk menampung segala inputan yang dimasukkan oleh user.
jadi nilainya dimanis sesuai dengan apa yang diinginkan oleh user
"""

# nama_lengkap = input("Masukkan Nama Lengkap Anda : ")
# print(nama_lengkap)
# print(type(nama_lengkap))

# nama_depan = input("Masukkan Nama Depan : ")
# nama_belakang = input("Masukkan Nama Belakang : ")
# nama_lengkap = nama_depan + nama_belakang
# print(nama_lengkap)

angka_1 = int(input("Masukkan angka pertama : ")) #5 ->konversi tipe data jika ingin menjumlahkan dua buah angka
angka_2 = int(input("Masukkan angka kedua : ")) #10

# angka_1_int = int(angka_1)
# angka_2_int = int(angka_2)

hasil = angka_1 + angka_2
print(f"Hasil penjumlahan {angka_1} + {angka_2} adalah {hasil}")

""" 
Latihan soal 1. - Menampilkan hasil inputan
- Buat variabel untuk menampung inputam nama lengkap 
- Buat variabel untuk menampung inputan Hobi
- Buat variabel untuk menampung inputan umur 
- Buat variabel untuk menampung inputan alamat
- Tampilkan hasilnya dengan format : 
    Nama Saya : {isi dari varibel nama lengkap}, hobi saya : {isi dari variabel hobi}, umur saya : {isi dari variabel umur}, Alamat saya : {isi dari variabel alamat}
    
Latihan soal 2. - sistem kasir sederhana
- Buat variable untuk menampung inputan nama barang
- Buat variable untuk menampung inputan harga barang
- Buat variable untuk menampung inputan qty (jumlah yang di beli) yang dibeli
- Hitung total pembelian dengan rumus : harga * qty 
- Tampilkan hasilnya dengan format : 
    {Nama barang} dengan harga {harga barang} dibeli sebanyak {qty} yang totalnya {total pembelian}
    
Latihan soal 3. - luas dan keliling persegi panjang
- Buat variable untuk menampung inputan panjang
- Buat variable untuk menampung inputan lebar
- rumus Luas persegi panjang : p x l 
- rumus Keliling persegi panjang : 2 (p+l)
- Tampilkan hasilnya denhan format : 
    Persegi panjang dengan panjang sisi {panjang}, dan lebarnya {lebar}, memiliki Luas {luas}, dan keliling {keliling}
"""