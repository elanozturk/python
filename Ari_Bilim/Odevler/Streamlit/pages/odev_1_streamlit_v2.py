import streamlit as st
import yaml
from yaml import SafeLoader
import streamlit_authenticator as stauth

with open("credentials.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

authenticator = stauth.Authenticate(
    config.get('credentials'),
    config['cookie']['name'],
    config['cookie']['key']
)

name, authentication_status, username = authenticator.login('Giriş', 'main')

if authentication_status:
    authenticator.logout('Çıkış', 'main')
    st.write(f'Hoşgeldiniz *{name}*')
    st.title('Giriş')

elif authentication_status is False:
    st.error("Kullanıcı adı ve şifre hatalı.")
elif authentication_status is None:
    pass  # Do nothing if authentication_status is None

elif authentication_status is True:
    st.success("Giriş başarılı.")
    st.markdown("<meta http-equiv='refresh' content='0;URL=https://www.python.org/' >", unsafe_allow_html=True)
    ##st.write("Giriş başarılı")

else:
    st.warning('Lütfen kullanıcı adı ve şifrenizi giriniz.')
