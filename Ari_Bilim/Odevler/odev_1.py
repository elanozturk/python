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
       print("..............")
else:
    print("Kullanıcı adı bulunamadı.")
    print(".........................")


# Comment all lines wit CTRL+C and K.
# De-comment all lines with Ctrl+K AND U.

# #import streamlit as st 
# # def main():
# #     kullaniciadi = "yönetici"
# #     sifre = "1903"

# #     login_name = st.text_input("Kullanıcı adı:")

# #     if kullaniciadi == login_name:
# #         st.success("Kullanıcı adı doğrulandı.")
# #         login_pass = st.text_input("Parola:", type="password")

# #         if sifre == login_pass:
# #             st.success("Parola doğru, giriş başarılı.")
# #         else:
# #             st.error("Parola hatalı!")
# #     else:
# #         st.warning("Kullanıcı adı bulunamadı.")

# # if __name__ == "__main__":
# #     main()

