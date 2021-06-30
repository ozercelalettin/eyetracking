print("""
****************************
ATM UYGULAMASI

İŞLEMLER
1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme

Son vermek için 'q' ya basın!
****************************
""")

bakiye = 1000

while True:
    işlem = input("İşlem Seçiniz:")

    if (işlem == "q"):
        print("İşleminiz Sonlandırılmıştır")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı Giriniz:"))
        bakiye += miktar

    elif (işlem == "3"):
        miktar = int(input("Miktarı Giriniz:"))

        if (bakiye - miktar < 0):
            print("Bakiye Yetersiz")
            continue
        bakiye -= miktar

    else:
        print("İşlem Geçersiz!")
