import random

s = random.randint(1, 20)

for i in range(5):
    n = int(input("Inserisci un numero"))
    if n == s:
        print("Hai vinto")
        break
    elif n <= s:
        print("Il numero è più grande di quello indicato")
    elif n >= s:
        print("Il numero è più piccolo di quello indicato")