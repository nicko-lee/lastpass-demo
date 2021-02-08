import sys
import time
from hashlib import sha256

# Prove app has started
print("Hello World")

# Source: https://stackoverflow.com/questions/60241267/how-to-hash-sha256-many-times-in-python
pw = input('Enter Password: ')
h = sha256(pw.encode('utf-8')).digest()

N = 1000
for i in range(N):
    if i != N-1:
        h = sha256(h).digest()
        time.sleep(0.01) ## in order for people to see the steps else it is too fast
        print(f"Iteration #{i+1}: {sha256(h).hexdigest()}")  

    else:
        h = sha256(h).hexdigest()


