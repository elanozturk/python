def mailyap(ad, soyad, uzanti):
    mail = soyad[0] + "." + ad + "@" + uzanti
    mail = mail.lower()
    mail = mail.replace(" ", "")
    mail = mail.replace("ğ", "g")
    mail = mail.replace("ç", "c")
    mail = mail.replace("ş", "s")
    mail = mail.replace("ı", "i")
    mail = mail.replace("ö", "o")
    mail = mail.replace("ü", "u")
    return mail
sonuc = mailyap("Oğuz Serkan","Öztürk","google.com")
print(sonuc)
