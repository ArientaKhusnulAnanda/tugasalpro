count = 0
print('Starting')
while count <= 10:
    print(count, ' ', end='') # bagian dari while loop
    count += 1 # juga bagian dari while loop
print('\nDone')

for i in range(1, 11):
    print(i, ' ', end=" ")
print("\nSelesai")

for i in range(0, 10, 2):
    print(i + 1, ' ', end=" ")
print("\nFinish")

for _ in range(0, 10):
    print(_, ' ', end=" ")
print()

print("Hanya print code jika semua perulangan selesai")
number = int(input("Masukkan angka: "))

kosong_printed = False  

for i in range(0, 10):
    if i == number:
        break
    if not kosong_printed:
        print("kosong")
        kosong_printed = True

print("\nSelesai")

#CONTOH:
#Soal 1: Menghitung Bilangan Genap Buatlah program yang mencetak semua bilangan genap dari 1 sampai 20 menggunakan perulangan for.
Angka = 2
for i in range(1, 21):
    if Angka % 2 == 0:
        print(Angka, ' ', end=" ")
    Angka += 1

#Soal 2: Menjumlahkan Angka yang Dimasukkan, Tulis program yang meminta pengguna memasukkan angka hingga mereka memasukkan angka 0. 
#Program akan menjumlahkan semua angka yang dimasukkan, kecuali angka 0. Gunakan perulangan while.
Jumlah = 0
while True:
    angka = int(input("Masukkan angka: "))
    if angka == 0:
        break
    Jumlah += angka
print("jumlah totak adalah: ", Jumlah)

#Soal 3: Faktorial Menggunakan Loop Buat program untuk menghitung faktorial dari sebuah bilangan yang dimasukkan oleh pengguna. 
# Faktorial dari sebuah bilangan n adalah hasil perkalian dari n dengan semua bilangan positif di bawahnya (n! = n × (n-1) × ... × 1). Gunakan perulangan
number = int(input("Masukkan angka: "))
faktorial = 1
for i in range(1, number + 1):
    faktorial *= i
print(f"Faktorial dari {number} adalah {faktorial}")

#Soal
#Soal 4: Menampilkan Deret Fibonacci Buat program yang mencetak deret Fibonacci hingga bilangan ke-n yang diinginkan oleh pengguna. 
#Fibonacci dimulai dari 0 dan 1, dan setiap bilangan berikutnya adalah hasil penjumlahan dua bilangan sebelumnya. Gunakan perulangan for.
number1 = int(input("Masukkan angka: "))
a, b = 0, 1
for i in range(number1):
    print(a, end=" ")
    a, b = b, a + b

#Soal 5: Membalikkan String Tulis program yang meminta pengguna memasukkan sebuah string, 
#lalu mencetak string tersebut secara terbalik menggunakan perulangan while.
text = input("Masukkan sebuah string: ")
reversed_text = ""
index = len(text) - 1
while index >= 0:
    reversed_text += text[index]
    index -= 1
print("String terbalik:", reversed_text)

import random
Min = 1
Max = 6
roll_again = 'y'
while roll_again == 'y':
    print('Rolling the dices...')
    print('The values are....')
    dice1 = random.randint(Min, Max)
    print(dice1)
    dice2 = random.randint(Min, Max)
    print(dice2)
    roll_again = input('Roll the dices again? (y / n): ')