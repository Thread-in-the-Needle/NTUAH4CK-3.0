vals = [46096, 29310, 35786, 34250, 1682, 11703, 61757, 3732, 9259, 35900, 51157, 33143, 711, 15574, 10828, 33537, 40680, 50187, 18386, 31483]
finals = [13660, 20137, 19784, 1306, 978, 10684, 36366, 1167, 6038, 4071, 28503, 2856, 363, 1268, 7100, 9711, 21216, 17029, 17033, 25654]
flag = []

def op(x, i):
    x = x ^ 0x1337
    t = 0xdead
    x = (x * t) >> 4
    t = vals[i]
    x %= t
    return x    

for i in range(20):
    for b in range(0xff):
        if op(b, i) == finals[i]:
            flag.append(b)
            break
print(bytes(flag).decode())