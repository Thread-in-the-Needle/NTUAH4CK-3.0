from base64 import b64encode
import random
from arc4 import ARC4

# ---| KEY_LEN | OFFSET | JUNK | KEY | DATA | ENCRYPTED ----

FLAG = b"NH4CK{P4In_n0t_t0_c0M3_t0_u5_pl34s3}"
FLAG_HEAD = b"\x13\x37\x13\x37"

key_min = 4
key_max = 16

junk_min = 4
junk_max = 110

def encrypt_flag(rounds):

    payload = FLAG_HEAD + FLAG

    for i in range(rounds):
        # Generate Key
        key_length = random.randint(key_min,key_max)
        key = random.randbytes(key_length)

        # Encrypt payload with key
        rc = ARC4(key)
        payload = rc.encrypt(payload)

        # Generate junk
        junk_length = random.randint(junk_min,junk_max)
        junk = random.randbytes(junk_length)

        payload = bytes([key_length]) + bytes([junk_length]) + junk + key + payload

    return payload

def main():
    print(b64encode(encrypt_flag(10)))

if __name__ == "__main__":
    main()
