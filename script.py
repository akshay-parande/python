import sys
import shutil
import os

def encrypt_file(input_file, key):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as f:
            content = f.read()
        
        # Encrypt the content
        encrypted_content = ''
        key_index = 0
        
        for char in content:
            key_char = key[key_index % len(key)]
            encrypted_char = chr((ord(char) + ord(key_char)) % 128)  # Ensure printable ASCII range
            encrypted_content += encrypted_char
            key_index += 1
        
        # Write the encrypted content to the original file
        with open(input_file, 'w') as f:
            f.write(encrypted_content)
        
        print("File successfully encrypted.")

    except FileNotFoundError:
        print("Input file not found.")

def decrypt_file(input_file, key):
    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            print("Input file not found.")
            return

        # Read the encrypted content from the input file
        with open(input_file, 'r') as f:
            encrypted_content = f.read()
        
        # Decrypt the content
        decrypted_content = ''
        key_index = 0
        
        for char in encrypted_content:
            key_char = key[key_index % len(key)]
            decrypted_char = chr((ord(char) - ord(key_char)) % 128)  # Ensure printable ASCII range
            decrypted_content += decrypted_char
            key_index += 1

        # Write the decrypted content to the original file
        with open(input_file, 'w') as f:
            f.write(decrypted_content)
        
        print("File successfully decrypted.")

    except Exception as e:
        print("An error occurred during decryption:", str(e))


def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file key action")
        print("Action: 'encrypt' or 'decrypt'")
        sys.exit(1)

    input_file = sys.argv[1]
    key = sys.argv[2]
    action = sys.argv[3]

    # Perform the specified action
    if action == 'encrypt':
        encrypt_file(input_file, key)
    elif action == 'decrypt':
        decrypt_file(input_file, key)
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
