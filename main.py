import encryption.A1Z26 as A1Z26

text = "Helloworld"
encryptedText = A1Z26.encrypt(text)
print(encryptedText)
decryptedText = A1Z26.decrypt(encryptedText)
print(decryptedText)