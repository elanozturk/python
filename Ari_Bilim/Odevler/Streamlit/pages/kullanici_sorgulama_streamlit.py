import streamlit as st

users = {"admin": "1234", "fatih": "1453", "selanik": "1881", "dolmabahce": "1903"}
login_request = st.text_input("Kullanıcı adını giriniz: ")

if login_request in users.keys():
    st.text_input_password = st.text_input("Kullanıcı adı tanımlı. Lütfen şifrenizi giriniz: ")
    if st.text_input_password == users[login_request]:
        print("Giriş başarılı.")
    else:
        print("Şifre yanlış")
else:
    print("Kullanıcı adı tanımlı değil.")