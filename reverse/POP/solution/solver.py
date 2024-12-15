from base64 import b64decode
import arc4

def main():
    enc_string = "DBziwCh2U7mVnRoEzhXJXdyFwQYf0rwZI0oj76TokRPp4/mIJpd/tA8xJZ4nXeUlYl9NY0XI+d55ApbCKhWjLsKfPJepW7vCe0fJF2gG2J1nJJxxgCFpr4+kq1kE7pCXBvVcGf4nWv2nLcqDKN+g7IS4d1owd2qq61GPyHefQDi3lVn8H/FzO0COp+9BPsJc8GVsWCJZ2AeYhFf91vXP+wyFj6RPmylH8yz37bzE/3bYV6OK3t/u2YbQj/JWlsGQk5kjuELogZYNUn9c2oSfsaTqMQmKUXTRJMFp0NVubAEJtQPg7AzvTY5oX0BABBTKMpLIJsXhhs036ZYue3oBaOqPq/Cen0ek89FeGxLt98nEFKk4xvq9+XtI1ZSYqfYw7lCtl49yNjuTfa7fE51netthfoASWSImpV3vw3WqNBCO/ifcrq3SIarEJIulw52TfqS5+SXPgLAzXDaWz6E/41gp1GyegON4/mtzP64qr55zNypCW5KQmYlXN+aTDNmD2uKRAKENSh6F5Kfixz9TDPjzKvjJ66zSjcN7uYVnytQHxIAc6WCA/q51oYkLpwZK5tSIkAFyXbM6xpCNdnHsMEVv8RhuuooOz/4luibS5Caw7NK9bR6aCwCNrDv45hHpE/XWHOdEsm5a5hmfaZr3vhgql82MsKHbUsE3nck0YAimrvXOdDxumXGc9O8gBOCV9Qo3+3KyBYyp4vjgtKPfJaxhFCVigAkshIEKfGgQLAgfg0jB7rmjYFZaCo+NMpf3WcjCSG/bGiPekUFxkV0ICppM+Llu1k/We1JmaanobOaJIe+YKTvG6duNRqwm3wDnEA=="
    magic = b'\x13\x37\x13\x37'

    target = b64decode(enc_string)

    while target[:4] != magic:
        key_len = target[0]
        junk_len = target[1]
        key = target[2+junk_len:2+junk_len+key_len]
        enc_target = target[2+junk_len+key_len:]
        
        rc = arc4.ARC4(key)
        target = rc.decrypt(enc_target)

    print(target[4:].decode())

if __name__ == "__main__":
    main()