def brute_force(message_chiffre, justesseLettresFrancais, justesseLettresAnglais):
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
        meilleur_decalage = meilleur_decalage_francais
    else:
        meilleur_decalage = meilleur_decalage_anglais

    return meilleur_decalage
