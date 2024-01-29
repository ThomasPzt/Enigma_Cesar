from unidecode import unidecode

def caesar_cipher(text, key_1, key_2, key_3, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for i, char in enumerate(text):
        if char.isalpha():
            key = (key_1, key_2, key_3)[i % 3] * (-1 if not encrypt else 1)
            char_lower = char.lower()
            encrypted_char = alphabet[(ord(char_lower) - ord('a') + key) % 26]
            print(key)
            result += encrypted_char
        else:
            result += char
    return result

def encrypt_decrypt_file(file_path, key_1,key_2,key_3, encrypt=True):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Convertir le texte en minuscules tout en conservant la ponctuation et gérer les accents
    content_normalized = unidecode(''.join([char.lower() if char.isalpha() else char for char in content]))

    # Appliquer le chiffrement César avec les clés spécifiées
    result_type = 'Chiffré' if encrypt else 'Déchiffré'
    encrypted_text = caesar_cipher(content_normalized, key_1,key_2,key_3, encrypt)

    # Écrire le texte chiffré/déchiffré dans un nouveau fichier
    output_file_path = f'{result_type.lower()}_output.txt'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(encrypted_text)

    print(f"Texte {result_type.lower()} avec les clés {key_1,key_2,key_3}. Résultat enregistré dans {output_file_path}.")

# Demander à l'utilisateur les trois clés de chiffrement et le chemin du fichier
key_1 = int(input("Entrez la clef de chiffrement 1 : "))
key_2 = int(input("Entrez la clef de chiffrement 2 : "))
key_3 = int(input("Entrez la clef de chiffrement 3 : "))

file_path = input("Entrez le chemin du fichier : ")
operation_choice = input("Voulez-vous crypter (c) ou décrypter (d) le texte? ").lower()

# Décider si l'utilisateur veut crypter ou décrypter et appeler la fonction appropriée
if operation_choice == 'c':
    encrypt_decrypt_file(file_path, key_1, key_2, key_3, encrypt=True)
elif operation_choice == 'd':
    encrypt_decrypt_file(file_path, key_1, key_2, key_3, encrypt=False)
else:
    print("Option invalide. Veuillez choisir 'c' pour crypter ou 'd' pour décrypter.")
