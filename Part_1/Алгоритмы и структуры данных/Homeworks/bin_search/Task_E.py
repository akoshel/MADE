import sys

def time_counter(n, x, y):
    l = 0
    r = n * min(x, y)
    n -= 1
    t0 = min(x, y)
    for i in range(100):
        m = (l + r) // 2
        if int(m / x) + int(m / y) >= n:
            r = m
        else:
            l = m
    return(r + t0)

n, x, y = list(map(int, sys.stdin.readline().split(' ')))
sys.stdout.write(str(time_counter(n, x, y)))
