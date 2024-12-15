from pwn import *


LOCAL = True
if LOCAL:
    conn1 = process(['python', 'server.py'])
    conn2 = process(['python', 'server.py'])
else:
    ip = ''
    port = 0
    conn1 = remote(ip, port)
    conn2 = remote(ip, port)

conn1.recvuntil(b"> ")
conn2.recvuntil(b"> ")

conn1.sendline(b"1")
encflag = bytes.fromhex(conn1.recvline().decode().strip())

conn2.sendline(b"2")
conn2.recvuntil(b": ")
conn2.sendline(b"00"*len(encflag))
xor_with_this = bytes.fromhex(conn2.recvline().decode().strip())
print(xor(xor_with_this, encflag))

