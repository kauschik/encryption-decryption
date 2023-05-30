import os
from cryptography.fernet import Fernet


def generate_key():
    """Generate a random encryption key."""
    return Fernet.generate_key()


def save_key(key, filename):
    """Save the encryption key to a file."""
    with open(filename, 'wb') as file:
        file.write(key)


def load_key(filename):
    """Load the encryption key from a file."""
    with open(filename, 'rb') as file:
        return file.read()


def encrypt_file(key, input_file, output_file):
    """Encrypt the input file using the provided key and save the result to the output file."""
    cipher = Fernet(key)
    with open(input_file, 'rb') as file:
        plaintext = file.read()
    ciphertext = cipher.encrypt(plaintext)
    with open(output_file, 'wb') as file:
        file.write(ciphertext)


def decrypt_file(key, input_file, output_file):
    """Decrypt the input file using the provided key and save the result to the output file."""
    cipher = Fernet(key)
    with open(input_file, 'rb') as file:
        ciphertext = file.read()
    plaintext = cipher.decrypt(ciphertext)
    with open(output_file, 'wb') as file:
        file.write(plaintext)


def encrypt_folder(key, input_folder, output_folder):
    """Encrypt all files in the input folder and its subfolders using the provided key."""
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            input_file = os.path.join(root, file)
            relative_path = os.path.relpath(input_file, input_folder)
            output_file = os.path.join(output_folder, relative_path + '.enc')

            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            encrypt_file(key, input_file, output_file)
            key_file = os.path.join(output_folder, relative_path + '.key')
            save_key(key, key_file)


def decrypt_folder(input_folder, output_folder):
    """Decrypt all files in the input folder and its subfolders using the provided key."""
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.enc'):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_folder)
                output_file = os.path.join(output_folder, os.path.splitext(relative_path)[0])
                key_file = os.path.join(input_folder, relative_path + '.key')

                # Prompt the user to enter the encryption key
                key = input(f"Enter the encryption key for file '{relative_path}': ")

                try:
                    loaded_key = load_key(key_file)
                    decrypt_file(loaded_key, input_file, output_file)
                    print(f"File decrypted and saved as {output_file}")
                except FileNotFoundError:
                    print(f"Encryption key file '{key_file}' not found. Skipping decryption.")


# Example usage
key_folder = 'encryptions'

# Generate a new encryption key
encryption_key = generate_key()

# Get the encryption or decryption option from the user
option = input('Enter "e" to encrypt or "d" to decrypt a folder: ')

if option == 'e':
    # Get the folder paths from the user
    input_folder = input('Enter the path to the folder you want to encrypt: ')
    output_folder = input('Enter the desired path for the encrypted folder: ')

    # Encrypt the folder
    encrypt_folder(encryption_key, input_folder, output_folder)
    print(f'Folder encrypted and saved as {output_folder}')

elif option == 'd':
    # Get the folder paths from the user
    input_folder = input('Enter the path to the folder you want to decrypt: ')
    output_folder = input('Enter the desired path for the decrypted folder: ')

    # Decrypt the folder
    decrypt_folder(input_folder, output_folder)

else:
    print('Invalid option. Please choose "e" to encrypt or "d" to decrypt a folder.')
