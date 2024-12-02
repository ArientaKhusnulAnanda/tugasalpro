#Nomor 1
class MobilLengkap:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model
        self.mesin_hidup = False
        self.gigi = 0

    def hidupkanMobil(self):
        if not self.mesin_hidup:
            self.mesin_hidup = True
            print(f"Mobil {self.merk} {self.model} dihidupkan")
        else:
            print(f"Mobil {self.merk} {self.model} Sudah Menyala")

    def MatikanMobil(self):
        if self.mesin_hidup:
            self.mesin_hidup = False
            print(f"Mobil {self.merk} {self.model} dimatikan\n")
        else:
            print(f"Mobil{self.merk} {self.model} sudah mati\n")

    def ubahGigi(self, gigi_baru):
        if self.mesin_hidup:
            self.gigi = gigi_baru
            print(f"Gigi Mobil {self.merk} {self.model} diubah ke {self.gigi}")
        else:
            print(f"Tidak Bisa Mengubah gigi {self.merk} {self.model} belum dihidupkan\n")

class MobilLengkapJalan:
    def __init__(self):
        self.mobil = MobilLengkap("Nissan", "GTR")

    def jalan(self):
        self.mobil.hidupkanMobil()
        self.mobil.ubahGigi(1)
        self.mobil.ubahGigi(2)
        self.mobil.ubahGigi(3)
        self.mobil.ubahGigi(4)
        self.mobil.MatikanMobil()

aksi = MobilLengkapJalan()
aksi.jalan()


#Nomor 2
class Matematika:
    def pertambahan(self, a, b):
         return a + b
    
    def pengurangan(self,a, b):
        return a - b
    
    def perkalian(self, a, b):
         return a * b
    
    def pembagian(self, a, b):
        return a / b


def main():

    kalkulator = Matematika()

    print(f"Pertambahan a + b: {kalkulator.pertambahan(20, 20)}")
    print(f"Pertambahan a + b: {kalkulator.pengurangan(10, 5)}")
    print(f"Pertambahan a + b: {kalkulator.perkalian(10, 20)}")
    print(f"Pertambahan a + b: {kalkulator.pembagian(21, 2)}\n")

if __name__ == "__main__":
    main()


#Nomor 3
class Buku:
    def __init__(self, Judul, Pengarang, Penerbit, Tahun):
        self.Judul = Judul
        self.Pengarang = Pengarang
        self.Penerbit = Penerbit
        self.Tahun = Tahun

    def cetakbuku(self):
        print(f"Judul: {self.Judul}\nPengarang: {self.Pengarang}\nPenerbit: {self.Penerbit}\nTahun: {self.Tahun}")

def BukuBeraksi():
        Buku_pertama = Buku("Pemrograman Berbasis Objek dengan Python", "Tirta Setiawan", "ITERA PRESS", 2024)
        Buku_kedua = Buku("Dasar Pemrograman Python", "Fulana", "Sains Data Press", 2024)

        print("Buku pertama: ")
        Buku_pertama.cetakbuku()

        print("\nBuku kedua: ")
        Buku_kedua.cetakbuku()
    
BukuBeraksi()