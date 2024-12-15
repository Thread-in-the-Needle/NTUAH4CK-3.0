from hashlib import sha256
from secret import FLAG

half = len(FLAG)//2

D1 = []
for i in range(half):
    D1.append(sha256(FLAG[:i+1]).hexdigest())
print(f"{D1 = }")

D2 = []
for i in range(half):
    D2.append(sha256(FLAG[:half + i+1]).digest()[0])
print(f"{D2 = }")