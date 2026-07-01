# Variabel - tempat untuk menampung data. 
print("Nama : Ilham")
print("Nama : Ilham")
print("Nama : Ilham")
print("Nama : Aliffian")
print("Nama : Aliffian")
print("Nama : Aliffian")
print("Nama : Aliffian")
print("Nama : Aliffian")
print("Nama : Aliffian")
print("Nama : Aliffian")

print("")
nama_saya = "Septi"
print(nama_saya)
print(nama_saya)
print(nama_saya)
print(nama_saya)
print(nama_saya)
print(nama_saya)
print(nama_saya)
print(nama_saya)
print(nama_saya)
print(nama_saya)


print("")

# Variabel penampung untuk biodata mahasiswa
nama_mahasiswa = "Aliffian Ilham Febriyana"
umur = 23
tinggi_badan = 165.7 
apakah_sudah_lulus = False

print(nama_mahasiswa)
print(umur)
print(tinggi_badan)
print(apakah_sudah_lulus) 

# Kode untuk mencari tipe data suatu variable
print(type(nama_mahasiswa))
print(type(umur))
print(type(tinggi_badan))
print(type(apakah_sudah_lulus))

# melakukan print satu line 
print(nama_mahasiswa, umur, tinggi_badan, apakah_sudah_lulus)
# print(nama_mahasiswa + umur + tinggi_badan + apakah_sudah_lulus)

# Fstring
print(f"{nama_mahasiswa} {umur} {tinggi_badan} {apakah_sudah_lulus}")


# output : Nama Saya : Aliffian Ilham Febriyana, Umur : 23, Tinggi Badan : 165.7, Apakah Sudah Lulus Kuliah ? : False
print("Nama Saya :", nama_mahasiswa, ", Umur : ", umur, ", Tinggi Badan : ", tinggi_badan, ", Apakah Sudah Lulus Kuliah? : ", apakah_sudah_lulus)
print(f"Nama Saya : {nama_mahasiswa}, Umur : {umur}, Tinggi Badan : {tinggi_badan}, Apakah Sudah Lulus Kuliah ? : {apakah_sudah_lulus}")

# Best practice menulis variabel
# 1. menggunakan lowercase 
# 2. jika terdiri dari 2 kata atau lebih, pisahkan dengan underscore
# 3. jangan diawali dengan angka / karakter lain

# Latihan : 
# 1. Buat variable yang menampung 1 hari favoritmu (cth: fav_day = senin)
fav_day_why = "Senin karena semangat saya masih tinggi"
hated_day_why = "minggu, karena besoknya senin"
fav_day = "Senin"
hated_day = "Minggu"
# 2. Buat variable yang menampung 1 hari yang tidak kamu sukai 
# 3. print dan jelaskan kenapa kamu suka hari itu dan tidak suka hari itu, cth : 
# "Saya suka hari Senin karena semangat saya masih tinggi, dan saya tidak suka hariB minggu, karena besoknya senin"
print(f"Saya suka hari {fav_day_why}, dan saya tidak suka hari {hated_day_why}")
print(f"Saya suka hari {fav_day} karena semangat saya masih tinggi, dan saya tidak suka hari {hated_day}, karena besoknya {fav_day}")

# 4. print penjelasan kegiatan di hari favoritmu
print(f"kegiatanku di hari : {fav_day} adalah Sarapan, belajar, bermain ")