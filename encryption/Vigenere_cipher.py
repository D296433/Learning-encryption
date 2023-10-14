defaultAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, key, alphabet=defaultAlphabet):
    ciphertext = ""
    key = key.upper()
    plaintext = plaintext.upper()
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            ciphertext += alphabet[(alphabet.index(plaintext[i]) + alphabet.index(key[i % len(key)])) % len(alphabet)]
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt(ciphertext, key, alphabet=defaultAlphabet):
    plaintext = ""
    key = key.upper()
    ciphertext = ciphertext.upper()
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            plaintext += alphabet[(alphabet.index(ciphertext[i]) - alphabet.index(key[i % len(key)])) % len(alphabet)]
        else:
            plaintext += ciphertext[i]
    return plaintext

def brute_force(ciphertext, alphabet=defaultAlphabet):
    plaintext = ""
    for i in range(len(alphabet)):
        plaintext += decrypt(ciphertext, alphabet[i])
        plaintext += "\n"
    return plaintext