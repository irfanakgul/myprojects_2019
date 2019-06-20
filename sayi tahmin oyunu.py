import random
import time

print("""***********
sayi tahmin oyunu
1 ile 40 arasinda bir sayi tahmin edin.
************
""")

rastgele_sayi=random.randint(1,40)
tahminsayisi=7
while True:
    tahmin=int(input("Bir tahminde bulunun :"))

    if (tahmin<rastgele_sayi):
        print('Lutfen yukari cikin')
        tahminsayisi-=1
        print("Kalan tahmin hakkiniz:", tahminsayisi, "`dir.")


    elif (tahmin>rastgele_sayi):
        print("lutfen asagi inin..")
        print("Kalan tahmin hakkiniz:", tahminsayisi, "`dir.")
        tahminsayisi-=1

    elif(tahmin==rastgele_sayi):
        print("Tebrikler bildiniz...")
        break
    if (tahminsayisi == 0):
        print("Tahmin hakkiniz kalmamistir,,")
        break