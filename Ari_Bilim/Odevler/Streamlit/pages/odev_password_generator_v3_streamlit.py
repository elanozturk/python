import streamlit as st
import random
import string
import hashlib

st.title("Şifre Oluşturucu")

length = st.slider("Şifre Uzunluğu", min_value=8, max_value=50, value=12, step=1)
uppercase_count = st.slider("Büyük Harf Sayısı", min_value=1, max_value=length, value=2, step=1)
lowercase_count = st.slider("Küçük Harf Sayısı", min_value=1, max_value=length, value=2, step=1)
punctuation_count = st.slider("Noktalama İşareti Sayısı", min_value=1, max_value=length, value=2, step=1)
digit_count = st.slider("Sayı Sayısı", min_value=1, max_value=length, value=2, step=1)

if st.button("Şifre Oluştur"):
    total_chars = uppercase_count + lowercase_count + punctuation_count + digit_count
    if total_chars > length:
        st.error("Hata: Toplam karakter sayısı şifre uzunluğundan büyük olamaz.")
    else:
        password = ""

        for _ in range(uppercase_count):
            password += random.choice(string.ascii_uppercase)

        for _ in range(lowercase_count):
            password += random.choice(string.ascii_lowercase)

        for _ in range(punctuation_count):
            password += random.choice(string.punctuation)

        for _ in range(digit_count):
            password += random.choice(string.digits)

        while len(password) < length:
            category = random.choice(["uppercase", "lowercase", "punctuation", "digit"])
            if category == "uppercase":
                password += random.choice(string.ascii_uppercase)
            elif category == "lowercase":
                password += random.choice(string.ascii_lowercase)
            elif category == "punctuation":
                password += random.choice(string.punctuation)
            elif category == "digit":
                password += random.choice(string.digits)

        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        st.success("Oluşturulan Şifre: " + password)

        md5 = hashlib.md5(password.encode()).hexdigest()
        sha1 = hashlib.sha1(password.encode()).hexdigest()
        sha256 = hashlib.sha256(password.encode()).hexdigest()
        sha512 = hashlib.sha512(password.encode()).hexdigest()

        st.write("MD5 hali:", md5)
        st.write("SHA1 hali:", sha1)
        st.write("SHA256 hali:", sha256)
        st.write("SHA512 hali:", sha512)
