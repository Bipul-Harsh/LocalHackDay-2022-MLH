import argparse

def encrypt(password, key):
    '''
    Encrypt given password in following way:
    1. Convert to ASCII value, add key and 10 to it.
    2. If the character on the resultant ASCII value is alphabet, convert it case.
    3. Reverse final string.
    '''
    encrypted_password = ''
    for char in password:
        ascii_value = (ord(char) + key + 10)%256
        if chr(ascii_value).isalpha():
            if char.isupper():
                encrypted_password += chr(ascii_value).upper()
            else:
                encrypted_password += chr(ascii_value).lower()
        else:
            encrypted_password += chr(ascii_value)
    return encrypted_password[::-1]

def decrypt(password, key):
    '''
    Decrypt the given password encrypted by above method.
    It do:
    - Reverse the string.
    - Convert each char to ASCII and subtract key from it.
    - If the ASCII value is alphabet, convert it case.
    '''
    decrypted_password = ''
    for char in password[::-1]:
        ascii_value = (ord(char)  - key - 10)%256
        if chr(ascii_value).isalpha():
            if char.isupper():
                decrypted_password += chr(ascii_value).upper()
            else:
                decrypted_password += chr(ascii_value).lower()
        else:
            decrypted_password += chr(ascii_value)
    return decrypted_password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    prog="Password Encryptor",
    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--encrypt', type=str, default='', help="Provide password to encrypt. Please provide it with double quotes.",nargs='*')
    parser.add_argument('--decrypt', type=str, default='', help="Provide enrypted string to decrypt. Please put it in \" \"",nargs='*')
    parser.add_argument('--key', type=int, default=0, help="Enter any integer key value.",nargs='?')

    args = parser.parse_args()
    TO_ENCRYPT = ' '.join(args.encrypt)
    TO_DECRYPT = ' '.join(args.decrypt)
    KEY = args.key
    if not (TO_ENCRYPT or TO_DECRYPT):
        print("Please provide a password to encrypt or decrypt.")
        exit(0)

    if TO_ENCRYPT:
        print(f"Encrypted password: {encrypt(TO_ENCRYPT, KEY)}\nKey: {args.key}")
    if TO_DECRYPT:
        print("Decrypted password: {}".format(decrypt(TO_DECRYPT, KEY)))