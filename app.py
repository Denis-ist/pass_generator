from random import choice

numbers = '1234567890'
chars = '+-/*!&$#?=@<>_'
letters = 'abcdefghijklnopqrstuvwxyz'
password_chars = numbers + chars + letters + letters.upper()
count = int(input('количество паролей?' + "\n"))
length = int(input('длина пароля?' + "\n"))

for n in range(count):
    password = ''
    for i in range(length):
        password += choice(password_chars)
    print(password)
