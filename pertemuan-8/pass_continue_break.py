# pass
for i in range(10):
    pass 

# continue 
for i in range(10):
    if i % 2 == 1 :
        pass 
        # continue
    print(i)
    
print()
# break
for i in range(10):
    if i == 5 : 
        break
    print(i)
    
    
jumlah_tebakan = 0 
angka_rahasia = 20
while True : 
    tebakan_user = int(input("Masukkan tebakanmu : "))
    jumlah_tebakan += 1 
    
    if tebakan_user > angka_rahasia : 
        print("Tebakanmu terlalu tinggi")
    elif tebakan_user < angka_rahasia :
        print("Tebakanmu terlalu rendah")
    else :
        print(f"tebakanmu benar. kamu menebak sebanyak {jumlah_tebakan}")
        break
    
    