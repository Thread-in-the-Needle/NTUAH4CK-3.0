from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

enc = '666cdbe955066d7c3de97c8abc06427f306825769fc728d87cb683efb5e2567c96157e02869a7a1765245367424b5ca833c2446876686df9db115df63e96045c87e7a5ffec4fabd7c39d66608682a31dc3b3aca49a36f487c0851c6c8cbf3293d4d2cfc3a7a459e9cb45f9e69fa04bd1bad99aa43e3d1a7b12d29a0c1b34b72781eaf20ecd5d126a51484d04d30e9322617869672aad6986a812c0ca1f9b8bdc36fa739dd7d094190f17ae1b43df1f5c1c37e02af8a3bb1d059a0a021f00afe8afaae344b62a5a5b12d3086217f2c40a6a56bcddd2a3565a0ec49bc5e2a304e9c12e667646ea4b59be0b154dec5ccb3d68cac1a5084c6c95154ddead6e683d3dde2ffadcb14e50e67f7d31f8d3ec91f9fff1876541ecb7f91d98fe4955afa6468b095bddd31ec918c132b0115b83407945130efe54b057251d27826a4c4f9e559a1b45ed47ab8ea4d4d58b3b21a6ca84b3f42a28eceeaca2fa77e132413a98f23126da91335f417cf47f95f376a60934575c7e53e1af33da3e3336ee07c0fe21839ee5ef99ece150799d32a660bad69dcc37f2135db5f778b8b2af8ecafeed61cf9c59f1a0f39ec8789c1012d26b4b97d3bf915390b469a057d8d2bfc698ced1612d8b17c7a40f392fb2cfc2cc9781c58209952b6204c95a6bbd902c85171b80fdbeb427626dd01dbd120bcc20ade9c8ab37faa3b9601dc5f423bd2b90e617185c12d3782ef5d0462620c3b95639ef5ef8536f5f0878fe716fbe3719076e8f3922c0e5feceea6a4950306aa4c4088a3b1078d6d19e7c2d7f5819d4e08b7ff1911f5a9fbf2a8142429e6c2ea1c1af9259717014078d2f4e2eb40961ed13a743d1c1e02b33b37dfe26a4ca942b3277748e543a574b1eea039ecaf3f85f12bba0c5b259995ba219a397654bb7afb174a29688e6cf68c66f89921a26e635b6860bb2e9f5a3f8e970396441ac443a3ee880d51e11169a511424a2086dbe6bf769a2f38e7fbd42daed2741641aa291a598cea12452a9c41972051ffe91a1d2e1655bcd0f5a7412f2c1e0b6d8072ee1e7313f83a7934ed23c74bbc6e157732043eb51869dce0f6e3225a67fd2e8dc800027a8efa0b8299b235c1c7184b968fc5c5ea21a96ebec698b50c35fc6697dfe2047d7e9c055359477d459f12f48ae951c99339f42b0d72bc22d6770327fd0fdc14eacd1'
enc = bytes.fromhex(enc)

def modified_keygen(b1, b2):
    key = bytes([b1, b2])
    while len(key) != 16:
        key += bytes([(key[-2] + key[-1]) % 256])
    return key

def aesdec(key, msg, padlen16= True):
    dec = AES.new(key, AES.MODE_ECB).decrypt(msg)
    unpadded = unpad(dec, 16)
    if padlen16:
        assert len(unpadded) == len(dec) - 16
    return unpadded

print("[+] Generating keys")
all_keys = []
for i in range(256):
    for j in range(256):
        all_keys.append(modified_keygen(i, j))

def decrypt_oneround(msg):
    assert len(msg) % 16 == 0, len(msg)
    for k in all_keys:
        try:
            dec = aesdec(k, msg)
            return dec
        except:
            continue
    else:
        print("Didn't find key???")
        exit()

numrounds = 50
for i in range(numrounds - 1):
    print(f"[+] Decrypting round {numrounds - i:>2d}", end= '\r')
    enc = decrypt_oneround(enc)

print("[+] Decrypting final round")
for k in all_keys:
    try:
        flag = aesdec(k, enc, False)
        if b"NH4CK{" in flag:
            print(flag)
    except:
        continue