import requests

def coinfiyat(coin):
    url = f"https://api.coincap.io/v2/assets/{coin}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        veri = response.json()
        
        # API'den alınan veriyi kullanarak istediğiniz işlemleri gerçekleştirin
        coin_ad = veri['data']['name']
        coin_fiyat = veri['data']['priceUsd']
        
        print(f"{coin_ad} fiyatı: {coin_fiyat} USD")
        
        # İsterseniz veriyi geri döndürebilirsiniz
        return veri['data']
    else:
        print(f"HTTP Hatası: {response.status_code}")
        return None

# Kullanıcıdan kripto para sembolünü al
coin_symbol = input("Kripto para sembolünü girin (örneğin, 'bitcoin'): ")
coin_verisi = coinfiyat(coin_symbol)