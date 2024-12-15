from Crypto.Util.number import isPrime, long_to_bytes
from gmpy2 import iroot, next_prime

n = 729873623543656312134307118912665256781357935692626903169156150433937519752782083907499829904547040251053110020584673588552287964181185247366145284580956529366829912211930759566764271125168397271330673982376560489636282781549333563
c = 55998184521830999281817039472301544636818114568295094941847806390463936789530964194822878197897166490112675455011157083179676040236474209093809166224001096815812124353799949999248500406044583901981864080093522349557347259218634936

# b is only 12 bits long
# q = p + 42*b**(bitsize//12) + 17*b**(bitsize//24) + 42*b + 1337
# n = p*q
# n = p**2 + p*(42*b**(bitsize//12) + 17*b**(bitsize//24) + 42*b + 1337)
# Quadratic with:
#   a = 1
#   b = (42*b**(bitsize//12)
#   c = 17*b**(bitsize//24) + 42*b + 1337)
# b is unknown but small and easily bruteforcable

bitsize = 384
def calc_value(b):
    return 42*b**(bitsize//12) + 17*b**(bitsize//24) + 42*b + 1337

def solve_quadratic(a, b, c):
    # solve a*x^2 + b*x + c = 0
    D = b**2 - 4*a*c
    Droot, check = iroot(D, 2)
    if not check:
        return None
    sol = (-b + Droot)//(2*a)
    return sol

i = 2**11
while i < 2**12:
    i = next_prime(i)
    sol = solve_quadratic(1, calc_value(i), -n)
    if sol != None:
        print(f"success, b = {i}")
        p = sol
        q = n//p
        d = pow(65537, -1, (p - 1)*(q - 1))
        print(long_to_bytes(pow(c, d, n)))
