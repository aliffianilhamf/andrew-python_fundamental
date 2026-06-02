# Memanipulasi huruf
print("Memanipulasi Huruf")

text = "belaJaR pyThOn Dari daSaR"

print(f"Original    : {text}")
print(f"Upper       : {text.upper()}")
print(f"Lower       : {text.lower()}")
print(f"Capitalize  : {text.capitalize()}")
print(f"Title       : {text.title()}")
print(f"Swapcase    : {text.swapcase()}")

print()
# Pembersihan Spasi 
print("Pembersihan spasi")
data_kotor = "  Senangnya Aku   "
print(f"Original teks : '{data_kotor}'")
print(f"Strip : '{data_kotor.strip()}'")
print(f"Left Strip : '{data_kotor.lstrip()}'")
print(f"Right Strip : '{data_kotor.rstrip()}'")

print()
# Pemisahan / splitting
print("Splitting")
judul = "Tanaman Pemakan Segalanya"
kata_kata = judul.split(" ")
print(f"Original teks '{judul}', hasil split : {kata_kata}")

kode_barang = "001-ASSD-234"
hasil_split = kode_barang.split("-")
print(f"Original teks '{kode_barang}', hasil split : {hasil_split}")

print()
# Replace
print("Replace")
data_1 = "hari ini cuacanya hujan"
data_2 = data_1.replace("hujan", "cerah")
print(f"Original data : '{data_1}'")
print(f"Setelah di replcae : '{data_2}'")


print()
# Tipe konten
print("Tipe Konten")
string_1 = "Python3"
string_2 = "1345"

print(f"Apakah alpanumerik? {string_1.isalnum()}") # campuran huruf dan angka
print(f"Aapakah alpa? {string_2.isalpha()}") # huruf saja
print(f"Apakah angka saja ? {string_2.isdigit()}") # angka saja


""" 
Latihan Soal 1. 
Bersihkan spasi diawal /akhir dan ubah menjadi huruf kecil semua 
- input : " JaKaRtA  "
- target : "jakarta"

Latihan Soal 2. 
Hapus "Rp" (termasuk spasi setelah Rp) dan hapus tanda titik "."
- input : "Rp 15.000.000"
- Target : "15000000"

Latihan Soal 3.
Pecah String berdasarkan karakter strip (-)
- input : "IPHONE13-RED-256GB 
- Target : ['IPHONE13', 'RED', '256GB']

Latihan Soal 4. 
gabungkan list menggunakan separator tanda hubung (-)
- input : ['belajar', 'python', 'untuk', 'pemula']
- target : "belajar-python-untuk-pemula"

Latihan Soal 5. 
Pisahkan string berdasarkan |, bersihkan spasi diawal dan akhir setiap item, ubah jadi huruf kecil, ubah spase di tengah menjadi udnerscore (_), hapus tanda kurung
- input : " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  "
- target : ['nama_customer_', '_total_belanja_idr_', '_alamat_pengiriman']
"""
