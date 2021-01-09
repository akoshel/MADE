from random import randint
list_lenght = int(input())
raw_list = list(map(int, input().split(' ')))
assert(len(raw_list) == list_lenght)


def quick_sort_step(input_list, l, r):
    ind = randint(l+1, r)
    x = input_list[ind]
    input_list[ind], input_list[l] = input_list[l], input_list[ind]
    i = l
    ll = l
    h = r
    for j in range(l, r+1):
        if input_list[j] < x:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
        elif input_list[i] > x:
            input_list[i], input_list[h] = input_list[h], input_list[i]
            h -= 1
        else:
            i += 1
    input_list[l], input_list[i] = input_list[i], input_list[l]
    return i


def partition3(A, l, r):

    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l  # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[
        l]  # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
    # in the quick_sort function.
    while i <= gt:  # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    return lt, gt

def quick_sort1(init_list, l, r):
    if l < r:
        n = partition3(init_list, l, r)
        quick_sort(init_list, l, n - 1)
        quick_sort(init_list, n + 1, r)
    else:
        return init_list


def quick_sort(A, l, r):

    if l >= r:
        return
    k = randint(l, r)
    A[k], A[l] = A[l], A[k]

    lt, gt = partition3(A, l, r)
    quick_sort(A, l, lt - 1)
    quick_sort(A, gt + 1, r)

quick_sort(raw_list, 0, len(raw_list)-1)
print(' '.join(list(map(str, raw_list))))
