#Nomor 2
LamaKerja = float(input("Masukkan lama anda bekerja: "))

if LamaKerja < 0:
    print("Input tidak valid")
else:
    GajiPokok = float(input("Masukkan Gaji Pokok anda: "))
    Bonus = 0

    if LamaKerja >= 10:
        Bonus = GajiPokok * 0.15
        print(f"Gaji Pokok anda: {GajiPokok} \nBonus anda adalah: {Bonus}")
        
    elif LamaKerja >= 5:
        Bonus = GajiPokok * 0.1
        print(f"Gaji Pokok anda: {GajiPokok} \nBonus anda adalah: {Bonus}")

    elif LamaKerja >= 2:
        Bonus = GajiPokok * 0.05 
        print(f"Gaji Pokok anda: {GajiPokok} \nBonus anda adalah: {Bonus}")

    elif LamaKerja < 2 and LamaKerja >= 0:
        print("Tidak ada bonus")

    GajiKotor = GajiPokok + Bonus
    print("Total gaji Anda adalah: ", GajiKotor)


#Nomor 4
umur = int(input("Umur anda: "))

if umur < 0 or umur >= 150:
    print("input tidak valid")
elif umur >= 65:
    print("Lansia")
elif umur >= 18:
    print("Dewasa")
elif umur >= 13:
    print("Remaja")
elif umur >= 6:
    print("Anak-anak")
else:
    print("Balita")