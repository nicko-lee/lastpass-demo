import sys
from hashlib import sha256

# Prove app has started
print("Hello World")


pw = input('Enter Password: ')
h = sha256(pw.encode('utf-8')).digest()

N = 100
for i in range(N):
    if i != N-1:
        h = sha256(h).digest()
        print(f"Iteration #{i+1}: {sha256(h).hexdigest()}")  

    else:
        h = sha256(h).hexdigest()


