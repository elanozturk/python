sozluk = {
    "software": "yazılım",
    "hardware": "donanım",
    "input": "girdi",
    "output": "çıktı",
    "average": "ortalama",
    "sum": "toplam"
}

dogru_cevaplar = {kelime: False for kelime in sozluk}
dogru_sayisi = 0
yanlis_sayisi = 0

while any(not dogru for dogru in dogru_cevaplar.values()):
    kelime = next(k for k, v in dogru_cevaplar.items() if not v)
    cevap = input(f"{kelime} kelimesinin Türkçe karşılığı nedir? ").lower()

    if cevap == sozluk[kelime]:
        print("Doğru! 👍")
        dogru_sayisi += 1
    else:
        print(f"Yanlış. Doğru cevap: {sozluk[kelime]}")
        yanlis_sayisi += 1

    dogru_cevaplar[kelime] = True

print(f"\nToplam doğru sayısı: {dogru_sayisi}")
print(f"Toplam yanlış sayısı: {yanlis_sayisi}")
