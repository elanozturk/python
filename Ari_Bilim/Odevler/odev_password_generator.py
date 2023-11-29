import random as r
import string as s

for i in range(1):
    password = ""
    for j in range(10):
        password += r.choice(s.ascii_letters + s.digits)
    print(password)