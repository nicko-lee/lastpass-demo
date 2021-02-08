import sys
import hashlib

# Prove app is running and log some data for easy coding
print("Hello World")
print(f"Arguments count: {len(sys.argv)}")
print(sys.argv)

# Access user provided master password
master = sys.argv[1] # Access master password
print("master as a string: ", master)
master = master.encode('utf_8')
print("master after encoding: ", master)

# Hash master pw
scramble = hashlib.sha256() # Use SHA256 hashing algo
scramble.update(master) # Give it the string you want to hash
print("scramble value prior to calling hexdigest() on it: ", scramble)
print(scramble.hexdigest())