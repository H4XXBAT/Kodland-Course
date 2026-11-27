import random

Caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Numero = int(input("inserisci il numero di caratteri che vuoi presenti nella Password (Solo numeri):   "))
Password = ""

for i in range(Numero):
    Password += random.choice(Caratteri)

print(f"La password generate è: {Password}")
