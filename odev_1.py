#ÖDEV (BURDA YANİ Google Colab'da yapalım, sonra streamlitte çalışan versiyonunu da yapalım)

#streamlitte şifre ve kullanıcı adı alalım girilen bilgilere göre ekrana bişeyler yazdıralım

#sifre ve kullanıcı adımızın yukarıdaki gibi olduğunu varsayalım. Kullanıcıdan bir kullanıcı adı ve şifre girmesini isteyelim.

#Kullanıcı adı hatalıysa kullanıcı bulunamadı
#Şifre hatalıysa şifreniz hatalı
#İkisi de doğruysa giriş başarılı
#İkisi de hatalıysa giriş bilgileri hatalı  şeklinde sonuçlar göstersin

kullaniciadi="yönetici"
sifre="1903"

login_name = input("Kullanıcı adı: ")

if kullaniciadi == login_name:
    print("Kullanıcı adı doğrulandı.")
    login_pass = input("Parola: ")
    
    if sifre == login_pass:
       print("Parola doğru, giriş başarılı.")    
    else:
       print("Parola hatalı!")
else:
    print("Kullanıcı adı bulunamadı.")
