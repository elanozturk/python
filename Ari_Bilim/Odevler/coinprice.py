import requests

def coinprice(coin):
    url = f"https://api.coincap.io/v2/assets/{coin}"
    veri = requests.get(url)
    
    if veri.status_code == 200:
        data = veri.json()
        if 'data' in data:
            coin_data = data['data']
            for key, value in coin_data.items():
                print(f"{key}: {value}")
        else:
            print("Coin verisi bulunamadı.")
    else:
        print(f"Hata kodu: {veri.status_code}")

# Örnek kullanım
#coinprice("bitcoin")