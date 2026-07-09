# List adalah struktur data di python yang bisa menambung lebih dari 1 data
# isinya bisa berbeda - beda tipe data
# sifatnya mutable (bisa diubah - ubah)
# list memiliki indeks yang selalu dimulai dari 0 untuk mengakses items

my_list = [1, "ADI", True, 3.14]
# indeks   0,   1  ,  2  ,   3
#         -4,  -3  ,  -2 ,  -1   Negatif indeks

# Cara mengakses list
# 1. indeks
print(my_list)
print(my_list[1])
print(my_list[3])
print(my_list[-1])

# 2. slicing

nama = ["Adi", "Retno", "Budi", "Feri"]
# misal mau mengakses retno dan budi
# [start:stop]
print(nama[1:3])
print(nama[1:4])
# [start:stop:step]
print(nama[0:3:2])
# 
print(nama[1:])
print(nama[:3])

list_2d = [
            [1,2,3], 
            [4,5,6]
          ]

list_3d = [
            [
                [1,2,3], 
                [4,5,6]
            ], 
            [
                [7,8,9], 
                [10,11,12]
            ]
        ]

print(list_3d[1][1][1])

""" 
Latihan List
my_list_3 = ["Ratna", 0, 100, 32, False, [99,88], True]

1. Tampilkan item ke 3
2. Dapatkan nilai false dengan negatif indexing 
3. Dapatkan nilai [99,88]
4. Dapatkan nilai [100, 32, False, [99, 88]]
5. Dapatkan Nilai ["Ratna", 100, False, True]
"""

# 
print("\nMengubah value list")
hari = ['Senin', 'Selasa', 'Rabu']
print(f"List sebelum diubah : {hari}")

hari[-1] = 'Wednesday'
hari[:2] = ['Monday', 'tuesday']

print(f"List sesudah diubah : {hari}")


print("\nMenambah Item pada list")
numbers = [1, 2, 3, 4, 5]
print(f"List number sebelum di tambah : {numbers}")

# menggunakan apend 
numbers.append(6)

# mengunakan insert 
numbers.insert(1, 1.5) 


print(f"list number setelah di tambah : {numbers}")

# extend 
number_1 = [1,2,3]
number_2 = [4,5,6]
number_1.extend(number_2)


print(number_1)


""" 
months = ["Januari", "April", "September", "Desember"]
- Lengkapi list months dengan menambahkan bulan yang kosong menggunakan bahasa inggris (cth, February, March, May, dst)
- Ubah Januari, Aparil, September, Desember ke bahasa inggris juga

"""

print("\nMenghapus item pada list")
my_list_4 = ["Ani", 33, 44, 55]
print(f"My list 4 : {my_list_4}")
# 1. pop()
# Dia akan menghapus item terakhir, kalau tidak ada indeksnya, kalau ada indeksnya, dia akan menghapus sesuai indeks
hasil_pop = my_list_4.pop() # tdk ada indeks, berarti item terakhir yang akan di hapus
print(f"My list 4 setelah di pop() : {my_list_4} item yang di hapus : {hasil_pop}")
hasil_pop_2 = my_list_4.pop(1) # ada indeks, berarti item sesuai indeks yang akan di hapus
print(f"My list 4 setelah di pop(1) : {my_list_4} item yang di hapus : {hasil_pop_2}")

# 2. remove() 
# Menghapus item mana yang dipilih dalam parameter remove 
my_list_5 = [100, 200, 300, 400, 500]

print(f"\nMy list 5 : {my_list_5}")

hasil_remove = my_list_5.remove(300)
print(f"My list 5 setelah di remove(300) : {my_list_5} item yang di hapus : {hasil_remove}")


# 
print("\nLooping pada list")
my_list_6 = my_list_5.copy() 

print(f"my list 6 : {my_list_6}")
for i in my_list_6:
    print(f"Isi dari list : {i}")

print()
for i in range(len(my_list_6)):
    print(f"Isi dari list : {my_list_6[i]}")
    
    
print()
for indeks, value in enumerate(my_list_6):
    print(f"Perulangan ke {indeks} valuenya : {value}")
    
    
print() 
awal = 0 
akhir = len(my_list_6)

while (awal < akhir) : 
    print(f"Isi dari list : {my_list_6[awal]}")
    
    awal = awal + 1
    
""" 
mahasiswa = ["Andi", "Joko", "Pardi", "Aziz"]
1. Looping  (for & while) dapatkan indeks dan valuenya

nilai = [60, 70, 75, 99, 90, 89, 99, 87]
2. buat list kosong bernama nilai_lulus 
3. gunakan looping untuk memeriksa setiap nilai, jika lebih besar atau sama dengan 80, masukkan nilai ke dalam nilai_lulus
4. tampilkan nilai lulus dengan looping

kontak_kotor = ["Andi", "Budi", "Andi", "Siti", "Budi", "Dewi", "Siti"]
5. buat list kosong bernama kontak_bersih
6. gunakan looping untuk mengiterasi daftar kontak_kotor, cek apakah nama belum ada di kontak bersih, jika belum, masukkan ke kontak bersih,kalau sudah, tidak perlu di masukkan 
7. cetak kontak bersih dengan looping
"""


print("\nList COmprehension")
numbers = [1, 2, 3, 4]
pangkat_numbers = [i ** 2 for i in numbers] 
# for i in numbers : 
#     pangkat_numbers.append(i ** 2)
    
print(pangkat_numbers)

numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8,9, 10]
numbers_2_ganjil = [i for i in numbers_2 if i % 2 == 1]
print(numbers_2_ganjil)

""""
celcius = [0, 10, 20, 30, 40]
buat menggunakan list comprehension, untuk konversi ke fahrenheit - (suhu_celcius * 9/5) + 32
"""