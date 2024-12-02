#Program perhitungan diskon pembelian

#meminta jumlah belanja
Jumlah_belanja = float(input("Masukkan jumlah belanja Anda:Rp "))
diskon = ()

#Memeriksa jumlah belanja
if Jumlah_belanja > 0:
    if Jumlah_belanja > 1000000 :
        diskon = 0.20
    elif Jumlah_belanja >= 500000 and Jumlah_belanja <= 1000000 :
        diskon = 0.10
    elif Jumlah_belanja < 500000 :
        diskon = 0.0
else :
    print ("Input tidak Valid. Silahkan masukkan jumlah lain")

#Menghitung jumlah diskon
Jumlah_diskon = Jumlah_belanja * diskon
Total_bayar = Jumlah_belanja - Jumlah_diskon

#Menampilkan hasil perhitungan
print(f"Jumlah belanja: Rp{Jumlah_belanja:,.2f}")
print(f"Diskon: {diskon * 100}%")
print(f"Jumlah diskon: Rp{Jumlah_diskon:,.2f}")
print(f"Total yang harus dibayar: Rp{Total_bayar:,.2f}")
    
    




