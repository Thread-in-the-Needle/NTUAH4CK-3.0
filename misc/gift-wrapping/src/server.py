FLAG = 'NH4CK{h0_h0_h0_7h4nk5_f0r_y0ur_h3lp_!!!}'
from time import time
import random
from math import log,ceil
from hashlib import sha256
from json import loads,dumps
from random import SystemRandom
rng = SystemRandom()
def get_belt(seed:int, n:int) -> list[int]:   
    random.seed(seed)
    return [random.randint(1,n**2) for _ in range(n)]


def optimal(arr:list[int],k:int) -> list[int]:
    n = len(arr)
    q = [(arr[i],i) for i in range(n)]
    res = []
    for i in range(n):
        x,j = q[i]
        res.append((ceil(x/k),j))
    res.sort(key = lambda x: x[0])
    return [x[1] for x in res]


MAX_TIME = 4 # check this
def play(Ns:list[int]) -> bool:
    for n in Ns:
        max_val=n**2
        if n < 10**4:
            k = random.randint(1, int(max_val/log(max_val)))  
        else:
            k = random.randint(1, int(max_val/(log(max_val)**2)))
        
        seed = rng.randbytes(8)
        seed = int.from_bytes(seed, 'big')
        belt = get_belt(seed,n)
        print(dumps({'seed':seed,'n':n,'k':k}))
        
        t = time()
        sol = sha256(str(optimal(belt,k)).encode()).hexdigest()
        user_sol = loads(input())['sol_hash']
        t = time() - t

        res = {'msg':'Good job! 🎉🎉🎉'}
        if t > MAX_TIME:
            res['msg'] = 'Christmas is over 😢😢😢'
            print(dumps(res))
            return False
        if sol != user_sol:
            res['msg'] = 'Wrong answer 😢😢😢'
            print(dumps(res))
            return False
        print(dumps(res))
    return True

try:
    Ns=[10,100,1000]  + [10**4,10**5,10**6,10**6,10**6]
    if play(Ns):
        res = {'msg':'Congratulations! You saved Christmas 🎉🎉🎉','prize':FLAG}
        print(dumps(res))
except Exception as e:
    res = {'msg':'Something went wrong ⚠️⚠️⚠️','error':str(e)}

    


