import sys

def find_x(y, l, r):
    for i in range(100):
        m = (l + r) / 2
        if m**2 + m**0.5 < y:
            l = m
        else:
            r = m
    return r

y = float(sys.stdin.readline())
sys.stdout.write(str(find_x(y, 0, y)))

