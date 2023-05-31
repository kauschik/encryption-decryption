# File Encryption/Decryption

This is a Python program that encrypts and decrypts files using a symmetric encryption algorithm. Users can specify a file to encrypt and a secret key to protect the data. The program also supports encrypting and decrypting folders.

## Features

- Encrypts individual files using a symmetric encryption algorithm.
- Decrypts encrypted files using the corresponding encryption key.
- Supports encrypting and decrypting entire folders and their subfolders.
- Saves each encryption key in a separate file for decryption.

## Prerequisites

- Python latest
- `cryptography` library: You can install it by running `pip install cryptography`.

## Usage

1. Clone this repository or download the `encryption-decryption.py` file.

2. Open a terminal or command prompt and navigate to the directory containing the `encryption-decryption.py` file.

3. Run the following command to install the required `cryptography` library (if not already installed):
    pip install cryptography

4. Run the program using the following command:
    python encryption-decryption.py


5. The program will prompt you to choose an option:
- Enter "e" to encrypt a folder or file.
- Enter "d" to decrypt a folder or file.

6. Follow the on-screen instructions to provide the necessary inputs:
- For encryption:
  - Specify the path to the file or folder you want to encrypt.
  - Specify the desired path for the encrypted file(s) or folder.
- For decryption:
  - Specify the path to the encrypted file or folder you want to decrypt.
  - Provide the corresponding encryption key when prompted.

7. After the encryption or decryption process is complete, the program will display a success message with the path to the output file(s) or folder.


## Example

### Encryption
    
    Enter "e" to encrypt or "d" to decrypt a folder: e
    
    Enter the path to the folder you want to encrypt: /home/kauschik/work-files/projects/File Encryption or Decryption/test-files
    
    Enter the desired path for the encrypted folder: /home/kauschik/work-files/projects/File Encryption or Decryption/encrypted-files
    
    Folder encrypted and saved as /home/kauschik/work-files/projects/File Encryption or Decryption/encrypted-files


### Decryption

    Enter "e" to encrypt or "d" to decrypt a folder: d
    
    Enter the path to the folder you want to decrypt: /home/kauschik/work-files/projects/File Encryption or Decryption/encrypted-files
    
    Enter the desired path for the decrypted folder: /home/kauschik/work-files/projects/File Encryption or Decryption/decrypted-files
    
    Enter the encryption key for file 'jjk wallpaper.jpeg.enc': rXlVOR_kSEiOLwHrU1Hp5C_WIxKTcSlqUxf8RQifGzM=
    
    File decrypted and saved as /home/kauschik/work-files/projects/File Encryption or Decryption/decrypted-files/jjk wallpaper.jpeg
## Important Notes

- When encrypting a folder, the program will create an "encryptions" folder (if it doesn't exist) to store the encryption key files. Or it will just create the encryption key file alongside the encrypted file in the path you selected.

- When decrypting a file, make sure to provide the correct encryption key that corresponds to the file. The program will prompt you to enter the encryption key when necessary.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and use the code according to your needs.

## Acknowledgements

This project utilizes the [cryptography](https://cryptography.io) library for encryption and decryption.
