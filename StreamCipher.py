def generate_keystream(key, length):
    key = key.encode()
    keystream = (key * (length // len(key) + 1))[:length]
    return keystream


def encrypt_stream(plaintext, key):
    plaintext_bytes = plaintext.encode()
    keystream = generate_keystream(key, len(plaintext_bytes))

    cipher = []
    for i in range(len(plaintext_bytes)):
        cipher.append(plaintext_bytes[i] ^ keystream[i])

    return bytes(cipher)


def decrypt_stream(cipher, key):
    keystream = generate_keystream(key, len(cipher))

    plain = []
    for i in range(len(cipher)):
        plain.append(cipher[i] ^ keystream[i])

    return bytes(plain).decode()


def print_stream_table(title, input_bytes, key_bytes, output_bytes, input_label, output_label):
    print(f"\n{title}")
    print("+-----+------------+----------+------------+")
    print(f"| Pos | {input_label:^10} | {'Key':^8} | {output_label:^10} |")
    print("+-----+------------+----------+------------+")

    for index, (inp, key_b, outp) in enumerate(zip(input_bytes, key_bytes, output_bytes), start=1):
        print(f"| {str(index).rjust(3)} | {str(inp).rjust(10)} | {str(key_b).rjust(8)} | {str(outp).rjust(10)} |")

    print("+-----+------------+----------+------------+")


def print_styled_output(text, key, encrypted, decrypted):
    print("\n" + "=" * 46)
    print("            STREAM CIPHER OUTPUT")
    print("=" * 46)
    print(f"Input Text      : {text}")
    print(f"Key             : {key}")
    print(f"Encrypted Bytes : {encrypted}")
    print(f"Encrypted Hex   : {encrypted.hex()}")
    print(f"Decrypted Text  : {decrypted}")
    print("=" * 46)


# ---- MAIN ----
text = input("Enter text: ")
key = input("Enter key: ")

if not key:
    print("Key cannot be empty")
    exit()

encrypted = encrypt_stream(text, key)
plaintext_bytes = text.encode()
key_bytes_for_encrypt = generate_keystream(key, len(plaintext_bytes))
print_stream_table(
    "Encryption Table (XOR)",
    plaintext_bytes,
    key_bytes_for_encrypt,
    encrypted,
    "Plain",
    "Cipher",
)

decrypted = decrypt_stream(encrypted, key)
decrypted_bytes = decrypted.encode()
key_bytes_for_decrypt = generate_keystream(key, len(encrypted))
print_stream_table(
    "Decryption Table (XOR)",
    encrypted,
    key_bytes_for_decrypt,
    decrypted_bytes,
    "Cipher",
    "Plain",
)

print_styled_output(text, key, encrypted, decrypted)