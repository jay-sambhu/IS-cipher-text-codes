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


def print_vigenere_steps_table(input_text, expanded_key, output_text, mode):
    operation = "Encrypt" if mode == 'e' else "Decrypt"
    print(f"\n{operation}ion table:")
    print("+-----+-------+-----+--------+")
    print("| Pos | Input | Key | Output |")
    print("+-----+-------+-----+--------+")

    for index, (inp, key_char, outp) in enumerate(zip(input_text, expanded_key, output_text), start=1):
        print(f"| {str(index).rjust(3)} | {inp.center(5)} | {key_char.center(3)} | {outp.center(6)} |")

    print("+-----+-------+-----+--------+")


text = input("Enter text: ")
key = input("Enter key: ")
choice = input("Enter e for encryption or d for decryption: ").lower()

if not key.strip():
    print("Key cannot be empty")
    exit()

if choice == 'e':
    result = encrypt_vigenere(text, key)
    expanded_key = generate_key(text.upper(), key)
    print_vigenere_steps_table(text.upper(), expanded_key, result, choice)
    print("Encrypted text:", result)
elif choice == 'd':
    result = decrypt_vigenere(text, key)
    expanded_key = generate_key(text.upper(), key)
    print_vigenere_steps_table(text.upper(), expanded_key, result, choice)
    print("Decrypted text:", result)
else:
    print("Invalid choice")