"""
Math Function - digunakan untuk membantu memudahkan operasi matematika
"""

a = 10
b = 3.5
c = -5

# 1. Round / pembulatan >= .5 dibulatkan ke atas, kurang dari .5 dibulatkan kebawah
result = round(b)
print(f"hasil dari round {b} adalah {result}")

# 2. absolute -> mengubah nilai menjadi positif 
result = abs(c) 
print(f"Hasil absolute dari {c} adalah {result}")

# 3. max 
result = max(9, 5, 4, 12)
print(f"Nilai maksimalnya adalah {result}")

# 3. min
result = min(9, 5, 4, 12)
print(f"Nilai minimalnya adalah {result}")

import math

PHI = math.pi

print(f"Nilai phi adalah {PHI}") 

# pembulatan kebawah
result = math.floor(3.99)
print(f"Hasil pembulatan kebawah dari 3.99 adalah {result}")

# pembulatan ke atas
result = math.ceil(3.1)
print(f"Hasil pembulatan keatas dari 3.1 adalah {result:.2f}")

# akar kuadrat dari sebuah angka
result = math.sqrt(9)
print(f"Akar kuadrat dari 9 adalah {result}")

# Pangkat
result = math.pow(3, 2) # kiri itu angka yang ingin di pangkatkan, kanan itu pangkatnya
print(f"Hasil dari 3 pangkat 2 adalah {result}")


""" 
Latihan Soal 
1. Buat program untuk menghitung Luas dan Keliling Lingkaran
2. Bebas, mau menggunakan input atau variable static
3. Tapi harus mengimplementasikan math function
4. Rumus : Luas = phi * r^2, Keliling = 2 * phi * r
"""

def pembulatan_keatas(x):
    result = int(x)
    result += 1
    
    return result

def pembulatan_kebawah(x):
    result = int(x)
    
    return result


result = pembulatan_keatas(3.1)
print(f"Hasil pembulatan keatas dengan fungsi yang kita buat dari 3.1 adalah {result}")
result = pembulatan_kebawah(3.99)
print(f"Hasil pembulatan kebawah dengan fungsi yang kita buat dari 3.99 adalah {result}")
# luas = pi * pow(jari_jari, 2)

# 3**3
# 3**4
# 3**5 

# hasil = 0
# total_akhir = 0

# for i in range(0, 6, 2):
#    if(i == 3):
#        hasil = math.pow(3, i)
#        print(f"{i} pangkat {i} adalah {hasil}")
#    else :
#        hasil = hasil + total_akhir
#        total_akhir = math.pow(hasil , i)
#        print(f"{hasil} pangkat {i} adalah {total_akhir}")
    
# print(f"Hasil akhirnya adalah : {total_akhir}")