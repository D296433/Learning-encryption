defaultAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, shift, alphabet = defaultAlphabet):
    alphabet = [*alphabet]
    alphabetLength = len(alphabet)
    shiftedAlphabet = []

    for char in alphabet:
        index = alphabet.index(char) + shift
        if index >= alphabetLength:
            index = index - alphabetLength
        shiftedAlphabet.append(alphabet[index])

    textList = [*text]
    encryptedText = ""
    for letter in textList:
        found = False
        for char in alphabet:
            if letter.upper() == char:
                found = True
                index = alphabet.index(char)
                encryptedText += shiftedAlphabet[index]
                break
        if not found:
            encryptedText += letter

    return encryptedText

def decrypt(text, shift, alphabet = defaultAlphabet):
    alphabet = [*alphabet]
    alphabetLength = len(alphabet)
    shiftedAlphabet = []

    for char in alphabet:
        index = alphabet.index(char) - shift
        if index >= alphabetLength:
            index = index - alphabetLength
        shiftedAlphabet.append(alphabet[index])

    textList = [*text]
    decryptedText = ""
    for letter in textList:
        found = False
        for char in alphabet:
            if letter.upper() == char:
                found = True
                index = alphabet.index(char)
                decryptedText += shiftedAlphabet[index]
                break
        if not found:
            decryptedText += letter

    return decryptedText

def bruteforce(text, alphabet = defaultAlphabet):
    alphabet = [*alphabet]
    alphabetLength = len(alphabet)
    outputList = []
    for shift in range(alphabetLength):
        shiftedAlphabet = []

        for char in alphabet:
            index = alphabet.index(char) - shift
            if index >= alphabetLength:
                index = index - alphabetLength
            shiftedAlphabet.append(alphabet[index])

        textList = [*text]
        decryptedText = ""
        for letter in textList:
            found = False
            for char in alphabet:
                if letter.upper() == char:
                    found = True
                    index = alphabet.index(char)
                    decryptedText += shiftedAlphabet[index]
                    break
            if not found:
                decryptedText += letter
        outputList.append(decryptedText)
    return outputList