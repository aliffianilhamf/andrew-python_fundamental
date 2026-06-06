nilai = 80

# grade A : 85-100
# grade B : 79 - 84
# grade C : 60-78
# grade D : 50 - 59
# grade E : 1 - 49 
#  kalau 0 : Otomatis tidak lulus 
print("Program Mulai")
if (nilai >=  85 ):
    print("Grade A")
elif (nilai >= 79):
    print("Grade B")
elif (nilai >= 60):
    print("Grade C")
elif (nilai >= 50):
    print("Grade D")
elif (nilai >= 1):
    print("Grade E")
else:
    print("Maaf, kamu tidak lulus")

print("Program Selesai")


""" 
Latihan Soal 1. 
Buat program untuk menghitung berapa total pembayaran belanja, dimana ketika 
- cust membeli dengan harga lebih dari 5000 akan mendapat diskon 10%
- cust membeli dengan harga lebih dari 1000 akan mendapat diskon 5%
- cust membeli dengan harga lebih dari 20000 akan mendapat diskon 20%
- Tidak ada diskon jika jumlah kurang dari 1000
- Tampilkan harga yang harus dibayar setelah diskon

Latihan Soal 2.
- Buat program untuk mengecek apakah bilagngan itu 0, positif, atau negatif
- Jika nol print "NOL"
- Jika Positif print "POSITIF"
- Jika Negatif print "NEGATIF"

Latihan Soal 3. 
- Buat program untuk menghitung konversi Suhu dari celcius ke fahrenheit, celcius ke reamur, dan celcius ke kelvin
- buat inputan suhu celciusnya menggunakan method input()
- jangan lupa konversi ke float. karene input selalu bertipe string 
- print pilihan tujuan konversi, misal : 
    Pilih Tujuan Konversi
    1: Fahrenheit
    2: Reamur
    3: Kelvin
- buat inputan lagi untuk menampung pilihan dari user, mau di konversi ke apa
- buat logika pengkondisian dari user memilih konversi yang apa
- di masing masing kondisi, jika memilih 
    1. Fahrenheit, rumusnya (suhu_celcius * 9/5) + 32, lalu print "{suhu_celcius} sama dengan {suhu_fahrenheit}"
    2. Reamur, rumusnya suhu_celcius * 4/5, lalu print "{suhu_celcius} sama dengan {suhu_reamur}"
    3. Kelvin, rumusnya suhu_celcius + 273.15, lalu print "{suhu_celcius} sama dengan {suhu_kelvin}"
- Jika pilihan tidak valid, print "Pilihan tidak valid, silahkan pilih 1, 2, atau 3"
"""

total_belanja = 100000