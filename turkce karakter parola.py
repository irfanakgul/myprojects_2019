tr_karakterler="çöğüş"
parola=input('bir parola giriniz : ')
for karakter in parola:
    if karakter in tr_karakterler:
        print('lutfen turkce karakter kullanmayiniz...')
        tr_karakterler = "çöğüş"
        parola = input('bir parola giriniz : ')
        for karakter in parola:
            if karakter in tr_karakterler:
                print('lutfen turkce karakter kullanmayiniz...')
else:
        print('parolaniz olusturulmustur...')

