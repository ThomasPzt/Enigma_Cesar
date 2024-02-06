# README Projet Enigma_Cesar
# 

## Chiffrement César et Enigma César

Ce programme Python propose des fonctionnalités de chiffrement et de déchiffrement utilisant les méthodes de César et d'Enigma César. L'utilisateur peut choisir parmi plusieurs modes d'opération, notamment :

1. **Chiffrement/Déchiffrement de César :**
   - L'utilisateur peut entrer une clé positive ou négative.
   - Il peut choisir d'encrypter/décrypter des entrées dans la console ou des fichiers textes fournis par l'utilisateur.

2. **Chiffrement/Déchiffrement d'Enigma César :**
   - L'utilisateur peut entrer trois clés (positives ou négatives) pour le chiffrement Enigma César.
   - Il peut choisir d'encrypter/décrypter des entrées dans la console ou des fichiers textes fournis par l'utilisateur.

3. **Brute-force d'un fichier chiffré :**
   - L'utilisateur peut appliquer un brute-force sur un fichier texte chiffré pour trouver la clé correspondante.
   - Le programme teste toutes les combinaisons possibles de clés pour les méthodes de chiffrement de César et d'Enigma César.

## Constantes de Justesse

Le programme utilise des constantes de justesse pour évaluer la vraisemblance des résultats lors de l'opération brute-force. Ces constantes représentent le pourcentage d'apparition des lettres en fonction des langues française et anglaise.

```python
justesseLettresFrancais = [0.0812, 0.009, 0.0334, 0.0367, 0.1713, 0.0107, 0.0087, 0.0074, 0.0758, 0.0054, 0.0005,
                           0.0545, 0.0297, 0.0709, 0.0541, 0.0302, 0.0136, 0.0655, 0.0795, 0.0724, 0.0637, 0.0163,
                           0.0011, 0.0039, 0.0031, 0.0014]

justesseLettresAnglais = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, 0.0527, 0.0724, 0.0014, 0.0063,
                          0.0404, 0.026, 0.0738, 0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0219, 0.01, 0.0189,
                          0.0021, 0.0165, 0.0007]
````

## Fonctions de Brute Force
Le programme propose des fonctions de brute-force pour déterminer la clé de chiffrement optimale. Il teste différentes combinaisons de clés et utilise les constantes de justesse pour évaluer la pertinence des résultats.

## Fonctions de Chiffrement César Simple
Les fonctions de chiffrement César simple permettent de chiffrer et déchiffrer des messages en utilisant une clé spécifiée.

## Fonctions de Chiffrement Enigma César
Les fonctions de chiffrement Enigma César permettent de chiffrer et déchiffrer des messages en utilisant trois clés spécifiées. Ces clés varient pour chaque lettre du message.

## Utilisation du Programme
L'utilisateur peut exécuter le programme en choisissant un mode d'opération parmi les options disponibles. Le programme demande ensuite les informations nécessaires à l'utilisateur, telles que la clé, le chemin du fichier, etc. Il fournit des messages d'erreur pertinents en cas de saisie incorrecte.

Pour le mode brute-force, l'utilisateur peut choisir entre la méthode brute-force César (clé unique) ou la méthode brute-force Enigma César (clé triple). Le programme teste toutes les combinaisons possibles jusqu'à trouver le message décrypté et la clé correspondante.

*Note : Les fichiers résultants (chiffrés ou déchiffrés) sont enregistrés dans des fichiers distincts, et le programme affiche le chemin du fichier résultant.*

# Auteurs
- Thomas Poizot
- Esteban Brion