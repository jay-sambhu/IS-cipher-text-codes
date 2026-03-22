def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
            
    return result


def caesar_decrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
            
    return result


def print_caesar_table(title, input_text, output_text, shift):
    print(f"\n{title}")
    print("+-----+-------+---------+--------+")
    print("| Pos | Input | Shifted | Output |")
    print("+-----+-------+---------+--------+")

    for index, (inp, outp) in enumerate(zip(input_text, output_text), start=1):
        shifted = str(shift if inp.isalpha() else 0)
        print(f"| {str(index).rjust(3)} | {inp.center(5)} | {shifted.rjust(7)} | {outp.center(6)} |")

    print("+-----+-------+---------+--------+")


def print_styled_output(stage, input_text, shift, output_text):
    print("\n" + "=" * 42)
    print(f"          CAESAR {stage} OUTPUT")
    print("=" * 42)
    print(f"Input  : {input_text}")
    print(f"Shift  : {shift}")
    print(f"Output : {output_text}")
    print("=" * 42)


print("=== Caesar Cipher Program ===")

# user input
message = input("Enter the text you want to encrypt: ")
shift = int(input("Enter the shift value (key): "))

# encryption
encrypted_text = caesar_encrypt(message, shift)
print_caesar_table("Encryption Table", message, encrypted_text, shift)
print_styled_output("ENCRYPTION", message, shift, encrypted_text)

print("\nDescription: Each letter in the message was shifted forward by", shift, "positions in the alphabet.")

# ask user for decryption
choice = input("\nDo you want to decrypt the message? (yes/no): ")

if choice.lower() == "yes":
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print_caesar_table("Decryption Table", encrypted_text, decrypted_text, shift)
    print_styled_output("DECRYPTION", encrypted_text, shift, decrypted_text)
    print("Description: The encrypted text was shifted back by", shift, "positions to get the original message.")
else:
    print("\nDecryption skipped. Program finished.")