from Crypto.Util.number import long_to_bytes
from pwn import *
from gmpy2 import iroot
from sympy.ntheory.modular import crt

context.log_level = 'warn'
n_rs = []
e = 3

while len(n_rs) < 3:
    print(f"[+] Number of ctxts collected: {len(n_rs)}/{e}", end= "\r")
    conn = process(["./letter_from_santa"])
    conn.recvuntil(b"n = ")
    n = int(conn.recvline().decode().strip())
    conn.sendline(b"-2147483645") # 0x80000003
    for _ in range(5):
        conn.recvuntil(b"...")
    conn.recvline()
    res = conn.recvline()
    if b"lotto" in res:
        conn.close()
        continue
    c = int(res.decode().strip().split()[-1])
    if c == 1:
        conn.close()
        continue
    n_rs.append((n, c))

number = crt(*zip(*n_rs))[0]
flag, check = iroot(number, e)
if check:
    flag = long_to_bytes(int(flag))
    if b"NH4CK" in flag:
        print(flag.decode())
        exit()
else:
    print("fail")

