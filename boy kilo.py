print("""beden kitle index""")

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))
bki=kilo/boy**2
print("bki:", bki)
if (bki >= 18.5):
    print('zayif')
elif (bki >= 18.5 and bki < 25):
    print('normal')
elif (bki >= 25 and bki < 30):
    print(' kilolu')
elif (bki >= 30):
    print('obez')

else:
    print('sonuc yok')
