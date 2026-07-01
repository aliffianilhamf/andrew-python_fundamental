judul = "Kakekku Ternyata Ayahku"

for character in judul :
    print(character, end='')
    
print()
for char in judul : 
    if char.lower() in 'aiueo':
        print(char)
        

print("Looping untuk list")
numbers = [1, 2, 3, 512, 5, 6]
numbers_pangkat_dua = []
for number in numbers : 
    numbers_pangkat_dua.append(number**2)
    
print(numbers_pangkat_dua)


print("Looping untuk range")
# range(start, stop, step)
# range(start, stop)
# range(stop)

# 1 - 5
for i in range(1, 6):
    print(i) 
    
print()
# 4 - 20 
for i in range(4 , 21):
    print(i)
  
print()  
# 1 - 20, cuman ganjil saja 
for i in range(1, 21, 2):
    print(i)

print()
# 0 - 7 
for i in range(8):
    print(i)


""" 
Latihan Soal 1. 
- kalimat = "Dokumen ini berisi latihan-latihan sederhana menggunakan Python"
- print hanya huruf konsonan saja (selain aiueo) dan juga print berapa jumlah hurufnya

Latihan Soal 2. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- cari nilai maksimum dari list diatas, tanpa menggunakan fungsi max() dari python

Latihan Soal 3. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- Hitung total nilai dari yang ada di list

"""

print()
kalimat = "Dokumen ini berisi latihan-latihan sederhana menggunakan Python"
total_char = 0

for i in kalimat:
    if i not in 'aiueo':
        print(i, end='')
        total_char = total_char + 1
  
print()      
print(total_char)