import random
import string

def generate_password():
    length = int(input("Şifrenin uzunluğunu girin: "))
    uppercase_count = int(input("Kaç büyük harf içersin?: "))
    lowercase_count = int(input("Kaç küçük harf içersin?: "))
    punctuation_count = int(input("Kaç noktalama işareti içersin?: "))
    digit_count = int(input("Kaç sayı içersin?: "))
    underscore_count = int(input("Kaç alt çizgi içersin?: "))

    # Toplam karakter sayısının kontrolü
    total_chars = uppercase_count + lowercase_count + punctuation_count + digit_count + underscore_count
    if total_chars > length:
        print("Hata: Toplam karakter sayısı şifre uzunluğundan büyük olamaz.")
        return

    password = ""

    # Büyük harfler
    for _ in range(uppercase_count):
        password += random.choice(string.ascii_uppercase)

    # Küçük harfler
    for _ in range(lowercase_count):
        password += random.choice(string.ascii_lowercase)

    # Noktalama işaretleri
    for _ in range(punctuation_count):
        password += random.choice(string.punctuation)

    # Sayılar
    for _ in range(digit_count):
        password += random.choice(string.digits)

    # Alt çizgiler
    for _ in range(underscore_count):
        password += "_"

    # Eksik karakterleri rastgele tamamlama
    while len(password) < length:
        category = random.choice(["uppercase", "lowercase", "punctuation", "digit", "underscore"])
        if category == "uppercase":
            password += random.choice(string.ascii_uppercase)
        elif category == "lowercase":
            password += random.choice(string.ascii_lowercase)
        elif category == "punctuation":
            password += random.choice(string.punctuation)
        elif category == "digit":
            password += random.choice(string.digits)
        elif category == "underscore":
            password += "_"

    # Karıştırma işlemi
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Şifreyi oluştur ve ekrana yazdır
generated_password = generate_password()
print("Oluşturulan Şifre:", generated_password)
