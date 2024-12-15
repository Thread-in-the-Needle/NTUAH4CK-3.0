
enc = open("./encrypted", "rb").read()
assert len(enc) % 5 == 0

vals = list(enc[:-len(enc)//5])
enc = list(enc[-len(enc)//5:])
print(f"{enc = }")
flag = []
with open("chall", "rb") as f:
    data = f.read()
    ind = 0
    for i in range(len(enc)):
        ind = sum(vals[4*i:4*i+4])
        while data[ind] == 0:
            ind += 1
        flag.append((enc[i] ^ data[ind]) % 256)
print(bytes(flag))
