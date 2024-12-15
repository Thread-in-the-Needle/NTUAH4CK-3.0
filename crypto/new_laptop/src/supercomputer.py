from math import prod

def superfast_product_up_to_x_mod_n(x, n):
    if x == n: return 0
    ret = n - 1 # product up to n - 1 mod n by Wilson's theorem
    if x < n:
        ret = ret * pow(prod(range(x + 1, n)), -1, n) % n # remove excess
    elif x > n:
        ret = ret * prod(range(n + 1, x+1)) % n # mul by the extra except for n
    return ret
