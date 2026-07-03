# Latihan soal 1. 
for angka in range(1, 21):
    print(angka)
    
    
print()
awal = 1
akhir = 20 

while (awal <= akhir):
    print(awal)
    
    awal = awal + 1

# while True : 
#     print(awal)
    
#     awal += 1 
    
#     if (awal == akhir+1):
#         break

# Latihan soal 3

angka_faktorial = int(input("Masukkan Angka : "))
hasil = 1

for i in range(angka_faktorial, 0, -1):
    hasil = hasil * i 
    
print(f"Faktorial = {hasil}")

