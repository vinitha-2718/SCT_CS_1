

def encrypt(text, shift):
    """Encrypts a string using the Caesar Cipher."""
    result = ""
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # If it's not a letter, just add it to the result
            result += char
    return result


def decrypt(text, shift):
    """Decrypts a string using the Caesar Cipher."""
    # Decrypting is the same as encrypting with a negative shift
    return encrypt(text, -shift)


def main():
    """Main function to handle user input and perform the operations."""
    print("--- Caesar Cipher Program ---")
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? (e/d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

    message = input("Enter the message: ")

    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if mode == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    else:  # mode == 'd'
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
