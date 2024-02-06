from unidecode import unidecode

# constante de justesse, % d'apparition des lettres en focntion des langues
justesseLettresFrancais = [0.0812, 0.009, 0.0334, 0.0367, 0.1713, 0.0107, 0.0087, 0.0074, 0.0758, 0.0054, 0.0005,
                           0.0545, 0.0297, 0.0709, 0.0541, 0.0302, 0.0136, 0.0655, 0.0795, 0.0724, 0.0637, 0.0163,
                           0.0011, 0.0039, 0.0031, 0.0014]

justesseLettresAnglais = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, 0.0527, 0.0724, 0.0014, 0.0063,
                          0.0404, 0.026, 0.0738, 0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0219, 0.01, 0.0189,
                          0.0021, 0.0165, 0.0007]


## FONCTIONS DE BRUTE FORCE
def justesse(phrase, justesseLettres, decalage):
    somme_justesse = 0
    for lettre in phrase:
        if lettre == ' ' or not lettre.isalpha():
            continue  # Ignorer les espaces et la ponctuation
        indice_lettre = ord(lettre) - ord('a')
        somme_justesse += justesseLettres[(indice_lettre - decalage) % 26]
    return somme_justesse


def diviser_avec_roulement(chaine):
    chaine1 = ""
    chaine2 = ""
    chaine3 = ""

    for i in range(len(chaine)):
        if i % 3 == 0:
            chaine1 += chaine[i]
        elif i % 3 == 1:
            chaine2 += chaine[i]
        else:
            chaine3 += chaine[i]

    return chaine1, chaine2, chaine3


def brute_force(message_chiffre, justesseLettresFrancais, justesseLettresAnglais):
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


## FONCTIONS DE CESAR SIMPLE
def chiffrement_cesar(texte, cle):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    resultat = ''
    for char in texte:
        if char.isalpha():
            index = (ord(char) - ord('a') + cle) % 26
            char_chiffre = alphabet[index]
            resultat += char_chiffre
        else:
            resultat += char
    return resultat


def chiffrement_dechiffrement_fichier(chemin_fichier, cle, chiffrement=True):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    # Convertir le texte en minuscules tout en conservant la ponctuation et gérer les accents
    contenu_normalise = unidecode(''.join([char.lower() if char.isalpha() else char for char in contenu]))

    # Ajuster la clé en fonction de l'option choisie (chiffrer ou déchiffrer)
    cle = cle if chiffrement else -cle

    # Appliquer le chiffrement César avec la clé spécifiée
    texte_chiffre = chiffrement_cesar(contenu_normalise, cle)

    # Écrire le texte chiffré/déchiffré dans un nouveau fichier
    operation = 'Chiffré' if chiffrement else 'Déchiffré'
    chemin_fichier_sortie = f'{operation}_output.txt'
    with open(chemin_fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
        fichier_sortie.write(texte_chiffre)

    print(f"Texte {operation.lower()} avec la clé {cle}. Résultat enregistré dans {chemin_fichier_sortie}.")


## FONCTIONS DE CESAR-ENIGMA
def enigma_chiffrement_cesar(texte, cle_1, cle_2, cle_3, chiffrement=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    resultat = ''

    for i, char in enumerate(texte):
        if char.isalpha():
            cle = (cle_1, cle_2, cle_3)[i % 3] * (-1 if not chiffrement else 1)
            char_minuscule = char.lower()
            char_chiffre = alphabet[(ord(char_minuscule) - ord('a') + cle) % 26]
            resultat += char_chiffre
        else:
            resultat += char
    return resultat


def enigma_chiffrement_dechiffrement_fichier(chemin_fichier, cle_1, cle_2, cle_3, chiffrement=True):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    # Convertir le texte en minuscules tout en conservant la ponctuation et gérer les accents
    contenu_normalise = unidecode(''.join([char.lower() if char.isalpha() else char for char in contenu]))

    # Appliquer le chiffrement César avec les clés spécifiées
    resultat_type = 'Chiffré' if chiffrement else 'Déchiffré'
    texte_chiffre = enigma_chiffrement_cesar(contenu_normalise, cle_1, cle_2, cle_3, chiffrement)

    # Écrire le texte chiffré/déchiffré dans un nouveau fichier
    chemin_fichier_sortie = f'{resultat_type.lower()}_output.txt'
    with open(chemin_fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
        fichier_sortie.write(texte_chiffre)

    print(
        f"Texte {resultat_type.lower()} avec les clés {cle_1, cle_2, cle_3}. Résultat enregistré dans {chemin_fichier_sortie}.")


## MAIN CODE ET INTERACTION UTILISATEUR
def main():
    print("Choisissez un mode :")
    print("1. Chiffrement/Déchiffrement de César")
    print("2. Chiffrement/Déchiffrement d'Enigma César")
    print("3. Brute-force d'un fichier chiffré")

    choix_mode = int(input("Entrez le numéro du mode choisi : "))

    if choix_mode == 1:
        # Demander à l'utilisateur la clé de chiffrement et le chemin du fichier
        key = int(input("Entrez la clé de chiffrement (positive ou négative): "))
        file_path = input("Entrez le chemin du fichier : ")
        operation_choice = input("Voulez-vous chiffrer (c) ou déchiffrer (d) le texte? ").lower()

        # Décider si l'utilisateur veut chiffrer ou déchiffrer et appeler la fonction appropriée
        if operation_choice == 'c':
            chiffrement_dechiffrement_fichier(file_path, key, chiffrement=True)
        elif operation_choice == 'd':
            chiffrement_dechiffrement_fichier(file_path, key, chiffrement=False)
        else:
            print("Option invalide. Veuillez choisir 'c' pour chiffrer ou 'd' pour déchiffrer.")

    elif choix_mode == 2:
        # Demander à l'utilisateur les trois clés de chiffrement et le chemin du fichier
        key_1 = int(input("Entrez la clé de chiffrement 1 : "))
        key_2 = int(input("Entrez la clé de chiffrement 2 : "))
        key_3 = int(input("Entrez la clé de chiffrement 3 : "))

        file_path = input("Entrez le chemin du fichier : ")
        operation_choice = input("Voulez-vous crypter (c) ou décrypter (d) le texte? ").lower()

        # Décider si l'utilisateur veut crypter ou décrypter et appeler la fonction appropriée
        if operation_choice == 'c':
            enigma_chiffrement_dechiffrement_fichier(file_path, key_1, key_2, key_3, chiffrement=True)
        elif operation_choice == 'd':
            enigma_chiffrement_dechiffrement_fichier(file_path, key_1, key_2, key_3, chiffrement=False)
        else:
            print("Option invalide. Veuillez choisir 'c' pour crypter ou 'd' pour décrypter.")
    elif choix_mode == 3:
        print("Choisissez un mode :")
        print("1. Brute-Force César (clé unique)")
        print("2. Brute-Force d'Enigma César (clé triple)")

        brute_mode = int(input("Entrez le numéro du mode choisi : "))

        if brute_mode == 1:
            chemin_fichier = input("Entrez le chemin du fichier : ")
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

            # Convertir le texte en minuscules tout en conservant la ponctuation et gérer les accents
            message_chiffre = unidecode(''.join([char.lower() if char.isalpha() else char for char in contenu]))

            cle = brute_force(message_chiffre, justesseLettresFrancais,
                              justesseLettresAnglais)
            print(f"La meilleure clé est : {cle}")
            chiffrement_dechiffrement_fichier(chemin_fichier, cle, chiffrement=False)

        if brute_mode == 2:
            chemin_fichier = input("Entrez le chemin du fichier : ")
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

            # Convertir le texte en minuscules tout en conservant la ponctuation et gérer les accents
            message_chiffre = unidecode(''.join([char.lower() if char.isalpha() else char for char in contenu]))

            chaine1, chaine2, chaine3 = diviser_avec_roulement(message_chiffre)
            cle1 = brute_force(chaine1,
                               justesseLettresFrancais,
                               justesseLettresAnglais)
            cle2 = brute_force(chaine2,
                               justesseLettresFrancais,
                               justesseLettresAnglais)
            cle3 = brute_force(chaine3,
                               justesseLettresFrancais,
                               justesseLettresAnglais)
            print(f"La meilleure combinaison de clés est : {cle1},{cle2},{cle3}")
            enigma_chiffrement_dechiffrement_fichier(chemin_fichier, cle1, cle2, cle3, chiffrement=False)
    else:
        print("Mode non valide.")


if __name__ == "__main__":
    main()
