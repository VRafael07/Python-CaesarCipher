MAX_KEY_VALUE = 26


def getMode():

    """This function gets the mode that the user wants
    the available ones are encrypt, decrypt or brute force
    a specific message."""

    while True:
        mode = input(
            "Would you like to encrypt, decrypt, or brute force a message?\n"
            ).lower()
        modeOptions = ['encrypt', 'decrypt', 'e', 'd', 'brute', 'b']
        if mode in modeOptions:
            return mode
        else:
            print("Invalid input!")


def getMessage():

    """This one gets the message to be
    decrypted/encrypted/brute forced."""

    return input("What's the message? ")


def getKey():

    """This one gets the key range of the Caesar Cipher.
    Originally it was three characters to the left, but
    nowadays it's possible do to 26 characters."""

    while True:
        Key = int(
            input("What's the key range of the cryptography? (1 - {})".format(
                str(MAX_KEY_VALUE)
            )))
        if 1 <= Key <= MAX_KEY_VALUE:
            return Key


def getCriptography(mode, message, key):

    """This one will decrypt/encrypt/brute force
    the message that the user asked to do one of
    the functions above."""

    if mode[0] == 'e':
        key = -key
    translated = ""
    for symbol in message:

        if symbol.isalpha():
            num = ord(symbol)
            num += key

            """There are some problems when we talk about the
            Caesar Cipher, since the alphabet has 26 letters,
            when the letter is Z or A it's necessary to wrap
            around all over the alphabet"""

            if symbol.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            elif symbol.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26
            translated += chr(num)

        else:
            translated += symbol
    return translated


mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()

print("Your translated text is:\n")
if mode[0] != 'b':
    print(getCriptography(mode, message, key))
else:
    for key in range(1, MAX_KEY_VALUE):
        print(key, getCriptography('decrypt', message, key))
