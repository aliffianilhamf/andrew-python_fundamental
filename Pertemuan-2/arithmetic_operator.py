""" 
Arithmetic operator adalah operator matematika biasa meliputi perkalian, penjumlahan, pembagian dan pengurangan
"""
print("Penjumlahan")
# 1. penjumlahan
angka_1 = 10 
angka_2 = 100 
hasil_penjumlahan = angka_1 + angka_2
print(f"Hasil penjumlahan dari {angka_1} + {angka_2} adalah {hasil_penjumlahan}")

angka_3 = 50
# hasil_penjumlahan_singkat 
# hasil_penjumlahan_singkat = hasil_penjumlahan + angka_3
angka_3 += hasil_penjumlahan
print(f"Hasil penjumlahan singkat dari {hasil_penjumlahan} + 50 = {angka_3}")

angka_4 = 100 

# penjumlahan cepat dengan hasil angka 3, lalu bagaimana caranya dan berapa totalnya
angka_4 += angka_3
print(f"Hasil penjumlahan singkat dari {angka_3} + 100 = {angka_4}")


print("")
print("Pengurangan")
# 2. Pengurangan 
angka_1 = 10
angka_2 = 5
hasil = angka_1 - angka_2 
print(f"hasil pengurangan dari {angka_1} - {angka_2} adalah {hasil}")

angka_3 = 100
hasil -= angka_3
print(f"hasil pengurangan dari {5} - {angka_3} adalah {hasil} ")

print()
print("Perkalian")
# 3. Perkalian
angka_1 = 10
angka_2 = 5
hasil = angka_1 * angka_2 
print(f"hasil perkalian dari {angka_1} x {angka_2} adalah {hasil}")

angka_3 = 100
hasil *= angka_3
print(f"hasil perkalian dari {50} x {angka_3} adalah {hasil} ")

print()
print("Pembagian")
# 3. Pembagian
angka_1 = 10
angka_2 = 5
hasil = angka_1 / angka_2 
print(f"hasil pembagian dari {angka_1} / {angka_2} adalah {hasil}")

angka_3 = 2
hasil /= angka_3
print(f"hasil pembagian dari {2} / {angka_3} adalah {hasil} ")

print()
print("Modulo")
# 3. Modulo == sisa hasil bagi
angka_1 = 11
angka_2 = 2
hasil = angka_1 % angka_2 
print(f"hasil pembagian dari {angka_1} % {angka_2} adalah {hasil}")

angka_3 = 1
hasil %= angka_3
print(f"hasil pembagian dari {1} % {angka_3} adalah {hasil} ")

# (bagian / keseluruhan) * 100 
total_siswa = 36
siswa_100 = 6
persentase = (siswa_100/total_siswa) * 100
print(f"total siswa yang mendapat nilai seratur sebanyak {persentase:.2f}%")
