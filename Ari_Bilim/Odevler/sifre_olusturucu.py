import random
import string

for i in range(1):
    password = ""
    for j in range(2):
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase) 
        password += random.choice(string.digits) 

password_as_list = list(password)
random.shuffle(password_as_list)
password = "-".join(password_as_list)

print("Şifreniz:", password)
