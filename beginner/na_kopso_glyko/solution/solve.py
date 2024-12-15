from pwn import *
from string import printable
import time
import random
import json

def random_flouri_generator():
    m = 10**30
    return random.randint(1, m)**11 + 17*random.randint(1, m)**7 - 42*random.randint(1, m)**5 + 1337*random.randint(1, m)*3 + 31337*random.randint(1, m)


printable = printable[:printable.index(" ")]

conn = process(["python", "../challenge/server.py"])
conn.recvline()
conn.recvline()
timer = time.time()
flag = "NH4CK{"
while "}" not in flag:
    times = []
    for c in printable:
        t = time.time()
        json_inp = {"password": flag + c, "number": 0}
        conn.sendlineafter(b": ", json.dumps(json_inp).encode())
        res = conn.recvline()
        if b"GLYKO and HUGS" in res:
            print(flag + c)
            print(f"Total time: {time.time() - timer}")
            exit()
        times.append(time.time() - t)

    flag += printable[times.index(min(times))]
    print(flag)

    