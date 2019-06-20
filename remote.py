import time

class air_remote ():
    def __init__(self,statu="OFF", degree=20, mode="summer",):
        self.statu=statu
        self.degree=degree
        self.mode=mode

    def air_close (self):
        if tercih=="close":
            if self.statu=="ON":
                print("Klima kapaniyor...\nGule Gule.. ")
                time.sleep(2)
                print("Klima Kapandi...")
                self.statu=="OFF"
            elif self.statu=="OFF":
                print("Klima zaten kapali !!! ")
        self.statu="OFF"

    def air_open (self):
        if tercih =="open":
            if self.statu=="OFF":
                print("Klima aciliyor..")
                time.sleep(2)
                print("HOS GELDINIZ...")
                self.statu=="ON"
            elif self.statu=="ON":
                print("Klima zaten acik !!! ")
        self.statu = "ON"
    def degree_plus (self):
        if tercih==">" :
            if self.degree==32:
                print("Maximum dereceye ulastiniz...")
                time.sleep(2)
                print("MAX Derece : ", self.degree)
            else:
                self.degree +=1
                print("Derece : ", self.degree)
    def degree_neg (self):
        if tercih == "<":
            if self.degree == 17:
                print("Minimum dereceye ulastiniz...")
                time.sleep(2)
                print("MIN Derece : ", self.degree)
            else:
                self.degree -= 1
                print("Derece : ", self.degree)

    def summer_mode(self):

        if tercih == "summer":
            if self.mode == "winter":
                print(" SUMMER moduna gecildi..")
                self.mode = "summer"
            elif self.mode == "summer":
                print("Zaten summer modundasiniz...")
                self.mode == "summer"

    def winter_mode (self):

        if tercih=="winter":
            if self.mode=="summer":
                print(" WINTER moduna gecildi..")
                self.mode="winter"
            elif self.mode=="winter":
                print("Zaten WINTER modundasiniz...")
                self.mode=="winter"

air_remote=air_remote()
print("""
*******************************
### Air Conditioning Remote ###
*******************************
Please pressing to one those: 

 For Closing       :  Close
 For Opening       :  Open
 For Degree +      :  >
 For Degree -      :  <
 For Summer Mode   :  summer
 For Winter Mode   :  winter
 For EXIT          :  exit
""")

while True:
    tercih=input("Yapmak istediginiz Islemi seciniz ? : ")

    if tercih=="exit":
        print("Cikis yapiliyor...")
        time.sleep(3)
        print("BYE BYE !!!")
        break

    elif tercih=="close":
        air_remote.air_close()
        quit()

    elif tercih=="open":
        air_remote.air_open()


    elif tercih==">":
        air_remote.degree_plus()

    elif tercih=="<":
        air_remote.degree_neg()

    elif tercih=="winter":
        air_remote.winter_mode()

    elif tercih=="summer":
        air_remote.summer_mode()

    else:
        print("Lutfen gecerli bir islem seciniz !!! ")
