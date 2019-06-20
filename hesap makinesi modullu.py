 import math

print("""
********************************
|||      HESAP MAKINESI      |||
********************************
||| 1) Toplama islemi        ||| 
||| 2) cikarma islemi        ||| 
||| 3) carpma islemi         |||
||| 4) bolme islemi          ||| 
||| 5) ust bulma             ||| 
||| 6) karekokunu bulma      |||
||| 7) cikis                 ||| 
********************************

""")
islem=int(input("Islem numarasini Giriniz : "))

birincisayi = int(input("Birinci Sayiyi Giriniz : "))

ikincisayi = int(input("Ikinci Sayiyi Giriniz : "))

while True:


    if (islem==1) :
        print("SONUCUNUZ : ", birincisayi+ikincisayi)
    elif (islem==2) :
        print("SONUCUNUZ : ", birincisayi-ikincisayi)
    elif (islem==3) :
        print("SONUCUNUZ : ", birincisayi*ikincisayi)
    elif (islem==4) :
        print("SONUCUNUZ : ", birincisayi/ikincisayi)

    elif (islem==5):
        print((pow(birincisayi,ikincisayi)))
    elif (islem==6):
        print(("Birinci sayinin karekoku", math.sqrt(birincisayi)))

    elif (islem==7):
        print("gule gule")

    else:
        print("Lutfen gecerli bir sayi giriniz!")
    break

#her islmeden sonra yeniden islem bolumu acilmiyor
#gule gule demek icin birinci ve ikinci sayinin girilmesini istiyor.
#break nereye koyulmali





