import sys
import hashlib

# Prove app has started
print("Hello World")

# Access CLI argument to accept master password
master = sys.argv[1] # Access master password
print(f"Master password: {master}")
master = master.encode('utf_8')
print(f"Master password: {master}")

# Hash master pw
scramble = hashlib.sha256() # Use SHA256 hashing algo
scramble.update(master) # Give it the string you want to hash
print(scramble.hexdigest())

# Print all CLI arguments (can remove when complete but will help with debugging)
print(sys.argv)
