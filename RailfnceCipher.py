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


# ---- MAIN ----
text = input("Enter text: ")
rails = int(input("Enter number of rails: "))
choice = input("Enter e for encrypt or d for decrypt: ").lower()

if choice == 'e':
    print("Encrypted:", encrypt_rail_fence(text, rails))
elif choice == 'd':
    print("Decrypted:", decrypt_rail_fence(text, rails))
else:
    print("Invalid choice")