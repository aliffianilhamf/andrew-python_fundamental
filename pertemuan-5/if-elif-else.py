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
"""

total_belanja = 100000