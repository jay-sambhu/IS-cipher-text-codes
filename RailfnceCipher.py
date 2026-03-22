def encrypt_rail_fence(text, rails):
    rail = [['\n' for _ in range(len(text))] for _ in range(rails)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        row += 1 if direction_down else -1

    result = ""
    for i in range(rails):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def decrypt_rail_fence(cipher, rails):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(rails)]

    direction_down = None
    row, col = 0, 0

    # Mark the zig-zag pattern
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    # Fill the matrix
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read in zig-zag
    result = ""
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        result += rail[row][col]
        col += 1
        row += 1 if direction_down else -1

    return result


def get_rail_path(length, rails):
    row = 0
    direction_down = True
    path = []

    for _ in range(length):
        path.append(row)
        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False
        row += 1 if direction_down else -1

    return path


def print_rail_table(title, input_text, output_text, path, input_label, output_label):
    print(f"\n{title}")
    print("+-----+-------+------+--------+")
    print(f"| Pos | {input_label:^5} | Rail | {output_label:^6} |")
    print("+-----+-------+------+--------+")

    for index, (inp, outp, rail_row) in enumerate(zip(input_text, output_text, path), start=1):
        print(f"| {str(index).rjust(3)} | {inp.center(5)} | {str(rail_row + 1).rjust(4)} | {outp.center(6)} |")

    print("+-----+-------+------+--------+")


def print_styled_output(mode, text, rails, result):
    operation = "ENCRYPTION" if mode == 'e' else "DECRYPTION"
    print("\n" + "=" * 44)
    print(f"       RAIL FENCE CIPHER {operation}")
    print("=" * 44)
    print(f"Input  : {text}")
    print(f"Rails  : {rails}")
    print(f"Output : {result}")
    print("=" * 44)


# ---- MAIN ----
text = input("Enter text: ")
rails = int(input("Enter number of rails: "))
choice = input("Enter e for encrypt or d for decrypt: ").lower()

if rails < 2:
    print("Number of rails must be at least 2")
    exit()

if choice == 'e':
    result = encrypt_rail_fence(text, rails)
    path = get_rail_path(len(text), rails)
    print_rail_table("Encryption Table", text, result, path, "Input", "Output")
    print_styled_output(choice, text, rails, result)
elif choice == 'd':
    result = decrypt_rail_fence(text, rails)
    path = get_rail_path(len(text), rails)
    print_rail_table("Decryption Table", text, result, path, "Cipher", "Plain")
    print_styled_output(choice, text, rails, result)
else:
    print("Invalid choice")