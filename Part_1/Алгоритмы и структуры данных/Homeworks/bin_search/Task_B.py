import sys
def lower_bound(arr, x):
    l = -1
    r = len(arr)
    while l < r - 1:
        m = (l + r) // 2
        if x <= arr[m]:
            r = m
        else:
            l = m
    return r

def upper_bound(arr, x):
    l = -1
    r = len(arr)
    while l < r - 1:
        m = (l + r) // 2
        if x >= arr[m]:
            l = m
        else:
            r = m
    return r

in1 = int(sys.stdin.readline())
input_array = list(map(int, sys.stdin.readline().split(' ')))
sorted_array = sorted(input_array)
for i in range(int(sys.stdin.readline())):
    bounds = list(map(int, sys.stdin.readline().split(' ')))
    print(upper_bound(sorted_array, bounds[1]) - lower_bound(sorted_array, bounds[0]))


