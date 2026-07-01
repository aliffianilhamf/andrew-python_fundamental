angka = 1 

# while angka < 10 : 
#     print(f"Ini perulangan ke {angka + 1}")
#     angka = angka + 1

# while angka < 100 : 
#     if (angka % 2 == 0):
#         print(f"{angka} adalah bilangan genap!")
#     angka = angka + 1

angka = 100 

while angka > 0 : 
    if (angka % 2 == 1):
        print(f"{angka} adalah bilangan ganjil!")
    angka = angka - 1
    
# infinite loop bisa disebabkan
# 1. Lupa tidak melakukan increment atau decrement
# 2. kondisi selalu bernilai TRUE



"""  
Latihan Soal 1. - Simulasi pengisian daya baterai 
- Kamu sedang membuat program simulasi indikator pengisian baterai. 
- Saat program dimulai baterai dalam kondisi lemah, dan lakukan pengisian 
- Akan berheti secara otomatis jika baterai sudah 100 %

    - buat variable baterai 
    - poakai while selama baterai kurang dari 100
    - dalam loop, naikkan nilai baterai sebanyak 5, setiap perulangannya. 
    - cetak pesan setiap kali daya betambah : "Daya saat ini : {nilai_baterai}%
    - Di luar loop (setelah selesai), cetak pesan: "Baterai Penuh! Pengisian dihentikan."
    
Latihan Soal 2. - Validasi Password Sistem Login
-  Kamu diminta membuat fitur keamanan dasar untuk mesin ATM. 
- Mesin akan terus meminta pengguna memasukkan PIN/Password selama input yang dimasukkan salah. 
- Namun, demi keamanan, pengguna hanya diberikan kesempatan maksimal 3 kali.
    - Tentukan password yang benar di dalam variabel, misal: password_benar = "rahasia123".
    - Buat variabel percobaan = 0 dan maks_percobaan = 3.
    - Gunakan while loop dengan kondisi: selama percobaan kurang dari maks_percobaan.
    - Di dalam loop, minta input dari pengguna menggunakan perintah input() dan simpan ke variabel tebakan. Jangan lupa naikkan nilai percobaan sebanyak 1.
    - Lakukan pengecekan: Jika tebakan == password_benar, cetak "Akses Diterima!" lalu hentikan loop menggunakan perintah break.
    - Jika loop selesai karena kehabisan kesempatan (perulangan habis tanpa terkena break), cetak pesan "Akun Anda Terblokir!".
    
"""

baterai = int(input("Masukkan baterai anda : "))
is_seratus = False

while is_seratus == False : 
    baterai = baterai + 5 
    
    if (baterai >= 100):
        is_seratus = True
        baterai = 100 
        
    print(f"Daya saat ini yaitu : {baterai}")
    

print("Baterai Penuh! Pengisian dihentikan.")
        
    

