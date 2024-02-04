from time import perf_counter


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


def combiner_avec_roulement(chaine1, chaine2, chaine3):
    taille_max = max(len(chaine1), len(chaine2), len(chaine3))
    resultat = ""

    for i in range(taille_max):
        if i < len(chaine1):
            resultat += chaine1[i]
        if i < len(chaine2):
            resultat += chaine2[i]
        if i < len(chaine3):
            resultat += chaine3[i]

    return resultat


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


justesseLettresFrancais = [0.0812, 0.009, 0.0334, 0.0367, 0.1713, 0.0107, 0.0087, 0.0074, 0.0758, 0.0054, 0.0005,
                           0.0545, 0.0297, 0.0709, 0.0541, 0.0302, 0.0136, 0.0655, 0.0795, 0.0724, 0.0637, 0.0163,
                           0.0011, 0.0039, 0.0031, 0.0014]

justesseLettresAnglais = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, 0.0527, 0.0724, 0.0014, 0.0063,
                          0.0404, 0.026, 0.0738, 0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0219, 0.01, 0.0189,
                          0.0021, 0.0165, 0.0007]

# Exemple d'utilisation
message_chiffre = input("Entrez le message chiffré en minuscules : ")
tic = perf_counter()
chaine1, chaine2, chaine3 = diviser_avec_roulement(message_chiffre)
meilleur_cle1 = brute_force(chaine1,
                                                                                justesseLettresFrancais,
                                                                                justesseLettresAnglais)
meilleur_cle2 = brute_force(chaine2,
                                                                                justesseLettresFrancais,
                                                                                justesseLettresAnglais)
meilleur_cle3 = brute_force(chaine3,
                                                                                justesseLettresFrancais,
                                                                                justesseLettresAnglais)


print(f"La meilleure combinaison de clés trouvée est : [{meilleur_cle1}, {meilleur_cle2} , {meilleur_cle3}]")
tac = perf_counter()
print(tac - tic)
# focntionne pour des chaines de caractères sans paragraphes, sinon problème d'affichage

# paragraphes = message_decrypte.split('\n')

# for paragraphe in paragraphes:
#    print(paragraphe)
