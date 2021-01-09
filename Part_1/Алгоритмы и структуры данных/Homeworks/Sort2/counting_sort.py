raw_list = list(map(int, input().split(' ')))

def count_sort(arr):
    count = [0 for i in range(101)]
    output = []
    for val in arr:
        count[val] += 1
    for i in range(len(count)):
        output += [i] * count[i]
    print(' '.join(list(map(str, output))))

count_sort(raw_list)