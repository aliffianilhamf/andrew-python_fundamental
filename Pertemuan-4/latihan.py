soal_1 =  " JaKaRtA  "
print(f"'{soal_1.strip().lower()}'")
soal_2 = "Rp 15.000.000"
print(f"'{soal_2.replace("Rp ", "").replace(".", "")}'")
soal_3 = "IPHONE13-RED-256GB"
print(f"'{soal_3.split("-")}'")
soal_4 = ['belajar', 'python', 'untuk', 'pemula']
print(f"'{"-".join(soal_4)}'")
soal_5 = " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  " 
print(f"'{soal_5.strip().lower().replace(" ", "_").replace("(", "").replace(")", "").split("|")}'")