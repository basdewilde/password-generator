import random
import string

length = 12  # change password length here|| made by chatgpt

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", password)
