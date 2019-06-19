print("""***************************
  Not Hesaplama Programi

  Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF

***************************""")

vize1 = int(input("ilk notunuzu giriniz    : "))
vize2 = int(input("ikinci notunuzu giriniz : "))
final = int(input("Final notunuzu giriniz  : "))

Sonuc = (vize1 * 30 / 100) + (vize2 * 30 / 100) + (final * 40 / 100)

print('sonuc', Sonuc)

if Sonuc >= 90:
    print("AA ve Gectiniz...")
elif Sonuc >= 85:
    print("BA ve Gectiniz...")
elif Sonuc >= 80:
    print("BB ve Gectiniz...")
elif Sonuc >= 75:
    print("CB ve Gectiniz...")
elif Sonuc >= 70:
    print("CC ve Gectiniz...")
elif Sonuc >= 65:
    print("DC ve Sartli Gectiniz...")
elif Sonuc >= 60:
    print("DD ve Kaldiniz...")
elif Sonuc >= 55:
    print("DF ve Kaldiniz...")
elif Sonuc < 55 and Sonuc > 0:
    print("FF ve Kaldiniz...")
else:
    print("Lutfen gecerli bir sonuc giriniz...")