number_1 = 10
number_2 = 5

# 1. lebih dari 
hasil = number_1 > number_2 
print(hasil) # True

# 2. kurang dari 
hasil = number_1 < number_2
print(hasil) # False

# 3. lebih dari  sama dengan
number_3 = 10
hasil = number_1 > number_3 # False
hasil = number_1 >= number_3 # True
print(hasil)

# 4. kurang dari sama dengan
number_4 = 5
hasil = number_2 < number_4 # false 
hasil = number_2 <= number_4 # true
print(hasil)

# 5. kalau sama dengan bagaimana?
number_5 = 5
number_6 = 6
hasil = number_5 == number_6 #False
print(hasil)
number_6 = 5 
hasil = number_5 == number_6 #True 
print(hasil) 

# 6. tidak sama dengan ?
number_7 = 5
number_8 = 6
hasil = number_7 != number_8 #true
print(hasil)
number_8 = 5 
hasil = number_7 != number_8 #false
print(hasil) 