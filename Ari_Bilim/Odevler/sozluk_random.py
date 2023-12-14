import random

sozluk = {
    "software": "yazılım",
    "hardware": "donanım",
    "input": "girdi",
    "output": "çıktı",
    "average": "ortalama",
    "sum": "toplam"
}
dogru = 0
yanlis = 0

#eleman = len(sozluk)
#print(eleman)
while len(sozluk) > 0:
    soru = random.choice(list(sozluk.keys())) # random sözlüklerde çalışmadığı için listeye çeviriyoruz.
    print('"'+soru+'" nedir?')
    #eleman -= 1  # Her döngüde eleman sayısını bir azaltın
    istenen_cevap = sozluk.get(soru)
    #print(istenen_cevap)
    verilen_cevap = input("Yanıtınız nedir? ")
    if istenen_cevap != verilen_cevap:
       print("Yanlış cevap! Doğru cevap "+"'" + istenen_cevap + "' olacaktı.")
       yanlis=yanlis+1
    else:
      print("Cevabınız doğru.")
      sozluk.pop(soru)
      dogru=dogru+1
print("Tebrikler ödev bitti")
print("Doğru sayısı "+str(dogru)+", Yanlış sayısı "+str(yanlis))