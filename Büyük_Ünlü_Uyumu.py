#Girilen kelimenin büyük ünlü uyumuna uyup uymadığını kontrol eden program
kelime = input("Kelime giriniz: ")
kelime = kelime.lower()

kalinsay = 0
incesay = 0

incesay = kelime.count("e") + kelime.count("i") + kelime.count("ü") + kelime.count("ö")
kalinsay = kelime.count("a") + kelime.count("ı") + kelime.count("u") + kelime.count("o")

print("İnce ünlü sayısı: ", incesay)
print("Kalın ünlü sayısı: ", kalinsay)

if kalinsay + incesay == 1:
    print("Büyük ünlü uyumu aranmaz.")
elif kalinsay > 0 and incesay == 0:
    print("Büyük ünlü uyumuna uyuyor.")
elif kalinsay == 0 and incesay > 0:
    print("Büyük ünlü uyumuna uyuyor.")
else:
    print("Büyük ünlü uyumuna uymuyor.")

