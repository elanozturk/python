# #ÖDEV

# #"https://api.nationalize.io/?name=damla"

# # Bu api isminizin hangi ülkeye ait olduğu ihtimalini veriyor.
# # Örnekteki url'nin sonundaki isim değiştirilerek kullanılabiliyor
# # Bu apiyi kullanarak girilen ismin yüzde cinsinden
# # kaç ihtimalle hangi ülkeye ait olduğunu getirsin
# # %75 TR
# # %23 AT
# #....

# import requests

# isim = input("İsminizi giriniz: ")
# url = f"https://api.nationalize.io/?name={isim}"
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Hata kodu: {response.status_code}, Hata mesajı: {response.text}")
import requests

isim = input("İsminizi giriniz: ")
url = f"https://api.nationalize.io/?name={isim}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()    
    country_probabilities = data.get("country")
    if country_probabilities:
        for entry in country_probabilities:
            country_name = entry.get("country_id")
            probability = entry.get("probability") * 100
            print(f"%{probability:.2f} {country_name}")
    else:
        print("Bu isim için ülke tahmini bulunamadı.")
else:
    print(f"Hata kodu: {response.status_code}, Hata mesajı: {response.text}")

