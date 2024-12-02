class aku():
    def __init__(self, nama, umur, pasangan, hobi):
        self.nama = nama
        self.umur = umur
        self.pasangan = pasangan
        self.hobi = hobi
    def info(self):
        return f"{self.nama} {self.umur} {self.pasangan} {self.hobi}"
    
Akuadalah=aku("Fabio Banyu Cyto, ", "20 tahun, ", "blom ada, ", "main game")
print(Akuadalah.info())
        