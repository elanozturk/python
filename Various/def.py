def greet(lang):
    if lang == "es":
        print("Hola", end=' ')
    elif lang == "tr":
        print("Merhaba", end=' ')
    else:
        print("Hello", end=' ')

lang = input("Input language prefix: ")
greet(lang)
print("padawan!")
