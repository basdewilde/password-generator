import random
import string

length = input("Uit hoeveel tekens moet je wachtwoord bestaan: ")  # change password length here|| made by chatgpt

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(int(length)))

print("Generated password:", password)
