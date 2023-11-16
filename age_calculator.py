from datetime import date
birthdate = int(input("Hangi yilda doğdunuz?"))
def age(birthdate):
    today = date.today()
    return today.year - birthdate
print("Yasiniz", age(birthdate)) #explain this line


