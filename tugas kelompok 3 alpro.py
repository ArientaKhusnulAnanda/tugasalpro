#kasus1
nilai=int(input("Masukkan nilai anda:"))
if nilai == 100 or nilai <=0:
    print("nilai tidak valid, masukkan lagi.")
elif nilai >= 90:
    print(f"dengan nilai: {nilai}, maka grade anda A")
elif nilai >= 80:
    print(f"dengan nilai: {nilai}, maka grade anda B")
elif nilai >= 70:
    print(f"dengan nilai: {nilai}, maka grade anda C")
elif nilai >= 60:
    print(f"dengan nilai: {nilai}, maka grade anda D")
else:
    print(f"dengan nilai: {nilai}, maka grade anda E")
    

#kasus3
totalBelanja = float(input("Masukkan Junmlah Belanja anda:"))
diskon=()
if totalBelanja <= 0:
    print("input tidak valid.")
elif totalBelanja >= 1000000:
    diskon = (totalBelanja * 0.20)
    setelah_diskon = (totalBelanja - diskon)
    print(f"Diskon 20%, Total Bayar:Rp.{setelah_diskon:.2f}")
elif totalBelanja >= 500000:
    diskon = (totalBelanja * 0.10)
    setelah_diskon = (totalBelanja - diskon)
    print(f"Diskon 10%, Total Bayar:Rp.{setelah_diskon:.2f}")
else:
    diskon = (totalBelanja * 0.00)
    setelah_diskon = (totalBelanja - diskon)
    print(f"Diskon 0%, Total Bayar:Rp.{setelah_diskon:.2f}")

#kasus5
income = float(input("Masukkan Junmlah Pendapatan anda:"))
pajak=()
if income <= 0:
    print("input tidak valid.")
elif income >= 500000000:
    pajak = (income * 0.30)
    print(f"Pajak yang harus dibayar:Rp.{pajak:.2f}")
elif totalBelanja >= 100000001:
    pajak = (income * 0.15)
    print(f"Pajak yang harus dibayar:Rp.{pajak:.2f}")
elif totalBelanja >= 50000001:
    pajak = (income * 0.05)
    print(f"Pajak yang harus dibayar:Rp.{pajak:.2f}")
else:
    pajak = (income * 0.00)
    print(f"Pajak yang harus dibayar:Rp.{pajak:.2f}")