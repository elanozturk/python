import streamlit as st
import yaml
from yaml import SafeLoader
import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

with open("credentials.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Giriş', 'main')

if authentication_status:
    authenticator.logout('Çıkış', 'main')
    st.write(f'Hoşgeldiniz *{name}*')
    st.title('Some content')

    # Yönlendirme için success veya write fonksiyonlarını kullanabilirsiniz
    st.write('[Giriş sayfasına yönlendiriliyorsunuz](https://www.python.org/)')
    st.redirect("https://www.python.org")

elif authentication_status is False:
    st.error("Kullanıcı adı ve şifre hatalı.")
elif authentication_status is None:
    st.warning('Lütfen kullanıcı adı ve şifrenizi giriniz.')
