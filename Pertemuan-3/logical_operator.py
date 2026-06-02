# 1. AND
print("AND")
nilai_ipa = 92 
persentase_kehadiran = 95 

# syarat kenaikan kelas 
syarat_nilai = nilai_ipa > 92
syarat_persentase_kehadiran = persentase_kehadiran > 90

apakah_lulus = syarat_nilai and syarat_persentase_kehadiran
print(f"Nilai ipa > 85? {syarat_nilai}")
print(f"Persentase kehadiran > 90 ? {syarat_persentase_kehadiran}")
print(f"siswa dinyatakan lulus? {apakah_lulus}")

print()
print("OR")
# 2. OR
bawa_sim = False 
bawa_stnk = False 

# syarat lolos tilang : harus membawa salah satu (sim / stnk)
apakah_lolos = bawa_sim or bawa_stnk 
print(f"Apakah bawa SIM ? {bawa_sim}")
print(f"Apakah bawa STNK? {bawa_stnk}")
print(f"Apakah Kamu Lolos Tilang ? {apakah_lolos}")


print()
print("NOT")
# 2. NOT
bawa_sim = False 
bawa_stnk = False 

# syarat lolos tilang : harus membawa salah satu (sim / stnk)
apakah_lolos = not bawa_sim or not bawa_stnk 
print(f"Apakah bawa SIM ? {bawa_sim}")
print(f"Apakah bawa STNK? {not bawa_stnk}")
print(f"Apakah Kamu Kena Tilang ? {apakah_lolos}")