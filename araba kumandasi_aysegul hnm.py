class Kumanda():
    def __init__(self,kapi_durum="kilitli", klima=0,bagaj_durum="kilitli",cam_durumu=5,silecek="0"):
        self.kapi_durum=kapi_durum
        self.klima=klima
        self.bagaj_durum=bagaj_durum
        self.cam_durumu=cam_durumu
        self.silecek=silecek
        
    def kilit_kapa(self):
        secenek=input("kapiyi kilitlemek icin: 'kk' \nbagaji kilitlemek icin: 'bk' \n")
        if secenek=="kk":
            if (self.kapi_durum=="kilitli"):
                print("kapi zaten kilitli")
            else:
                print("kapi kilitleniyor...")
                self.kapi_durum="kilitli"
        else:
            if (self.bagaj_durum=="kilitli"):
                print("kapi zaten kilitli")
            else:
                print("kapi kilitleniyor...")
                self.bagaj_durum="kilitli"
    def kilit_ac(self):
        secenek=input("kapiyi kilitlemek icin: 'ka' \nbagaji kilitlemek icin: 'ba' \n")
        if secenek=="ka":
            if (self.kapi_durum=="acik"):
                print("kapi zaten acik")
            else:
                print("kapi aciliyor...")
                self.kapi_durum="acik"
        else:
            if (self.bagaj_durum=="acik"):
                print("bagaj zaten acik")
            else:
                print("bagaj aciliyor...")
                self.bagaj_durum="acik"
    def klima_ayarlari(self):
        while True:
            cevap=input("isitmak icin:'>' \nsogutmak icin: '<' \nkapatmak icin: 'q' : ")
            
            if cevap=='q' :
                if (self.klima==0):
                    print("klima zaten kapali")
                else:
                    print("klima kapaniyor...")
                    self.klima=0
            elif cevap=='<' :
                derece=int(input("sicakligin kac derece azaltimasini istiyorsunuz: "))
                for i in range (derece):
                    self.klima-=1
                print("sicaklik:: ",self.klima)
                break
            elif cevap=='>' :
                derece=int(input("sicakligin kac derece artirilmasini istiyorsunuz: "))
                for i in range (derece):
                    self.klima+=1
                print("sicaklik:: ",self.klima)
                break
            else:
                print("sicaklik guncellendi:", self.klima)
                break
    def cam(self):
        seviye=int(input("cam seviyesi icin 0-5 arasi bir rakam giriniz\n'tamamen kapatmak icin 5 - tamamen acmak icin 0' :"))
        if (seviye< self.cam_durumu):
            while (seviye<=self.cam_durumu):
                self.cam_durumu-=1
                if (seviye==self.cam_durumu):
                    print("cam istediginiz seviyeye indi",self.cam_durumu)
                    break
        elif (seviye> self.cam_durumu):
            while (seviye>=self.cam_durumu):
                self.cam_durumu+=1
                if (seviye==self.cam_durumu):
                    print("cam istediginiz seviyeye cikti",self.cam_durumu)
                    break
        elif (seviye==self.cam_durumu):
            print("cam zaten istediginiz seviyede",self.cam_durumu)
    def silecek_ayari(self):
        sseviye=input("0-4 arasinda silecek hizi icin bir seviye secebilirsiniz: ")
        if sseviye=="0":
            if self.silecek=="0":
                print("silecekler zaten kapali...")
            else:
                print("silecekler kapaniyor...")
                self.silecek="0"
        if sseviye=="1":
            self.silecek=sseviye
            print("silecekler min hiz modunda calisiyor: ",self.silecek)
        elif sseviye=="2":
            self.silecek=sseviye
            print("silecekler orta modda calisiyor: ",self.silecek)
        elif sseviye=="3":
            self.silecek=sseviye
            print("silecekler hizli modda calisiyor: ",self.silecek)
        elif sseviye=="4":
            self.silecek=sseviye
            print("silecekler max hiz modunda calisiyor: ",self.silecek)
kumanda=Kumanda()
print(""" araba kumandasinada tuslarin amaci:
1- kapi veya bagaj kilidi acmak icin
2- kapi veya bagaj kilidi kapatmak icin
3- klima ayari icin
4- cam ayari icin
5- silecek ayari icin
'cikis' cikmak icin kullanilmaktadir. """)
while True:
    islem=input("yapmak istediginiz islemi seciniz: ")
    if (islem=="cikis"):
        print("islem sonlaniyor...")
        break
    elif (islem=="1"):
        kumanda.kilit_ac()
    elif (islem=="2"):
        kumanda.kilit_kapa()
    elif (islem=="3"):
        kumanda.klima_ayarlari()
    elif (islem=="4"):
        kumanda.cam()
    elif (islem=="5"):
        kumanda.silecek_ayari()
    else:
        print("gecersiz islem")
