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


def transform_playfair_pair(matrix, a, b, mode):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        if mode == 'e':
            out_a = matrix[row1][(col1 + 1) % 5]
            out_b = matrix[row2][(col2 + 1) % 5]
        else:
            out_a = matrix[row1][(col1 - 1) % 5]
            out_b = matrix[row2][(col2 - 1) % 5]
        rule = "Same row"
    elif col1 == col2:
        if mode == 'e':
            out_a = matrix[(row1 + 1) % 5][col1]
            out_b = matrix[(row2 + 1) % 5][col2]
        else:
            out_a = matrix[(row1 - 1) % 5][col1]
            out_b = matrix[(row2 - 1) % 5][col2]
        rule = "Same column"
    else:
        out_a = matrix[row1][col2]
        out_b = matrix[row2][col1]
        rule = "Rectangle"

    return out_a, out_b, rule


def encrypt_playfair(plaintext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(plaintext, for_encrypt=True)
    ciphertext = ""

    for pair in pairs:
        a, b = pair[0], pair[1]
        out_a, out_b, _ = transform_playfair_pair(matrix, a, b, 'e')
        ciphertext += out_a + out_b

    return ciphertext


def decrypt_playfair(ciphertext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(ciphertext, for_encrypt=False)
    plaintext = ""

    for pair in pairs:
        a, b = pair[0], pair[1]
        out_a, out_b, _ = transform_playfair_pair(matrix, a, b, 'd')
        plaintext += out_a + out_b

    return plaintext


def encrypt_playfair_with_steps(plaintext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(plaintext, for_encrypt=True)
    ciphertext = ""
    steps = []

    for index, pair in enumerate(pairs, start=1):
        a, b = pair[0], pair[1]
        out_a, out_b, rule = transform_playfair_pair(matrix, a, b, 'e')
        out_pair = out_a + out_b
        ciphertext += out_pair
        steps.append((index, pair, rule, out_pair))

    return ciphertext, steps


def decrypt_playfair_with_steps(ciphertext, key):
    matrix = generate_key_matrix(key)
    pairs = prepare_text(ciphertext, for_encrypt=False)
    plaintext = ""
    steps = []

    for index, pair in enumerate(pairs, start=1):
        a, b = pair[0], pair[1]
        out_a, out_b, rule = transform_playfair_pair(matrix, a, b, 'd')
        out_pair = out_a + out_b
        plaintext += out_pair
        steps.append((index, pair, rule, out_pair))

    return plaintext, steps


def print_matrix(matrix):
    print("Key Matrix:")
    for row in matrix:
        print(" ".join(row))


def print_playfair_table(title, steps):
    print(f"\n{title}")
    print("+------+-------+-------------+--------+")
    print("| Pair | Input | Rule        | Output |")
    print("+------+-------+-------------+--------+")

    for pair_no, pair_in, rule, pair_out in steps:
        print(f"| {str(pair_no).rjust(4)} | {pair_in.center(5)} | {rule.ljust(11)} | {pair_out.center(6)} |")

    print("+------+-------+-------------+--------+")


def print_styled_output(mode, text, key, result):
    operation = "ENCRYPTION" if mode == 'e' else "DECRYPTION"
    print("\n" + "=" * 44)
    print(f"         PLAYFAIR CIPHER {operation}")
    print("=" * 44)
    print(f"Input  : {text}")
    print(f"Key    : {key}")
    print(f"Output : {result}")
    print("=" * 44)


# Example usage
key = input("Enter key: ")
text = input("Enter text: ")
choice = input("Type 'e' for encrypt or 'd' for decrypt: ").lower()

matrix = generate_key_matrix(key)
print_matrix(matrix)

if choice == 'e':
    result, steps = encrypt_playfair_with_steps(text, key)
    print_playfair_table("Encryption Table", steps)
    print_styled_output(choice, text.upper(), key.upper(), result)
elif choice == 'd':
    result, steps = decrypt_playfair_with_steps(text, key)
    print_playfair_table("Decryption Table", steps)
    print_styled_output(choice, text.upper(), key.upper(), result)
else:
    print("Invalid choice!")