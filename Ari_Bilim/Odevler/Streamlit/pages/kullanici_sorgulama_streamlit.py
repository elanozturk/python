import streamlit as st

users = {"admin": "1234", "fatih": "1453", "selanik": "1881", "dolmabahce": "1903"}
login_request = st.text_input("Kullanıcı adını giriniz: ")

if login_request in users.keys():
    password_input = st.text_input("Kullanıcı adı tanımlı. Lütfen şifrenizi giriniz: ", type="password")
    if password_input == users[login_request]:
        st.success("Giriş başarılı.")
        #st.snow()  # Snow effect
        #st.experimental_rerun()  # Rerun the app to apply the snow effect
        st.markdown("<meta http-equiv='refresh' content='0;URL=https://www.python.org/' >", unsafe_allow_html=True)

    else:
        st.error("Şifre yanlış")
else:
    st.warning("Kullanıcı adı tanımlı değil.")
