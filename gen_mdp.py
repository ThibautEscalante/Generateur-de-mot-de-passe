# Ce script demande à l'utilisateur la longueur du mot de passe désiré et s'il souhaite autoriser les caractères spéciaux. 
# Ensuite, il génère un mot de passe en utilisant des caractères alphabétiques, des chiffres et éventuellement des caractères 
# spéciaux, en fonction du paramètre allow_special_chars.
import random
import string

def generate_password(length, allow_special_chars=False):
    # Définir les caractères autorisés
    chars = string.ascii_letters + string.digits
    if allow_special_chars:
        chars += string.punctuation

    # Générer le mot de passe
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Longueur du mot de passe : "))
    allow_special_chars = input("Autoriser les caractères spéciaux (O/N) ? ").upper() == "O"

    password = generate_password(length, allow_special_chars)
    print("Mot de passe généré :", password)