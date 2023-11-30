import streamlit as st
import string

def guvenilir_sifre_mi(sifre):
    # Büyük harf, küçük harf, sayı ve sembol içermesi kontrolü
    harf_buyuk = any(c.isupper() for c in sifre)
    harf_kucuk = any(c.islower() for c in sifre)
    rakam_var = any(c.isdigit() for c in sifre)
    sembol_var = any(c in string.punctuation for c in sifre)

    # Şifrenin uzunluğu kontrolü
    uzunluk_kontrol = len(sifre) >= 8

    # Tüm koşulların sağlanıp sağlanmadığını kontrol etme
    return harf_buyuk and harf_kucuk and rakam_var and sembol_var and uzunluk_kontrol

# Streamlit uygulaması
st.title("Şifre Güvenilirlik Kontrolü")

# Kullanıcıdan şifreyi al
kullanici_sifre = st.text_input("Şifrenizi girin:")

# Şifrenin güvenilir olup olmadığını kontrol et ve sonucu göster
if st.button("Şifreyi Kontrol Et"):
    if guvenilir_sifre_mi(kullanici_sifre):
        st.success("Şifre güvenilir.")
    else:
        st.error("Şifre güvenilir değil. Lütfen güvenilir bir şifre seçin. (Şifreniz en az 1 büyük harf, bir küçük harf, sayı ve noktalama işareti içersin.)")
