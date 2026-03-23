# ============================================
# DES-Style Feistel Cipher with:
# - Real DES Initial Permutation (IP)
# - Real DES Final Permutation (FP / IP^-1)
# - Step-by-step round output
# - Encryption + Decryption
# Educational purpose only
# ============================================

# Real DES Initial Permutation Table (64-bit)
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Real DES Final Permutation Table (Inverse IP)
FP_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]


def permute(bits, table):
    """Rearrange bits according to the permutation table."""
    return ''.join(bits[i - 1] for i in table)


def xor_bits(a, b):
    """XOR two equal-length bit strings."""
    return ''.join('0' if a[i] == b[i] else '1' for i in range(len(a)))


def left_rotate(bits, n):
    """Rotate bits to the left by n."""
    n %= len(bits)
    return bits[n:] + bits[:n]


def round_function(right, round_key):
    """
    Simplified Feistel round function.
    DES normally uses expansion, S-boxes, and permutation.
    For learning, we use:
        F(R, K) = R XOR K
    Both right and round_key must be 32 bits.
    """
    return xor_bits(right, round_key)


def generate_round_keys(key_64bit, rounds=16):
    """
    Generate 16 simple 32-bit round keys from a 64-bit master key.
    This is NOT the real DES key schedule.
    It is only for educational Feistel demonstration.
    """
    keys = []
    current = key_64bit

    for i in range(rounds):
        current = left_rotate(current, i + 1)
        round_key = current[:32]
        keys.append(round_key)

    return keys


def print_block(label, bits, group=8):
    """Pretty print bit blocks."""
    grouped = ' '.join(bits[i:i+group] for i in range(0, len(bits), group))
    print(f"{label}: {grouped}")


def print_round_diagram(round_no, left_before, right_before, round_key, f_output, left_after, right_after):
    print(f"\n--- Round {round_no} ---")
    print(f"Input:")
    print(f"   L{round_no-1} = {left_before}")
    print(f"   R{round_no-1} = {right_before}")
    print(f"   K{round_no}   = {round_key}")
    print()
    print("   Feistel Structure:")
    print(f"      L{round_no} = R{round_no-1}")
    print(f"      R{round_no} = L{round_no-1} XOR F(R{round_no-1}, K{round_no})")
    print()
    print(f"   F(R{round_no-1}, K{round_no}) = {f_output}")
    print()
    print(f"Output:")
    print(f"   L{round_no} = {left_after}")
    print(f"   R{round_no} = {right_after}")


def feistel_encrypt(plaintext_64bit, key_64bit, rounds=16):
    print("\n" + "=" * 70)
    print("ENCRYPTION")
    print("=" * 70)

    print_block("Original Plaintext", plaintext_64bit)

    # Step 1: Initial Permutation
    ip_output = permute(plaintext_64bit, IP_TABLE)
    print_block("After Initial Permutation (IP)", ip_output)

    # Split into left and right halves
    left = ip_output[:32]
    right = ip_output[32:]

    print(f"\nSplit after IP:")
    print(f"L0 = {left}")
    print(f"R0 = {right}")

    # Generate round keys
    round_keys = generate_round_keys(key_64bit, rounds)

    # Feistel rounds
    for i in range(rounds):
        left_before = left
        right_before = right

        f_output = round_function(right_before, round_keys[i])
        left = right_before
        right = xor_bits(left_before, f_output)

        print_round_diagram(
            i + 1,
            left_before,
            right_before,
            round_keys[i],
            f_output,
            left,
            right
        )

    # Final swap
    combined = right + left
    print("\nAfter final swap (R16 + L16):")
    print_block("Preoutput Block", combined, group=8)

    # Final permutation
    ciphertext = permute(combined, FP_TABLE)
    print_block("Ciphertext after Final Permutation (FP)", ciphertext)

    return ciphertext, round_keys


def feistel_decrypt(ciphertext_64bit, round_keys, rounds=16):
    print("\n" + "=" * 70)
    print("DECRYPTION")
    print("=" * 70)

    print_block("Ciphertext Input", ciphertext_64bit)

    # Step 1: Initial Permutation on ciphertext
    ip_output = permute(ciphertext_64bit, IP_TABLE)
    print_block("After Initial Permutation (IP)", ip_output)

    # Split into left and right halves
    left = ip_output[:32]
    right = ip_output[32:]

    print(f"\nSplit after IP:")
    print(f"L0 = {left}")
    print(f"R0 = {right}")

    # Reverse round keys for decryption
    reversed_keys = round_keys[::-1]

    # Feistel rounds
    for i in range(rounds):
        left_before = left
        right_before = right

        f_output = round_function(right_before, reversed_keys[i])
        left = right_before
        right = xor_bits(left_before, f_output)

        print_round_diagram(
            i + 1,
            left_before,
            right_before,
            reversed_keys[i],
            f_output,
            left,
            right
        )

    # Final swap
    combined = right + left
    print("\nAfter final swap:")
    print_block("Preoutput Block", combined, group=8)

    # Final permutation
    plaintext = permute(combined, FP_TABLE)
    print_block("Recovered Plaintext", plaintext)

    return plaintext


def is_valid_binary_string(bits, required_length):
    return len(bits) == required_length and all(bit in '01' for bit in bits)


def main():
    print("=" * 70)
    print("DES-STYLE FEISTEL CIPHER DEMO")
    print("=" * 70)
    print("\nRequirements:")
    print("- Plaintext must be 64 bits")
    print("- Key must be 64 bits")
    print("- Only 0 and 1 are allowed\n")

    # Example input
    default_plaintext = "0001001000110100010101100111100010011010101111001101111011110001"
    default_key =       "0001001100110100010101110111100110011011101111001101111111110001"

    print("Example plaintext (64-bit):")
    print(default_plaintext)
    print("\nExample key (64-bit):")
    print(default_key)

    use_default = input("\nUse default values? (y/n): ").strip().lower()

    if use_default == 'y':
        plaintext = default_plaintext
        key = default_key
    else:
        plaintext = input("Enter 64-bit plaintext: ").strip()
        key = input("Enter 64-bit key: ").strip()

        if not is_valid_binary_string(plaintext, 64):
            print("\nError: Plaintext must be exactly 64 bits and contain only 0 and 1.")
            return

        if not is_valid_binary_string(key, 64):
            print("\nError: Key must be exactly 64 bits and contain only 0 and 1.")
            return

    ciphertext, round_keys = feistel_encrypt(plaintext, key, rounds=16)
    recovered_plaintext = feistel_decrypt(ciphertext, round_keys, rounds=16)

    print("\n" + "=" * 70)
    print("FINAL RESULT")
    print("=" * 70)
    print_block("Original Plaintext ", plaintext)
    print_block("Ciphertext         ", ciphertext)
    print_block("Decrypted Plaintext", recovered_plaintext)

    if plaintext == recovered_plaintext:
        print("\nSuccess: Decryption matches original plaintext.")
    else:
        print("\nError: Decryption does not match original plaintext.")


if __name__ == "__main__":
    main()