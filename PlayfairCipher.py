def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix_list = []

    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix_list.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is excluded
        if char not in seen:
            seen.add(char)
            matrix_list.append(char)

    matrix = [matrix_list[i:i+5] for i in range(0, 25, 5)]
    return matrix


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def prepare_text(text, for_encrypt=True):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = ""

        if i + 1 < len(text):
            b = text[i + 1]

        if for_encrypt:
            if a == b:
                pairs.append(a + "X")
                i += 1
            elif b:
                pairs.append(a + b)
                i += 2
            else:
                pairs.append(a + "X")
                i += 1
        else:
            if b:
                pairs.append(a + b)
                i += 2
            else:
                pairs.append(a + "X")
                i += 1

    return pairs


def encrypt_playfair(plaintext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(plaintext, for_encrypt=True)
    ciphertext = ""

    for pair in pairs:
        a, b = pair[0], pair[1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext


def decrypt_playfair(ciphertext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(ciphertext, for_encrypt=False)
    plaintext = ""

    for pair in pairs:
        a, b = pair[0], pair[1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


def print_matrix(matrix):
    print("Key Matrix:")
    for row in matrix:
        print(" ".join(row))


# Example usage
key = input("Enter key: ")
text = input("Enter text: ")
choice = input("Type 'e' for encrypt or 'd' for decrypt: ").lower()

matrix = generate_key_matrix(key)
print_matrix(matrix)

if choice == 'e':
    result = encrypt_playfair(text, key)
    print("Encrypted Text:", result)
elif choice == 'd':
    result = decrypt_playfair(text, key)
    print("Decrypted Text:", result)
else:
    print("Invalid choice!")