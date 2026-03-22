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


print("=== Caesar Cipher Program ===")

# user input
message = input("Enter the text you want to encrypt: ")
shift = int(input("Enter the shift value (key): "))

# encryption
encrypted_text = caesar_encrypt(message, shift)
print("\nEncrypted Message:", encrypted_text)

print("\nDescription: Each letter in the message was shifted forward by", shift, "positions in the alphabet.")

# ask user for decryption
choice = input("\nDo you want to decrypt the message? (yes/no): ")

if choice.lower() == "yes":
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print("\nDecrypted Message:", decrypted_text)
    print("Description: The encrypted text was shifted back by", shift, "positions to get the original message.")
else:
    print("\nDecryption skipped. Program finished.")