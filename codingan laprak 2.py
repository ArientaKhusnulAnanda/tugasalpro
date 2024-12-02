#meminta pengguna memasukkan tahun lama bekerja
lama_kerja = float(input("masukkan lama kerja(tahun):"))

#menentukan bonus yang didapat sesuai kondisi
if lama_kerja<0:
       print("input tidak valid")
elif (lama_kerja>=10):
        gaji_pokok = int (input("masukkan gaji pokok:"))
        bonus1 = gaji_pokok*0.15
        print("bonus pegawai sebesar:",bonus1)
elif (lama_kerja>=5):
        gaji_pokok = int (input("masukkan gaji pokok:"))
        bonus2 = gaji_pokok*0.1
        print("bonus pegawai sebesar:",bonus2)
elif(lama_kerja>=2):
        gaji_pokok = int (input("masukkan gaji pokok:"))
        bonus3 = gaji_pokok*0.05
        print("bonus pegawai sebesar:",bonus3)
else:
        print("tidak ada bonus")