meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione",
            "CREEPY": "spaventoso, inquietante",
            "PARA": "preoccuparsi per qualcosa, paranoiarsi",
            }
for i in range(5):
    parola = input("Hey boss non capisci il linguaggio moderno, scrivi la parola (usa solo lettere maiuscole!): ")
    
    if parola in meme_dict.keys():
        print(meme_dict[parola])
    else:
        # Cosa fare se la parola non è stata trovata?
        print("La parola inserita non è compresa nel dizionario, boomer...")