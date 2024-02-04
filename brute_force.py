def decrypter_message_chiffre(message_chiffre, justesseLettresFrancais, justesseLettresAnglais):
    def justesse(phrase, justesseLettres, decalage):
        somme_justesse = 0
        for lettre in phrase:
            if lettre == ' ' or not lettre.isalpha():
                continue  # Ignorer les espaces et la ponctuation
            indice_lettre = ord(lettre) - ord('a')
            somme_justesse += justesseLettres[(indice_lettre - decalage) % 26]
        return somme_justesse

    meilleur_decalage_francais = 0
    meilleure_justesse_francais = 0

    meilleur_decalage_anglais = 0
    meilleure_justesse_anglais = 0

    for decalage in range(26):
        justesse_actuelle_francais = justesse(message_chiffre, justesseLettresFrancais, decalage)
        if justesse_actuelle_francais > meilleure_justesse_francais:
            meilleure_justesse_francais = justesse_actuelle_francais
            meilleur_decalage_francais = decalage

        justesse_actuelle_anglais = justesse(message_chiffre, justesseLettresAnglais, decalage)
        if justesse_actuelle_anglais > meilleure_justesse_anglais:
            meilleure_justesse_anglais = justesse_actuelle_anglais
            meilleur_decalage_anglais = decalage

    if meilleure_justesse_francais > meilleure_justesse_anglais:
        meilleure_langue = "francais"
        meilleur_decalage = meilleur_decalage_francais
    else:
        meilleure_langue = "anglais"
        meilleur_decalage = meilleur_decalage_anglais

    phrase_decryptee = ''
    for lettre in message_chiffre:
        if lettre == ' ' or not lettre.isalpha():
            phrase_decryptee += lettre
        else:
            indice_lettre = ord(lettre) - ord('a')
            if meilleure_langue == "francais":
                lettre_decryptee = chr((indice_lettre - meilleur_decalage_francais) % 26 + ord('a'))
            else:
                lettre_decryptee = chr((indice_lettre - meilleur_decalage_anglais) % 26 + ord('a'))
            phrase_decryptee += lettre_decryptee

    return meilleur_decalage, meilleure_langue, phrase_decryptee


justesseLettresFrancais = [0.0812, 0.009, 0.0334, 0.0367, 0.1713, 0.0107, 0.0087, 0.0074, 0.0758, 0.0054, 0.0005,
                           0.0545, 0.0297, 0.0709, 0.0541, 0.0302, 0.0136, 0.0655, 0.0795, 0.0724, 0.0637, 0.0163,
                           0.0011, 0.0039, 0.0031, 0.0014]

justesseLettresAnglais = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, 0.0527, 0.0724, 0.0014, 0.0063,
                          0.0404, 0.026, 0.0738, 0.0747,0.0191,0.0009,0.0642,0.0659,0.0915,0.0219,0.01,0.0189,
                          0.0021,0.0165,0.0007]

# Exemple d'utilisation
message_chiffre = input("Entrez le message chiffré en minuscules : ")
meilleur_decalage, meilleure_langue, message_decrypte = decrypter_message_chiffre(message_chiffre,
                                                                                  justesseLettresFrancais,
                                                                                  justesseLettresAnglais)

print(f"Le meilleur décalage est : {meilleur_decalage}")
print(f"Langue détectée : {meilleure_langue}")
print(f"Message décodé : {message_decrypte}")