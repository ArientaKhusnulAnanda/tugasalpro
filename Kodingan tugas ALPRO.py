#Nomor 1
print("\nnomor 1")
def input_anggaran(nama_koki):
    while True:
        try:
            biaya = int(input(f"Masukkan biaya harian untuk {nama_koki}: "))
            if biaya > 2000000:
                print(f"Warning! {nama_koki} melampaui batas anggaran harian Rp2.000.000.")
            else:
                return biaya
        except ValueError:
            print("Input tidak valid. Pastikan untuk memasukkan jumlah uang dalam angka.")

def kelola_anggaran_harian():
    total_makanan = 0
    catatan_anggaran = {"Andi": 0, "Budi": 0, "Cici": 0}
    jumlah_hari = 0

    while total_makanan < 1000:
        jumlah_hari += 1
        print(f"\n=== Hari ke-{jumlah_hari} ===")

        if jumlah_hari % 3 == 0:
            print("Hari ini, koki diizinkan menambah bahan makanan.")
            for koki in catatan_anggaran.keys():
                biaya_harian = input_anggaran(koki)
                porsi = biaya_harian // 5000
                catatan_anggaran[koki] += biaya_harian
                total_makanan += porsi
                print(f"{koki} menambahkan {porsi} porsi.")
        else:
            print("Hari ini, koki tidak diizinkan menambah bahan makanan.")

        print(f"Total porsi makanan hingga hari ini: {total_makanan}")

    print("\n=== Laporan Akhir ===")
    for koki, total_biaya in catatan_anggaran.items():
        print(f"Total biaya untuk {koki}: Rp{total_biaya}")
    print(f"Total porsi makanan yang disiapkan: {total_makanan}")

kelola_anggaran_harian()


#Nomor 2
def fibonacci(n):
    global count_recursive_calls
    count_recursive_calls += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def total_production(n):
    global count_recursive_calls
    count_recursive_calls = 0 
    total = 0  

    print("\nnomor 2")
    print("=== Laporan Produksi Bulanan ===")
    for month in range(1, n + 1):
        production = fibonacci(month)
        
        if is_prime(month):
            production += 5
            print(f"Bulan {month}: {production} (termasuk bonus 5 unit)")
        else:
            print(f"Bulan {month}: {production}")

        total += production

    print("\n=== Laporan Akhir ===")
    print(f"Total produksi hingga bulan ke-{n}: {total}")
    print(f"Jumlah iterasi rekursif yang dilakukan: {count_recursive_calls}")

total_production(7)
