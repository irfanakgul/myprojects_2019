
from modulmatematik import carpma1
islem=int(input("islem no giriniz : "))
a=int(input("birinci sayiyi gir: "))

b=int(input("ikinci sayiyi gir: "))

while True:
    if (islem==1):
        print((modulmatematik.toplama1(a,b)))

    elif (islem==2):
        print((modulmatematik.cikarma1(a,b)))
    elif (islem==3):
        print((carpma1(a,b)))
    elif (islem==4):
        print((modulmatematik.bolme1(a,b)))
    elif (islem==5):
        modulmatematik.ust1(a,b)

    elif (islem==6):
        print((modulmatematik.karekok1(a,b)))
    break

# neden sonuc bolumunde none cikiyor.
#  sadece belirli fonksiyonlari alamiyorum.

