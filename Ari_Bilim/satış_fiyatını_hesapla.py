def satış_fiyatını_hesapla(motor_hacmi, matrah):
    # Bayi karı %20
    bayi_kari_oranı = 0.20
    bayi_kari = matrah * bayi_kari_oranı

    # KDV oranı %18
    kdv_oranı = 0.18
    kdv_tutarı = (matrah + bayi_kari) * kdv_oranı

    # Vergi dilimine göre ÖTV oranını belirle
    ovt_oranı = 0.45 if motor_hacmi <= 1600 and matrah <= 184000 else \
                 0.50 if motor_hacmi <= 1600 and 184000 < matrah <= 220000 else \
                 0.60 if motor_hacmi <= 1600 and 220000 < matrah <= 250000 else \
                 0.70 if motor_hacmi <= 1600 and 250000 < matrah <= 280000 else \
                 0.80 if motor_hacmi <= 1600 else \
                 1.30 if 1600 < motor_hacmi <= 2000 and matrah <= 170000 else \
                 1.50 if 1600 < motor_hacmi <= 2000 else \
                 2.20

    # ÖTV tutarı
    ovt_tutarı = (matrah + bayi_kari) * ovt_oranı

    # Toplam satış fiyatını hesapla
    toplam_fiyat = matrah + bayi_kari + kdv_tutarı + ovt_tutarı

    return toplam_fiyat

# Kullanıcıdan giriş al
motor_hacmi = float(input("Araç motor hacmi (cm³): "))
matrah = float(input("Araç matrah fiyatı (TL): "))

# Satış fiyatını hesapla
sonuc = satış_fiyatını_hesapla(motor_hacmi, matrah)

# Sonucu ekrana yazdır
print(f"Araç satış fiyatı (KDV ve ÖTV dahil): {sonuc:.2f} TL")
