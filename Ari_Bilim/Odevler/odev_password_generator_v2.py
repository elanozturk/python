import random
import string

#create 8 character random password that contains 2 upper letters, 2 lower letters, 2 digits and 2 special characters
for p in range(1):
    password = ""
    for j in range(2):
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
    print(password)