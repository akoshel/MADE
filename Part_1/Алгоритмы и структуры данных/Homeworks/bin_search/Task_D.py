import sys

def search_rope_lenght(a, k_task):
    l = 0
    r = a[-1] + 2
    for i in range(300):
        m = (l + r) // 2
        if m == 0:
            return 0
        k = 0
        for rope in a:
            k += rope // m
        if k >= k_task:
            l = m
        else:
            r = m
    return m

n, k_task = list(map(int, sys.stdin.readline().split(' ')))
input_array = []
for i in range(n):
    input_array.append(int(sys.stdin.readline()))

sorted_array = sorted(input_array)
sys.stdout.write(str(search_rope_lenght(sorted_array, k_task)))
