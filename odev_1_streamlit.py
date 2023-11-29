import streamlit as st

kullanici_adi = "yönetici"
sifre = "1903"

login_name = st.text_input("Kullanıcı adı:")

if kullanici_adi == login_name:
    st.success("Kullanıcı adı doğrulandı.")
    login_pass = st.text_input("Parola:", type="password")

    if sifre == login_pass:
        st.success("Parola doğru, giriş başarılı.")
    else:
        st.error("Parola hatalı!")
else:
    st.warning("Kullanıcı adı bulunamadı.")
