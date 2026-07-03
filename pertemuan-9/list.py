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

