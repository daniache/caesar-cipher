CAESAR CIPHER ENCRYPTION ENCTYPTION APPLICATION

This project is a Caesar cipher application. For those who do not know what is a Caesar cipher, it is a basic encryption technique where each letter in a text is shifted a certain number of places down or up the alphabet. With this application, it can both encrypt and decrypt text based on the user’s input.

TECHNOLOGIES USED

Programming Language: Python
Data Structure: A Python list (alphabet) is used to represent the letters of the alphabet for performing the shift-based encryption and decryption.
User Input: The input() function is used to interact with the user.

FUNCTIONALITIES

Encrypt a message:

- Converts the input text into an encrypted form by shifting each letter by the specified number of places.
- Non-alphabetic characters (like spaces or punctuation) remain unchanged.
- Example: If the input is "hello" with a shift of 2, the output is "jgnnq".

Decrypt a message:

- Converts the encrypted text back to its original form by reversing the shift.
- Example: If the input is "jgnnq" with a shift of 2, the output is "hello".

Handles invalid input gracefully:

- Prints an error message for invalid input, such as entering a direction other than encode or decode.

HOW TO INVOKE THE APPLICATION

1. Run the code in a Python environment:

    - Open a terminal or IDE (such as VS Code or PyCharm).
    - Copy and paste the code into a Python file OR download it from the folder ""
    - Run the file using the command: python name_of_the_file.py

   If you are using an IDE, simply open it within the IDE through the File Menu.

2. Provide inputs as prompted:

    - Enter 'encode' to encrypt or 'decode' to decrypt.
    - Input the message you want to process.
    - Provide a numerical value for the shift.
