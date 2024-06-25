def caesar_cipher(text: str, shift: int, direction: str) -> str:
    """
    Encrypts or decrypts a text using the Caesar Cipher algorithm.

    Args:
        text (str): The text to encrypt or decrypt.
        shift (int): The shift value to apply.
        direction (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            char_code = ord(char) - ascii_offset
            if direction == 'encrypt':
                char_code = (char_code + shift) % 26
            elif direction == 'decrypt':
                char_code = (char_code - shift) % 26
            result += chr(char_code + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        print("Caesar Cipher Program")
        print("---------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            text = input("Enter a message to encrypt: ")
            shift = int(input("Enter a shift value: "))
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print(f"Encrypted text: {encrypted_text}")
        elif choice == '2':
            text = input("Enter a message to decrypt: ")
            shift = int(input("Enter a shift value: "))
            decrypted_text = caesar_cipher(text, shift, 'decrypt1')
            print(f"Decrypted text: {decrypted_text}")
        elif choice == '3':
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()