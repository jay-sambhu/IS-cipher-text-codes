def xor_strings(a, b):
    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result


def round_function(right, key):
    return xor_strings(right, key)


def is_binary_string(value):
    return all(ch in "01" for ch in value)


def get_binary_input(prompt, expected_length=None):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty.")
            continue
        if not is_binary_string(value):
            print("Only 0 and 1 are allowed.")
            continue
        if expected_length is not None and len(value) != expected_length:
            print(f"Input must be exactly {expected_length} bits.")
            continue
        return value


def print_encryption_table(rows):
    print("\nEncryption Table:")
    print("+-------+------+---------+---------+---------+---------+---------+")
    print("| Round | Key  | L(in)   | R(in)   | F(R,K)  | L(out)  | R(out)  |")
    print("+-------+------+---------+---------+---------+---------+---------+")

    for row in rows:
        print(
            f"| {str(row['round']).rjust(5)} | "
            f"{row['key'].ljust(4)} | "
            f"{row['left_in'].ljust(7)} | "
            f"{row['right_in'].ljust(7)} | "
            f"{row['f_out'].ljust(7)} | "
            f"{row['left_out'].ljust(7)} | "
            f"{row['right_out'].ljust(7)} |"
        )

    print("+-------+------+---------+---------+---------+---------+---------+")


def print_decryption_table(rows):
    print("\nDecryption Table:")
    print("+-------+------+---------+---------+---------+---------+---------+")
    print("| Round | Key  | L(in)   | R(in)   | F(L,K)  | L(out)  | R(out)  |")
    print("+-------+------+---------+---------+---------+---------+---------+")

    for row in rows:
        print(
            f"| {str(row['round']).rjust(5)} | "
            f"{row['key'].ljust(4)} | "
            f"{row['left_in'].ljust(7)} | "
            f"{row['right_in'].ljust(7)} | "
            f"{row['f_out'].ljust(7)} | "
            f"{row['left_out'].ljust(7)} | "
            f"{row['right_out'].ljust(7)} |"
        )

    print("+-------+------+---------+---------+---------+---------+---------+")


def print_summary_table(plaintext, ciphertext, decrypted_text):
    print("\nSummary Table:")
    print("+----------------------+----------------------+----------------------+")
    print("| Plaintext            | Ciphertext           | Decrypted            |")
    print("+----------------------+----------------------+----------------------+")
    print(
        f"| {plaintext.ljust(20)} | "
        f"{ciphertext.ljust(20)} | "
        f"{decrypted_text.ljust(20)} |"
    )
    print("+----------------------+----------------------+----------------------+")


def feistel_encrypt(plaintext, keys):
    half = len(plaintext) // 2
    left = plaintext[:half]
    right = plaintext[half:]
    rows = []

    for round_no, key in enumerate(keys, start=1):
        left_in = left
        right_in = right
        f_out = round_function(right_in, key)

        left = right_in
        right = xor_strings(left_in, f_out)

        rows.append(
            {
                "round": round_no,
                "key": key,
                "left_in": left_in,
                "right_in": right_in,
                "f_out": f_out,
                "left_out": left,
                "right_out": right,
            }
        )

    return left + right, rows


def feistel_decrypt(ciphertext, keys):
    half = len(ciphertext) // 2
    left = ciphertext[:half]
    right = ciphertext[half:]
    rows = []

    for round_no, key in enumerate(reversed(keys), start=1):
        left_in = left
        right_in = right
        f_out = round_function(left_in, key)

        new_right = left
        new_left = xor_strings(right, f_out)
        left = new_left
        right = new_right
        rows.append(
            {
                "round": round_no,
                "key": key,
                "left_in": left_in,
                "right_in": right_in,
                "f_out": f_out,
                "left_out": left,
                "right_out": right,
            }
        )

    return left + right, rows


def main():
    print("=== Feistel Cipher (Binary) ===")

    plaintext = get_binary_input("Enter plaintext bits (even length): ")
    while len(plaintext) % 2 != 0:
        print("Plaintext length must be even.")
        plaintext = get_binary_input("Enter plaintext bits (even length): ")

    half = len(plaintext) // 2

    while True:
        rounds_input = input("Enter number of rounds: ").strip()
        if rounds_input.isdigit() and int(rounds_input) > 0:
            rounds = int(rounds_input)
            break
        print("Enter a positive integer.")

    keys = []
    print(f"Enter {rounds} round keys (each must be {half} bits):")
    for i in range(rounds):
        key = get_binary_input(f"Key {i + 1}: ", expected_length=half)
        keys.append(key)

    ciphertext, rows = feistel_encrypt(plaintext, keys)

    print("\nInitial State:")
    print(f"Left : {plaintext[:half]}")
    print(f"Right: {plaintext[half:]}")
    print_encryption_table(rows)

    print(f"\nCiphertext: {ciphertext}")

    choice = input("Do you want to decrypt it now? (yes/no): ").strip().lower()
    decrypted_text = "-"
    if choice in {"yes", "y"}:
        decrypted_text, decrypt_rows = feistel_decrypt(ciphertext, keys)
        print_decryption_table(decrypt_rows)
        print(f"Decrypted Text: {decrypted_text}")

    print_summary_table(plaintext, ciphertext, decrypted_text)


if __name__ == "__main__":
    main()