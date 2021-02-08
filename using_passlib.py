import sys
from passlib.hash import pbkdf2_sha256

# Access CLI argument to accept master password
master = sys.argv[1] # Access master password
print(f"Master password: {master}")

# Hash the password
hashed_pw = pbkdf2_sha256.hash(master)
print(f"Hashed password: {hashed_pw}")
print(f"Hashed password: {hashed_pw.digest}")

# Hash the password 100 times
# for x in range(10):
#   hashed_pw = pbkdf2_sha256.hashed_pw(hashed_pw)
#   print(f"Hashed password: {hashed_pw}")