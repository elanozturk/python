# ÖDEV 2 (BURDA YANİ Google Colab'da yapalım, sonra streamlitte çalışan versiyonunu da yapalım)

ogrenciler = ["Ali","Fatma","Mehmet","Çağrı"]

ogrenci = input("Öğrenci Adı Giriniz: ")

ogrenci = ogrenci.title()

if ogrenci in ogrenciler:
    print(ogrenci, "listede zaten mevcut. Başka bir isim ekleyiniz.")
else:
     ogrenciler.append(ogrenci)

     print(ogrenci, "listeye eklendi.")

     print(ogrenciler)


# öğrenci yoksa ekle ve bilgi ver.
# öğrenci varsa ekleme ve öğrenci zaten var diye bilgi ver.
# en son öğrencileri yazdır.
# buraya kadar.


