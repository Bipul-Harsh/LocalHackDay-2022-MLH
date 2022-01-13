import argparse

def cipher(TEXT, SHIFT):
    """
    This function is used to cipher a text.

    Parameters:
        TEXT: Text to be ciphered.
        SHIFT: Shift to be used.
    
    Returns:
        Ciphered text.
    """
    CIPHERED_TEXT = ""
    for i in TEXT:
        if i.isalpha():
            if i.isupper():
                CIPHERED_TEXT += chr((ord(i) + SHIFT - 65) % 26 + 65)
            else:
                CIPHERED_TEXT += chr((ord(i) + SHIFT - 97) % 26 + 97)
        else:
            CIPHERED_TEXT += i
    return CIPHERED_TEXT

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    prog="Cipher Generator",
    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--text', type=str, help="Provide any text to convert to cipher.",nargs='*')
    parser.add_argument('--shift', type=int, default=1, help="Provide an integer value that will be use to shift the characters.")

    args = parser.parse_args()
    TEXT = ' '.join(args.text)
    SHIFT = args.shift
    
    print(f'Cipher: {cipher(TEXT, SHIFT)}\nShift: {SHIFT}')