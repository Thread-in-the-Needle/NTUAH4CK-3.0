from sage.all import *
from pwn import *

LOCAL = True
if LOCAL:
    conn = process(['python', 'calculator.py'])
else:
    ip = ''
    port = 0
    conn = remote(ip, port)

t = [1550, 1548, 8073, 5413, 1411]
# "addition" a + b is implemented like: 3*a + 5*b
# "equality" a == b is implemented like a == b + 1337

# we need the t_i = V_i + V_{i+1} for every i
# translating to "normal" operation for actual integers we need t_i = 3*V_i + 5*V_{i+1}
# additionally we need V_0 + V_1 + V_2 + V_3 + V_4 + V_5 = 0
# or in actual integers: \sum_{i=0}^{5}(3^{5-i}*5*V_i) = 1337
# 6 unknowns, 6 linear equations, solve linear system

M = matrix(ZZ, 6, 6)
v = vector(ZZ, [ti - 1337 for ti in t] + [78606 + 1337])
for i in range(5):
    M[i, i] = 3
    M[i, i + 1] = 5
    M[5, i] = 3**(5 - i)

M[5, 5] = 1
for i in range(5):
    M[5, i + 1] *= 5

values = M.solve_right(v)
print(f"{values = }")
# for u = 2, v = -1, 3*u + 5*v = 1, so to get any target value t for our sum se simply do a = t*u, b = t*v
u = 2
v = -1
values2send = [(t*u, t*v) for t in values]
print(values2send)
for v2s in values2send:
    conn.sendline((f"{v2s[0]} + {v2s[1]}").encode())
    conn.sendline(b"0 * 0")
conn.recvuntil(b"Backdoor activated!!! Spilling secrets: ")
print(conn.recvline())
