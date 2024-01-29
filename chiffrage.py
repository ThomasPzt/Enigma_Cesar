def caesar_cipher(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            index = (ord(char_lower) - ord('a') + key) % 26
            encrypted_char = alphabet[index]
            result += encrypted_char.upper() if is_upper else encrypted_char
        else:
            result += char
    return result

def encrypt_decrypt_file(file_path, key, encrypt=True):
    with open(file_path, 'r') as file:
        content = file.read()

    # Convertir le texte en minuscules tout en conservant la ponctuation
    content_lower = ''.join([char.lower() if char.isalpha() else char for char in content])

    # Ajuster la clé en fonction de l'option choisie (chiffrer ou déchiffrer)
    key = key if encrypt else -key

    # Appliquer le chiffrement César avec la clé spécifiée
    encrypted_text = caesar_cipher(content_lower, key)

    # Écrire le texte chiffré/déchiffré dans un nouveau fichier
    operation = 'Chiffré' if encrypt else 'Déchiffré'
    output_file_path = f'{operation}_output.txt'
    with open(output_file_path, 'w') as output_file:
        output_file.write(encrypted_text)

    print(f"Texte {operation.lower()} avec la clé {key}. Résultat enregistré dans {output_file_path}.")

# Demander à l'utilisateur la clé de chiffrement et le chemin du fichier
key = int(input("Entrez la clé de chiffrement (positive ou négative): "))
file_path = input("Entrez le chemin du fichier : ")
operation_choice = input("Voulez-vous chiffrer (c) ou déchiffrer (d) le texte? ").lower()

# Décider si l'utilisateur veut chiffrer ou déchiffrer et appeler la fonction appropriée
if operation_choice == 'c':
    encrypt_decrypt_file(file_path, key, encrypt=True)
elif operation_choice == 'd':
    encrypt_decrypt_file(file_path, key, encrypt=False)
else:
    print("Option invalide. Veuillez choisir 'c' pour chiffrer ou 'd' pour déchiffrer.")
