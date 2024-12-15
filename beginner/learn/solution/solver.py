from Crypto.Cipher import AES
from base64 import b64encode,b64decode
from tqdm import tqdm # Progress bar :)
from pwn import *   # Import the pwntools module to interact with the server
# t = remote('',)
t = process(['python','../src/server.py'])

t.level = 'debug'  # This will print the data sent and received

# Recieve until the challenges start
t.recvlines(2)

for _ in tqdm(range(25)):
    line = t.recvline().decode()   # This returns bytes, so we need to decode it
    action = line.split()[1]
    match action:
        case 'math':
            line = t.recvuntil(' = ').decode()   # Recieve until the '=' sign  
            t.sendline(str(eval(line[:-2])).encode()) # Send the result of the operation
        
        case 'aes':
            line = t.recvline().decode()
            key = line.split()[-1]
            line = t.recvline().decode()
            enc = line.split()[-1]
            cipher = AES.new(key.encode(), AES.MODE_ECB)
            t.sendlineafter('plaintext = ',cipher.decrypt(bytes.fromhex(enc)))
            
    res = t.recvline().decode()
    if not 'Correct' in res:    # Make sure the answer was correct
        print(res)
        break
        
flag = t.recvline().decode() # If everything went well, the flag is printed
print(flag)
            
            
            
         

