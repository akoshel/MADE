list_lenght = int(input())
raw_list = list(map(int, input().split(' ')))
assert(len(raw_list) == list_lenght)

def merge_sort_step(a, b):
    c = []
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    while i + j < n + m:
        if j == m or (i < n and a[i] <= b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            global k
            k += (n-i)
            j += 1
    return c


def merge_sort(init_list, k=0):
    if len(init_list) > 1:
        n = int(len(init_list) / 2)
        a = init_list[:n]
        b = init_list[n:]
        a = merge_sort(a, k)
        b = merge_sort(b, k)
        return merge_sort_step(a, b)
    else:
        return init_list
k = 0
merge_sort(raw_list)
print(k)