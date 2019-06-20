giris = print(""""
*******************
   ATM Makinesi
*******************
Islemler: 

1) Bakiye Sorgulama
2) Para Yatirma
3) Para Cekme
4) Cikis
""")
bakiye=3500
tercih = input("Yapmak istediginiz islemin numarasini giriniz : ")


while True:
    if (tercih=="1"):
        print("Bakiyeniz : ",bakiye, "TL`dir.")




    elif (tercih=="2"):
        yatirilan= int(input('Yatirmak istediginiz tutari giriniz: '))
        guncel_bakiye=bakiye+yatirilan
        bakiye=guncel_bakiye
        print('Bakiyeniz:', guncel_bakiye, "TL`dir")


    elif ( tercih=="3"):
        cekilen = int(input('cekmek istediginiz tutari giriniz: '))
        guncel_bakiye = bakiye - cekilen
        bakiye = guncel_bakiye
        print('Bakiyeniz:', guncel_bakiye, "TL`dir")



    elif (tercih=="4"):
        print("Bankamizi kullandiginiz icin tesekkur ederiz..")

    else:
        while True:
            print ("lutfen gecerli bir islem numarasi giriniz...")
            tercih = input("Yapmak istediginiz islemin numarasini giriniz : ")



            if (tercih == "1"):
                print("Bakiyeniz : ", bakiye, "TL`dir.")




            elif (tercih == "2"):
                yatirilan = int(input('Yatirmak istediginiz tutari giriniz: '))
                guncel_bakiye = bakiye + yatirilan
                bakiye = guncel_bakiye
                print('Bakiyeniz:', guncel_bakiye, "TL`dir")


            elif (tercih == "3"):
                cekilen = int(input('cekmek istediginiz tutari giriniz: '))
                guncel_bakiye = bakiye - cekilen
                bakiye = guncel_bakiye
                print('Bakiyeniz:', guncel_bakiye, "TL`dir")



            elif (tercih == "4"):
                print("Bankamizi kullandiginiz icin tesekkur ederiz..")

            break




    break

