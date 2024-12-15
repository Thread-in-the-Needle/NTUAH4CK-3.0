from pwn import *
from sage.all import *
from randcrack import RandCrack
from Crypto.Util.number import isPrime

e = 65537
rc = RandCrack()

LOCAL = True
if LOCAL:
    conn = process(["python", '../src/server.py'])
else:
    conn = remote("ip", 1337)

def get_num():
    return int(conn.recvline().decode().strip().split()[-1])

def extract_ind(num):
    last_4 = str(num)[-4:]
    if last_4 == '0000': return 0
    return int(last_4.lstrip("0"))

def split_32(num, i):
    bits = f"{num:0{i*32}b}"
    blocks = [int(bits[32*j:32*j+32], 2) for j in range(i)]
    assert len(blocks) == i
    assert not any([b == 0 for b in blocks])
    return blocks[::-1]

conn.recvline()
conn.recvline()


nums32 = []
# first three rounds can be passed with actually simply factoring the number
for i in range(1, 4):
    print(conn.recvline().decode().strip())
    n = get_num()
    conn.recvuntil(b": ")
    messages = eval(conn.recvline())
    num_msgs = len(messages)
    arrstates = i*(num_msgs + 2)*[0]
    p, q = [f[0] for f in factor(n)]
    print(p, q)
    p_ind = extract_ind(p)*i
    arrstates[p_ind:p_ind + i] = split_32(int(bin(int(str(p)[:-4]))[3:], 2), i)
    q_ind = extract_ind(q)*i
    arrstates[q_ind:q_ind + i] = split_32(int(bin(int(str(q)[:-4]))[3:], 2), i)

    d = pow(e, -1, (p - 1)*(q - 1))
    for j in range(num_msgs):
        c = messages[j]
        m = pow(c, d, n)
        conn.sendline(str(m).encode())
        m_ind = extract_ind(m)*i
        assert all([aa == 0 for aa in arrstates[m_ind:m_ind + i]])
        arrstates[m_ind:m_ind + i] = split_32(int(str(m)[:-4]), i)
    nums32 += arrstates
print(f"{len(nums32) = }")


def get_primes_and_messages_randcrack(nbits, rc):
    primes = []
    messages = []
    ind = 0
    while True:
        num = rc.predict_getrandbits(nbits)
        poss_prime = int(f"{(1 << nbits) + num}{ind:04}")
        if isPrime(poss_prime):
            primes.append(poss_prime)
        else:
            messages.append(int(f"{num}{ind:04}"))
        if len(primes) == 2:
            return primes, messages
        ind += 1

if len(nums32) < 624:
    print("not enough")
    exit()

# crack rng
for i in range(624):
    rc.submit(nums32[i])
for i in range(len(nums32) - 624):
    assert rc.predict_getrandbits(32) == nums32[624+i]

# predict future outputs
for i in range(7 - 3):
    primes, msgs = get_primes_and_messages_randcrack(32*(4+i), rc)
    print(conn.recvline().decode().strip())
    n = get_num()
    conn.recvuntil(b": ")
    messages = eval(conn.recvline())
    num_msgs = len(messages)

    for j in range(num_msgs):
        c = messages[j]
        conn.sendline(str(msgs[j]).encode())
print(conn.recvline())
