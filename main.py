import encryption.Caesar_cipher as caesar
import encryption.Atbash_cipher as atbash
import tools.order as order

output = caesar.encrypt("ynnuf", 1)
output = caesar.decrypt(output, 1)
output = order.reverse(output)
print(output)

print(atbash.encrypt("pvvk gsrh hvxivg"))