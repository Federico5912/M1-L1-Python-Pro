while True:
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "XD": "Es como reírse",
                "CREEPY": "Aterrador, siniestro",
                }
    
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Esa palabra no está aquí. Puedes buscar en otro lado")

    sino = input("Quieres buscar otra palabra?")
    if sino == "si":
        continue
    elif sino == "no":
        break
