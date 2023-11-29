import random
import string
import hashlib

allowed_punctuation = ['?', '!', '_']

for p in range(1):
    password = ""
    for j in range(2):
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.digits)
        #password += random.choice(string.punctuation) 
        password += random.choice(allowed_punctuation) #sadece ? ! _ kullanılacak, aksi halde bu satırı ve 5. satırı comment yapın, 13. satırı uncomment yapın.
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    print("Şifreniz:", password)
    md5 = hashlib.md5(password.encode()).hexdigest()
    print("MD5 hali:", md5)
    sha1 = hashlib.sha1(password.encode()).hexdigest()
    print("SHA1 hali:", sha1)
    sha256 = hashlib.sha256(password.encode()).hexdigest()
    print("SHA256 hali:", sha256)
    sha512 = hashlib.sha512(password.encode()).hexdigest()
    print("SHA512 hali:", sha512)

    
    