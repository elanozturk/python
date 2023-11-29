from time import sleep
import _datetime as dt

dogumyılı = int(input("Doğduğunuz yılı girin: "))
dogumayı = int(input("Doğduğunuz ayı girin: "))
dogumgunu = int(input("Doğduğunuz günü girin: "))

dogumtarihi = dt.date(dogumyılı, dogumayı, dogumgunu)
bugun = dt.date.today()

gecen_sure = bugun - dogumtarihi
gecen_gun = gecen_sure.days

print("Doğum tarihinizden bugüne kadar geçen gün: {:,}".format(gecen_gun))
sleep(10)
print ("Program sonlandırılıyor...")