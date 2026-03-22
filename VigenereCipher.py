def generate_key(text, key):
    key = key.upper()
    text = text.upper()
    new_key = ""
    j = 0

    for char in text:
        if char.isalpha():
            new_key += key[j % len(key)]
            j += 1
        else:
            new_key += char

    return new_key


def encrypt_vigenere(text, key):
    text = text.upper()
    key = generate_key(text, key)
    cipher_text = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
            cipher_text += chr(x + ord('A'))
        else:
            cipher_text += text[i]

    return cipher_text


def decrypt_vigenere(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = generate_key(cipher_text, key)
    plain_text = ""

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            x = (ord(cipher_text[i]) - ord('A') - (ord(key[i]) - ord('A')) + 26) % 26
            plain_text += chr(x + ord('A'))
        else:
            plain_text += cipher_text[i]

    return plain_text


text = input("Enter text: ")
key = input("Enter key: ")
choice = input("Enter e for encryption or d for decryption: ").lower()

if choice == 'e':
    result = encrypt_vigenere(text, key)
    print("Encrypted text:", result)
elif choice == 'd':
    result = decrypt_vigenere(text, key)
    print("Decrypted text:", result)
else:
    print("Invalid choice")