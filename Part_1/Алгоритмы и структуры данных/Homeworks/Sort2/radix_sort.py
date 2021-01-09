import string
def count_sort(indicies, lev, arr):
    letters = list(string.ascii_lowercase)
    count = {k: [] for k in letters}
    output_indicies = []
    # Складываем в словарь по буквам индексы
    for ind in indicies:
        if len(arr[ind]) < lev:
            count['a'].append(ind)
        else:
            count[arr[ind][-lev]].append(ind)
    # Собираем индексы в отсортированном порядке
    for vals in count.values():
        output_indicies += vals
    return output_indicies


def radixSort(inp_arr, k):
    indicies = [pos for pos in range(len(inp_arr))]
    for lev in range(k):
        indicies = count_sort(indicies, lev+1, inp_arr)
    return indicies


n, m, k = list(map(int, input().split(' ')))
inp_arr = []
for i in range(n):
    inp_arr.append(input())
inds = radixSort(inp_arr, k)
for ind in inds:
    print(inp_arr[ind])
