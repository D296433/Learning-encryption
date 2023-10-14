import encryption.A1Z26 as A1Z26
import encryption.Caesar_cipher as Caesar

a = Caesar.encrypt("This is fun!", 5)
print(Caesar.bruteforce(a))