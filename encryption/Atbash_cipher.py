defaultAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
defaultAtbash = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

def encrypt(text, alphabet = defaultAlphabet, atbash = defaultAtbash):
    textList = [*text]
    alphabetList = [*alphabet]
    atbashList = [*atbash]
    
    encryptedText = ""
    for char in textList:
        found = False
        for letter in alphabetList:
            if letter == char.upper():
                index = alphabetList.index(letter)
                encryptedText += atbashList[index]
                found = True
                break
        if found == False:
            encryptedText += char
    
    return encryptedText

def decrypt(text, alphabet = defaultAlphabet, atbash = defaultAtbash):
    textList = [*text]
    alphabetList = [*alphabet]
    atbashList = [*atbash]
    
    decryptedText = ""
    for char in textList:
        found = False
        for letter in atbashList:
            if letter == char.upper():
                index = atbashList.index(letter)
                decryptedText += alphabetList[index]
                found = True
                break
        if found == False:
            decryptedText += char
    
    return decryptedText