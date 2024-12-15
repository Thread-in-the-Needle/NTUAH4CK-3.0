from math import ceil

def optimal(arr:list[int],k:int) -> list[int]:
    n = len(arr)
    q = [(arr[i],i) for i in range(n)]
    res = []
    for i in range(n):
        x,j = q[i]
        res.append((ceil(x/k),j))
    res.sort(key = lambda x: x[0])
    return [x[1] for x in res]

def bf(arr:list[int],k:int) -> list[int]:
    n = len(arr)
    q = [(arr[i],i) for i in range(n)]
    res = []
    while q:
        x,i = q.pop(0)
        if x <=k:
            res.append(i)
        else:
            q.append((x-k,i))
    return res
