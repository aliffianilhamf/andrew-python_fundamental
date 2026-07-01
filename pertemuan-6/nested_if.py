# kita ingin mencari bilangan genap positf
bilangan = 0 

if (bilangan % 2 == 0):
    if (bilangan > 0):
        print("Bilangan Genap Positif")
    else : 
        if (bilangan == 0):
            print("Bilangan adalah NOL")
        else : 
            print("Bilangan genap Negatif")
            
else :
    print("Bilangan Ganjil")
    
    
total_belanja = float(input("Masukkan Total Belanja : "))
print(f'Total belanja anda : {total_belanja}')
if (total_belanja > 20000):
    diskon = 20/100 * total_belanja
    print(f"Selamat kamu mendapatkan diskon sebesar {diskon}")
else : 
    if ( total_belanja > 5000):
        diskon = 10/100 * total_belanja
        print(f"Selamat kamu mendapatkan diskon sebesar {diskon}")
    elif (total_belanja > 1000): 
        diskon = 5/100 * total_belanja
        print(f"Selamat kamu mendapatkan diskon sebesar {diskon}")
    else : 
        diskon = 0
        print(f"Selamat kamu mendapatkan diskon sebesar {diskon}")
            
print(f"Total yang harus di bayar {total_belanja - diskon}")

"""  
Latihan 1. 
- Membuat progran kalkulator sederhana 
- memiliki 3 inputan
    1. Angka pertama, buat variable untuk menampung inputan angka pertama
    2. Operator, buat juga variable untuk menampung inputan operator (+, -, x, /)
    3. Angka kedua, buat variable untuk menampung inputan angka kedua
- cek user memasukkan operator apa?
    - jika penjumlahan (+) maka print "{angka_1} + {angka_2} = {hasil}
    - jika penjumlahan (-) maka print "{angka_1} - {angka_2} = {hasil}
    - jika penjumlahan (x) maka print "{angka_1} x {angka_2} = {hasil}
    - jika penjumlahan (/) maka print "{angka_1} / {angka_2} = {hasil}
        - pembagi itu tidak boleh nol (angka_2), oleh karena itu, ada if untuk mengecek agar angka 2 tidak nol
        - jika angka_2 itu nol, maka cukup print saja "Angka kedua tidak boleh nol"
        - tapi kalau angka_2 tidak nol, maka lakukan operasi pembagian seperti biasa.
- Jika operator yang dipilih tidak valid, maka print "operator tida valid (+, -, x, /)"
"""

print()
angka_1 = float(input("Masukkan Angka pertama : "))
operator = input("Masukkan Operator (+, / , x, -) :  ")
angka_2 = float(input("Masukkan Angka Kedua : "))


if (operator == '+') : 
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
elif (operator == '-') : 
    hasil = angka_1 - angka_2
    print(f"{angka_1} - {angka_2} = {hasil}")
elif (operator == 'x') : 
    hasil = angka_1 * angka_2
    print(f"{angka_1} * {angka_2} = {hasil}")
elif (operator == '/') : 
    if (angka_2 != 0):
        hasil = angka_1 / angka_2
        print(f"{angka_1} / {angka_2} = {hasil}")
    else : 
        print("Angka Kedua tidak boleh nol")
else : 
    print("Operator tidak valid (+, - , x, /)")