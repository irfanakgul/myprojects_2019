print("""***************************
  Geometrik Sekil Hesaplama
***************************""")
tercih= input("ucgen mi, dortgen mi?\nSeciniz :")
print("tercihiniz: ", tercih)

if tercih=="dortgen":
    kenar1= input("kenar1 : ")
    kenar2=input("kenar2 : ")
    kenar3=input("kenar3 : ")
    kenar4=input("kenar4 : ")

if kenar1==kenar2==kenar3==kenar4 :
    print("Bu dortgen bir KARE`dir")
elif (kenar1 and kenar2 and kenar3 and kenar4):
    print("Bu dortgen bir dik dortgen degildir")


if tercih=="ucgen":
    kenar1 = input("kenar1 : ")
    kenar2 = input("kenar2 : ")
    kenar3 = input("kenar3 : ")
if kenar1==kenar2==kenar3 :
    print("Bu ucgen bir es kenar ucgendir")
elif kenar1 == kenar2 != kenar3 :
    print("bu ikizkenar bir ucgendir.")
elif kenar1 != kenar2 == kenar3 :
    print("bu ikizkenar bir ucgendir.")
elif kenar1 != kenar3 == kenar2 :
    print("bu ikizkenar bir ucgendir.")

