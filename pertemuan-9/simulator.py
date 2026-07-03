import time

def simulator_loop(jenis_loop):
    print(f"--- Memulai Simulasi {jenis_loop.upper()} ---")
    
    if jenis_loop == "for":
        # Contoh: Perulangan for dengan range
        angk = int(input("Mau berulang berapa kali: "))
        for i in range(1, angk+1):
            print(f"Iterasi ke-{i}: Variabel i bernilai {i}")
            time.sleep(1) 
            
    elif jenis_loop == "while":
        # Contoh: Perulangan while dengan kondisi
        angk = int(input("Mau berulang berapa kali: "))
        x = 1
        while x <= angk:
            print(f"Pengecekan: Apakah {x} <= {angk}? Ya.")
            print(f"Aksi: Eksekusi kode, sekarang x menjadi {x}")
            x += 1
            time.sleep(1)
            
    print("--- Simulasi Selesai ---")


pilihan = input("Pilih simulasi (for/while): ").lower()
simulator_loop(pilihan)