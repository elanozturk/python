import string

# Kullanıcının girdiği şifreyi kontrol et
kullanici_sifre = input("Lütfen şifrenizi girin: ")

# Büyük harf, küçük harf, sayı ve sembol içermesi kontrolü
harf_buyuk = any(c.isupper() for c in kullanici_sifre)
harf_kucuk = any(c.islower() for c in kullanici_sifre)
rakam_var = any(c.isdigit() for c in kullanici_sifre)
sembol_var = any(c in string.punctuation for c in kullanici_sifre)

# Şifrenin uzunluğu kontrolü
uzunluk_kontrol = len(kullanici_sifre) >= 8

# Tüm koşulların sağlanıp sağlanmadığını kontrol etme
if harf_buyuk and harf_kucuk and rakam_var and sembol_var and uzunluk_kontrol:
    print("Şifre güvenilir.")
else:
    print("Şifre güvenilir değil. Lütfen güvenilir bir şifre seçin.")
