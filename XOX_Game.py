a=[1,2,3]
b=[4,5,6]
c=[7,8,9]

girilenler=[]
def koordinatlar_1 ():

    if oyuncu_1==1:
        a[0]="X"

    elif oyuncu_1==2:
        a[1]="X"
    elif oyuncu_1==3:
        a[2]="X"
    elif oyuncu_1==4:
        b[0]="X"
    elif oyuncu_1==5:
        b[1]="X"
    elif oyuncu_1==6:
        b[2]="X"
    elif oyuncu_1==7:
        c[0]="X"
    elif oyuncu_1==8:
        c[1] = "X"
    elif oyuncu_1==9:
        c[2] = "X"
    else:
        print("lutfen 1 ile 9 arasinda bir koordinat giriniz...")
def koordinatlar_2 ():

    if oyuncu_2==1:
        a[0]="O"
    elif oyuncu_2==2:
        a[1]="O"
    elif oyuncu_2==3:
        a[2]="O"
    elif oyuncu_2==4:
        b[0]="O"
    elif oyuncu_2==5:
        b[1]="O"
    elif oyuncu_2==6:
        b[2]="O"
    elif oyuncu_2==7:
        c[0]="O"
    elif oyuncu_2==8:
        c[1] ="O"
    elif oyuncu_2==9:
        c[2] = "O"
    else:
        print("lutfen 1 ile 9 arasinda bir koordinat giriniz...")

def x_win ():
    if (a[0]==a[1]==a[2]):
        print("1. oyuncu kazandi")
        quit()
    elif (b[0]==b[1]==b[2]):
        print("1. oyuncu kazandi")
        quit()
    elif (c[0]==c[1]==c[2]):
        print("1. oyuncu kazandi")
        quit()
    elif (a[0]==b[0]==c[0]):
        print("1. oyuncu kazandi")
        quit()
    elif (a[1]==b[1]==c[1]):
        print("1. oyuncu kazandi")
        quit()
    elif (a[2]==b[2]==c[2]):
        print("1. oyuncu kazandi")
        quit()
    elif (a[0]==b[1]==c[2]):
        print("1. oyuncu kazandi")
        quit()
    elif (c[2]==b[1]==a[0]):
        print("1. oyuncu kazandi")
        quit()
    elif (a[2]==b[1]==c[0]):
        print("1. oyuncu kazandi")
        quit()


def o_win():
    if (a[0]==a[1]==a[2]):
        print("2. oyuncu kazandi")
        quit()
    elif (b[0]==b[1]==b[2]):
        print("2. oyuncu kazandi")
        quit()
    elif (c[0]==c[1]==c[2]):
        print("2. oyuncu kazandi")
        quit()
    elif (a[0]==b[0]==c[0]):
        print("2. oyuncu kazandi")
        quit()
    elif (a[1]==b[1]==c[1]):
        print("2. oyuncu kazandi")
        quit()
    elif (a[2]==b[2]==c[2]):
        print("2. oyuncu kazandi")
        quit()
    elif (a[0]==b[1]==c[2]):
        print("2. oyuncu kazandi")
        quit()
    elif (c[2]==b[1]==a[0]):
        print("2. oyuncu kazandi")
        quit()
    elif (a[2]==b[1]==c[0]):
        print("2. oyuncu kazandi")
        quit()

def dolu ():
    if (a[0] or a[1] or a[2] or b[0] or b[1] or b[2] or c[0] or c[1] or c[2]=="x" or "o"):
        print("Burasi doludur. Baska bir yer seciniz... ")


print("""
*************
X-O-X Oyunu
*************
""")

while True:

    try:
        oyuncu_1 = int(input("1.Oyuncu Lutfen koordinat belirtin : "))

        koordinatlar_1()
        girilenler.append(oyuncu_1)
        print(a,b,c, sep="\n")
        if (len(girilenler)>=9):
            print("Oyun berabere bitti")
            quit()
        x_win()


        oyuncu_2 = int(input("2.Oyuncu Lutfen koordinat belirtin : "))
        koordinatlar_2()
        girilenler.append(oyuncu_2)
        print(a,b,c, sep="\n")
        if (len(girilenler)>=9):
            print("Oyun berabere bitti")
            print(girilenler)
        if o_win():
            print("ikinci oyuncu kazandi")



    except ValueError:
        print("Lutfen bir sayi giriniz...")

# hatalar..
# belirtilen koordinat doluysa bilgi versin.ve ayni kullanicidan devam etsin...
