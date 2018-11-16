MAX_KEY_VALUE = 26


def getCriptography(mode, message, key):

    """Decrypt/encrypt/brute force
    the message that the user asked to."""

    outputCounter = 1
    phrase = ""
    if mode == 3:
        # Decrypt the phrase in all possible ways
        for key in range(1, MAX_KEY_VALUE+1):
            phrase += (
                " " + str(key) + "." + getCriptography(2, message, key))
            if outputCounter % 3 == 0:
                phrase += "\n"
            outputCounter += 1
        return phrase
    # To encrypt each letter must go x number of letters backwards.
    if mode == 1:
        key = -key

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
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

            # Convert a Unicode into the respective number and concatenate it.
            phrase += chr(num)
        else:
            phrase += symbol
    return phrase
