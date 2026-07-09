# Membuat dictionary
my_dict1 = {
    "nama" : "Tobi",
    "umur" : 20,
    "alamat" : "Semarang"
}

my_dict2  = {
    10 : "Sepuluh",
    20 : "Dua puluh",
    30 : "Tiga Puluh"
}

my_dict3 = dict(name="Aliffian", age='23')

keys = ['name', 'age']
my_dict4 = dict.fromkeys(keys)


print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict4)

print("\nMengakses dictionary")
# mengakses dictionary 
print(my_dict1["alamat"])
print(my_dict2[10])
print(my_dict3["name"])
print(my_dict4["age"])

print("\nUpdate dictionary")
my_dict4["age"] = 30
my_dict4["name"] = "hendra"
print(f"Isi my_dict4 : {my_dict4}")

print("\nDelete dictionary")
del my_dict4["age"]
print(f"Isi my_dict4 setelah di delete : {my_dict4}")

my_dict4.clear()
print(f"Isi my_dict4 setelah di clear : {my_dict4}")


print("\nLooping dicionary")
buku = {
    "judul" : "Pelangi Dimatamu",
    "tahun" : 2020,
    "penerbit" : "Erlangga",
    "kategori" : ["kehidupan", "percintaan"], 
    "penulis" : {
        "nama" : "Jambrud",
        "alamat" : "Jakarta"
    }
}

# for item in buku: 
    
#     print(f"{item} : {buku[item]}")
    
for key, value in buku.items():
    print(f"{key} : {value}")
    
print()
print(buku.items())
print(buku.keys())
print(buku.values())

print()
print(buku["penulis"]["nama"])

for key, value in buku.items():
    
    if key == "penulis":
        print(f"{key} :")
        for kunci, nilai in buku[key].items() : 
            print(f"\t{kunci} : {nilai}")
    else : 
        print(f"{key} : {value}")
        
# Latihan Soal
""" 
Buatlah sebuah dictionary yang menyimpan informasi tentang sebuah buku, 
seperti judul, penulis, tahun terbit, dan genre. Kemudian, lakukan operasi berikut:
1. Tambahkan informasi tentang penerbit buku tersebut.
2. Perbarui tahun terbit buku tersebut.
3. Hapus informasi tentang genre buku tersebut.
4. Tampilkan semua informasi tentang buku tersebut dg for.
"""