from datetime import date
birthdate = int(input("Hangi yılda doğdunuz?"))
def age(birthdate):
    today = date.today()
    return today.year - birthdate
print("Yaşınız", age(birthdate))
print("merhaba")
2356

