alphabet = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

def decrypt(cipherText, delimiter = " "):
    cipherList = cipherText.split(delimiter)
    text = ""

    for number in cipherList:
        count = 0
        found = False
        for letter in alphabet:
            count += 1
            if number == str(count):
                text += letter
                found = True
                break
        if found == False:
            text += number
    
    return text

def encrypt(text, addDelimiter = " "):
    textList = [*text]
    cipherText = ""

    for char in textList:
        count = 0
        found = False
        for letter in alphabet:
            count += 1
            if char.upper() == letter:
                cipherText += f"{count}{addDelimiter}"
                found = True
                break
        if not found:
            cipherText += char
    return cipherText