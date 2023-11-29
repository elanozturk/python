vergisiz = int(input("Gümrük fiyatını giriniz: "))
motor_hacmi = int(input("Motor hacmini giriniz: "))
kdv = 1.20
bayi = 1.20

if motor_hacmi < 1600:
    if vergisiz < 184000:
        otv = 1.45
    elif vergisiz < 220000:
        otv = 1.50
    elif vergisiz < 250000:
        otv = 1.60
    elif vergisiz < 280000:
        otv = 1.70
    else:
        otv = 1.80
elif motor_hacmi < 2000:
    if vergisiz < 170000:
        otv = 2.30
    else:
        otv = 2.50
else:
    otv = 3.20

satis_fiyati = vergisiz * otv * kdv * bayi
formatted_satis_fiyati = "{:,.2f} TL".format(satis_fiyati)

print("Satış fiyatı: ", formatted_satis_fiyati)
