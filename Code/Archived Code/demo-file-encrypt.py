
from Crypto.Cipher import AES

pw_list = open("sample_data.csv", "r")

# Before encryption
print("BEFORE ENCRYPTION")
print("-----------------\n")
for line in pw_list:
  print(line)

# After encryption
print("\n")
print("AFTER ENCRYPTION")
print("----------------\n")

# Use AES encryption to encrypt the contents of file
# Use pycrypto library https://pypi.org/project/pycrypto/
# https://www.dlitz.net/software/pycrypto/api/current/
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = pw_list
ciphertext = obj.encrypt(message)
print(ciphertext)

obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
print(obj2.decrypt(ciphertext))