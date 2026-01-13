import random
signs = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Wprowadź długość hasła: "))
password = ""
for i in range(length):
    password += random.choice(signs)
print("Wygenerowane hasło:", password)