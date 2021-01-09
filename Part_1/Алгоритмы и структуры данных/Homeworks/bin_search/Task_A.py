in1 = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
search_vals = list(map(int, input().split(' ')))

def bin_search(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = int((l + r) / 2)
        if a[m] == x:
            return x
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    if l == 0:
        return a[l]
    elif l == len(a):
        return a[l-1]
    elif a[l] - x < x - a[l-1]:
        return a[l]
    else:
        return a[l-1]


for val in search_vals:
    print(bin_search(a, val))
