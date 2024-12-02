#print or cout
a = 3
b = 2
total = a + b
print (total)
nama = "Fabio"
print ("nama saya adalah " + nama)

#class of variable or changing variable type: str(), int(), & float()
angka = 5
angka_berkoma = 3.85
aku = "Fadhil"
print (str(angka) + " & " + str(angka_berkoma))

#input & output
User = input("Masukkan nama anda: ")
print ("Hallo, Selamat Datang " + User + " di wisata gunung bromo!!")

#Aritmatika operator
print (5/2)         #harus memakai print, (/) = pembagian dengan hasil berkoma & (//) = pembagian dengan hasil bulat
print (11%3)        #modulus (habis dibagi/tidak)

A = 5
B = 4
print ("Hasil pemangkatan angka adalah: " + str(A**B))

TOTAL = A + B       #assignt methods
TOTAL += 5
print ("Hasil penjumlahan TOTAL adalah: " + str(TOTAL))

import math             #Modul Math
print (math.floor(5.3)) #Modul Math pembulatan ke bawah 
print (math.sqrt(64))   #Modul Math akar 
print (math.pow(2, 3))  #Modul Math pangkat 2^3
print (math.ceil(5.7))  #Modul Math pembulatan ke atas lawan dari floor

#BAB STRING

#STRING BASIC
print ("\"Selamat datang di rumah jawa\"")  #(\" "\) escape character / untuk print petik atau yang lain
text = "rumah fabio banyu cyto"

print (text.upper())            #untuk mengkapitalkan semua huruf pada text
print (text.lower())            #untuk mengkecilkan semua hruf pada text
print (len(text))               #untuk menghitung jumlah huruf dan space yang diketik
print (text.split(' '))         #untuk membagi sebuah string atau text berdasarkan dengan tanda
print (text.capitalize())       #mengubah huruf pertama menjadi huruf besar
print (text.index('y'))         #mencari index sebuah karakter, ex index: r pada rumah adalah urutan ke 0, u pada rumah adalah urutan ke 1 pada kalimat

#SLICING STRING 
#menghitung jumlah dan menentukan urutan huruf dalam suatu kalimat seperti len, namun dihitung terbalik (dari kanan & mulai dari -1 menuju seterusnya)

TEXT = "PYTHON"         # P =(0 & -6), Y =(1 & -5), T =(2 & -4), H =(3 & -3), O = (4 & -2), N = (5 & -1)

print (TEXT[0])         #mengeluarkan output dari angka 0 yaitu P
print (TEXT[-6])        #mengeluarkan output yang sama dari print diatas namun dengan cara menghitung posisi huruf yang berbeda (berkebalikan)
print (TEXT[2:])        #mengeluarkan output huruf pada posisi angka 2 = T, dan tanda ":" menandakan huruf yang setelahnya (huruf ke 2 dan setelahnya di output) atau hingga
print (TEXT[-5:-1])     #mengeluarkan output huruf pada posisi -5 hingga -1 (posisi -1 tidak ikut dihitung)
print (TEXT[3:5])       #mengeluarkan output huruf pada posisi 3 hingga 5 (posisi 5 tidak ikut dihitung)
print (TEXT[:4])        #mengeluarkan output huruf pada posisi huruf sebelum angka 4 "PYTH" (posisi 4 tidak ikut dihitung)

#STRING CONCATENATION
#penggabungan kalimat dengan beberapa komponen seperti dibawah
F = "Mabar"             #deklarasi variable
L = "Mobile Legend"

print (F + L)
print (F + " " + L)
print (F + " " + L + " Pada Jam " + str(8) + " atau setelah isya ya :)")

#STRING FORMAT
#Cara efektif selain menggunakan casting dalam menggabungkan kalimat dengan angka atau string dengan integer/float
#print (text.format(variable yang dimasukkan "{}"))

#Contoh:
Pepaya = 6
Anggur = 10
Nanas =3
Lobak =1
Kenari = 7

Kalimat = "Agus membeli beberapa buah-buahan dari pasar yaitu: Pepaya {} buah, Anggur {} buah, Nanas {} buah, Lobak {} buah, dan kacang Kenari {} buah"
print (Kalimat.format(Pepaya, Anggur, Nanas, Lobak, Kenari))

#In vs NOT In
#fungsi yang dapat memeriksa apakah terdapat sebuah substring (bagian kata) dalam sebuah kalimat.
#Contoh: Bio sedang belajar coding bahasa python! Kata "Bio" merupakan substring

#In
Kalimat2 = "Bio sedang belajar coding bahasa python!"
print ("Bio" in Kalimat2)       #jika ada output yang dihasilkan adalah "True"
print ("Belajar" in Kalimat2)   #jika tidak ada output yang dihasilkan adalah "False"

#Not In
print ("Belajar" not in Kalimat2)   #jika tidak ada dalam kalimat maka output yang dihasilkan adalah "True"
print ("python!" not in Kalimat2)   #Jika ada dalam kalimat maka output yang dihasilkan adalah "False"

#Conditional Statement 1 (Booleans)
#Comparison Operators = [> (lebih besar), < (lebih kecil), >= (lebih besar sama dengan), <= (lebih kecil sama dengan), == (sama dengan), != (tidak sama dengan)]
print (10 > 9)   #True
print (10 < 9)   #False
print (10 >= 10) #True
print (10 <= 10) #True
print (10 == 10) #True
print (10 != 10) #False
#Logical Operators = [and = (kedua pernyataan benar maka akan bernilai benar), or = (salah satu dari kedua pernyataan benar maka akan bernilai benar, 
# not = (membalikkan pernyataan hasil, jika pernytaan benar maka akan dinyatakan salah) ]
print (10 > 9 and 10 > 11)   #False
print (10 > 9 or 10 > 11)    #True
print (not (10 > 9))         #False

#Conditional Statement 2 (if, elif, else)
X = "Fabio"
user_input = input("Masukkan Nama anda: ")
if (user_input == X):
    print ("Aku suka dia")
elif (user_input == "Banyu"):                   #elif = else if
    print ("Aku penguasa air")
elif (user_input == "Cyto"):
    print ("Sombong amat hiduplu")
else:
    print ("Aku suka mamahnya daripada dia")

#LOOP STATEMENT
#For loop = perulangan yang digunakan pada parameter tertentu dan selama kondisi terpenuhi 
#For Loop: for i in range (start, end, interval):

#Range:
#print angka kelipatan 6
for i in range (6, 61, 6):
    print (i)
#Contoh hasil = 6, 12, 18, 24, 30, 36, 42, 48, 54, 60
for i in range (10):       #default parameter
    print ("henshin")

#Break and Continue:
#break:
for j in range(3, 31, 2): #mulai pada angka 3, stop pada angka 31, dan jarak antar angka adalah 2
    if j == 21:           #namun jika telah mencapai angka 21, diberhentikan paksa
        break
    print(j)              #posisi print harus setara dengan if, jika tidak hasilnya akan eror

#continue
#print angka genap
for i in range (1, 11):
    if (i % 2 == 1):
        continue
    print (i)

#print angka ganjil
for i in range (1,11):
    if (i % 2 == 0):
        continue
    print (i)

#While loop = perulangan yang akan terus berulang jika kondisinya bernilai true
#Contoh:
Nilai = int(input ("Masukkan nilai: "))

while (Nilai > 70):                #tanda dalam kurung adalah kondisi, dan perulangan terjadi jika kondisi terpenuhi
    print ("nilai anda adalah: " + str(Nilai))
    Nilai += 5                      #parameter atau interval pengulangan
    
    if Nilai >= 100:
        break

Uang = 100

while (Uang > 0):
    print ("Uang anda adalah: " + str(Uang))
    Uang -= 5

if (Uang <= 0):
    print ("Uang anda sudah habis")

#PYTHON COLLECTIONS DATA TYPE 1
# 1. List (listExample) = data yan terurut, data bisa double, bisa diisi dengan berbagai variable, dan dapat terganti.
#    List Operations = Create Data (append & insert), Read Data, Update Data, Delete Data (remove, pop, del, and clear)
#List Operations
listExample = [1, 2, 3, 4, 5, 8.7, 'Biyok']

#Create Data
listExample.append(6)           #Berfungsi memasukkan data pada urutan paling belakang/elemen terakhir
print (listExample)

listExample.insert(2, 7)        #Berfungsi memasukkan data berupa angka 7 pada urutan 2 (2[adalah urutan], 7 [adalah angka yang di insert])
print (listExample)

#Read Data
print(listExample[3])           #Menoutputkan data/print biasa

#Update Data
listExample[1] = 8              #Mengganti/Mengupdate data pada urutan tertentu dengan data yang baru
print (listExample)

#Delete Data
listExample.remove(3)           #Berfungsi menghapus data tertentu/menghapus data yang ada didalam kurung(hal yang ingin dihapus)
print (listExample)

listExample.pop()               #Berfungsi menghapus data pada urutan terakhir/elemen terakhir
print (listExample)

del listExample[0]              #Berfungsi menghapus data tertentu ()/sama seperti listExample.remove
print (listExample)

listExample.clear()             #Berfungsi menghapus keseluruhan data pada list Example
print (listExample)

#List Iterariton = Berfungsi menambahkan logic tambahan, seperti: angka genap pada list
listExample2 = [42, 57, 66, 73, 80]
for item in listExample2:
    if item % 2 == 0:
        print (item)

listExample3 = [40, 55, 20, 75, 80]
listExample4 = [65, 30, 12, 46, 77]
#Method: len, copy, concat (= dan extend), index, sort, reverse
#Length => len(listExample) memberikan informasi mengenai panjangnya data listExample
len(listExample3)
print (len(listExample3))

#Copy => listExample = listExample2.copy(), maka nilai listExample pertama akan sama/tercopy pada listExample2
listExample4 = listExample3.copy()
listExample4[0] = 10
print (listExample3)
print (listExample4)

#concat => menambah pada data pada list example, ex: print(listExample + listExample2) atau listExample.extend(listExample2)
print (listExample3 + listExample4)
listExample3.extend (listExample4)
print (listExample3)

listExample5 = [1, 2, 3, 4, 5]
#Index => mencari sebuah elemen pada urutan berapa pada list, ex: print(listExample2.index(66))
print (listExample5.index(5))

#sort => mensortir/mengurutkan dari data terkecil hingga terbesar jika angka, ex: listExample.sort() --> print
listExample4.sort()
print (listExample4)
#Reverse => membalikkan urutan/posisi data dalam list
listExample3.reverse()
print (listExample3)

#PYTHON COLLECTIONS DATA TYPE 2
#Tuple = berbeda dengan list, elemen tube tidak bisa diubah seperti tupleExample4 = (2, 3) tupleExample4[0] = 10 akan terjadi error
tupleExample = ('Python', 20, 3.8, True, 20)
print (tupleExample)
print (tupleExample[1:3])
print (tupleExample[-2])

#Dictionary = berfungsi untuk menyimpan data dalam bentuk key:value
#Customer = {"id":100, "nama": "budi", "umur":23}
Customer = {
    "nama": "Fabio",
    "id": 100,
    "Umur": 19,
    "pekerjaan": "Dosen"
}

Customer["hobby"] = "bermain game"

print(Customer)
print(Customer['nama'])
print(Customer['id'])
print(Customer['pekerjaan'])

Customer.pop("id")
print (Customer)

#Set = adalah kumpulan elemen unik yang tidak memiliki urutan
#Ex: Union, Intersection, Difference, dan Symetric Difference

numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers2 = {2, 4, 6, 8, 10, 12}

print (numbers1.union(numbers2))                    #union / gabungan
print (numbers2.union(numbers1))
print (numbers1.difference(numbers2))               #difference / terdapat pada salah satu saja
print (numbers2.difference(numbers1))
print (numbers1.intersection(numbers2))             #intersection / irisan
print (numbers2.intersection(numbers1))
print (numbers1.symmetric_difference(numbers2))     #symetric difference / data yang tidak sama pada peluang / lawannya irisan
print (numbers2.symmetric_difference(numbers1))

#FUNCTION
#Function Syntax: 
    # 1. Function Name: nama dari function
    # 2. Argument: nilai yang diberikan ke function
    # 3. Function body: isi dari sebuah function
    # 4. Return Value: Hasil yang dikembalikan oleh function

#Create and call or Passing Argument
def greet ():                   #() = isi dari kurung adalah parameter dan def adalah sebuah function
    print ("hello world")
    print ("sok asik")
greet()

def greet (name, age):              #greet In Python, the "greet" function can be defined using the  def
    print ("Name: " + name)
    print ("Age: " + str(age))
greet("Fabio", 19)

#Lambda Function = berfungsi untuk mempersingkat function
Harga = 10000                          #akan di subtitusi kan kedalam n pada lambda n
Total_belanja = lambda n: n + 50000    #rumus
print (Total_belanja(Harga))            #print total belanja terhadap harga

#CLASS = adalah blueprint untuk membuat sebuah object
#Create Class
class umurku:
    berumur = "19 tahun" 
Umr = umurku()
print(Umr.berumur)

#Init Function = berfungsi untuk mendeklarasi properti yang dimiliki sebuah class

class data_diri:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai
    def greet(self):
        print ("Hallo, " + self.nama + "!")

Siswa1 = data_diri("Fabio", 123450104, 100)
print (Siswa1.nama)
print (Siswa1.nim)
print (Siswa1.nilai)
print (Siswa1.__dict__)         #print semua variable dalam def init
Siswa1.greet()

#Simple Grouping Class
class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def __str__(self):
        return f"Name: {self.name}, Taste: {self.taste}"

class cake(Food):
    def __init__(self, name, taste, flavour, size):
        super().__init__(name, taste)
        self.flavour = flavour
        self.size = size

    def __str__(self):
        return f"Name: {self.name}, Taste: {self.taste}, Flavour: {self.flavour}, Size: {self.size}"

class fast_food(Food):
    def __init__(self, name, taste, part):
        super().__init__(name, taste)
        self.part = part

    def __str__(self):
        return f"Name: {self.name}, Taste: {self.taste}, Part: {self.part}"

    # This method allows adding two customers together
    def __add__(self, other):
        return f"Pelanggan 1: {str(self)}\nPelanggan 2: {str(other)}"

Pelanggan1 = fast_food("Chiken katsu", "pedas", "chiken wings")
Pelanggan2 = cake("strawberry cake", "creamy", "sweet", "medium")

Total_Customer = Pelanggan1 + Pelanggan2
print(Total_Customer)

#File Processing = membuka, membaca, menulis, dan menambahkan/edit file dari VsCode python
#READ / MEMBACA (r)
File = open ("test.txt", "r")           #masih error gak ngerti??
print (File.read())

#Overwrite / menulis ulang file (w)
File = open ("test.txt", "w")
File.write ("Ini adalah text yang baru saya buat")
File.close ()

#Append / menambahkan baris
File = open ("test.txt", "a")
File.write ("Ini adalah text yang baru saya buat")
File.write ("\n nini adalah tugas atau tulisan tambahan")
File.close () 