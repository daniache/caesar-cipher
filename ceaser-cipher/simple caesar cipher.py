alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encrypt the text
def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            # Calculate new position with wrap-around
            new_position = (alphabet.index(char) + shift) % 26
            cipher_text += alphabet[new_position]
        else:
            # Keep characters that are not in the alphabet unchanged
            cipher_text += char
    print(f"The encoded text is {cipher_text}")

# Get user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Call the encrypt function
if direction == 'encode':
    encrypt(text, shift)
else:
    print("Invalid input. Use 'encode' to encrypt.")

# Function to decrypt the text
def decrypt(text, shift):
    decipher_text = ""
    for char in text:
        if char in alphabet:
            # Calculate new position with wrap-around for decryption
            new_position = (alphabet.index(char) - shift) % 26
            decipher_text += alphabet[new_position]
        else:
            # Keep characters that are not in the alphabet unchanged
            decipher_text += char
    print(f"The decoded text is {decipher_text}")

# Call the encrypt or decrypt function based on user input
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("Invalid input. Use 'encode' to encrypt or 'decode' to decrypt.")
