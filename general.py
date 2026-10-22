import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols

length = int(input("Введите длину пароля (например, 12): "))

password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Ваш сгенерированный пароль:", password)
