""" 
Konversi tipe data - mengubah tipe data suatu variable ke bentuk yang lain
"""

print("Konversi dari String ke Int/Float")
# Konversi dari string ke int / float 
angka_str = "10"
print(type(angka_str))

angka_int = int(angka_str) # konversi ke int
print(f"{angka_str} sekarang tipe datanya {type(angka_int)}")

angka_float = float(angka_str) # konversi ke float
print(f"{angka_str} sekarang tipe datanya {type(angka_float)} dan value nya menjadi {angka_float}")

print()
print("Konversi dari Int/Float ke String")
# Konversi dari Int / Float ke string 
number_int = 100
print(type(number_int))

number_str = str(number_int) # konversi ke string
print(f"{number_int} sekarang tipe datanya {type(number_str)}")

number_float = 100.5
print(type(number_float))

number_str = str(number_float) # konversi ke string
print(f"{number_float} sekarang tipe datanya {type(number_str)}")

