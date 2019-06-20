print("""*******************************
 while dongulu Kullanici Paneli
*******************************""")
sys_kullanici_adi = "irfanakgl"
sys_parola = "abc123"

while (True):
    kullanici_adi = input('Kullanici Adiniz : ')
    kullanici_parola = input("Parolaniz : ")

    if (kullanici_adi==sys_kullanici_adi) and (kullanici_parola==sys_parola):
        print('Tebrikler.. Sisteme giris yaptiniz...')
        break
    elif (kullanici_adi == sys_kullanici_adi) and (kullanici_parola != sys_parola):
        print('Parolaniz yanlistir. Parolanizi unuttunuz mu? E/H')
        cevap = input('E/H : ')
        if (cevap=='E'):
            yeni_parola=input("Yeni parola Giriniz : ")
            sys_parola=yeni_parola

        elif (cevap=='H'):
            print('Lutfen tekrar giris yapiniz...')
    elif (kullanici_adi != sys_kullanici_adi) and (kullanici_parola == sys_parola):
            print('Kullanici adiniz yanlistir..')
            print('Lutfen tekrar giris yapiniz...')


