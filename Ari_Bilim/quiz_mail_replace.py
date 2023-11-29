isim =input("İsminiz nedir? ")
soyisim =input("Soyisminiz nedir? ")
sirketadi =input("Şirketinizin adı nedir? ")

mail = isim + "." + soyisim + "@" + sirketadi + ".com"
mail = mail.lower()
mail = mail.replace("ç","c")
mail = mail.replace("ğ","g")
mail = mail.replace("ı","i")
mail = mail.replace("ö","o")
mail = mail.replace("ş","s")
mail = mail.replace("ü","u")
mail = mail.replace(" ","")

print(mail)
