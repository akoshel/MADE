import sys
import math

def get_a(a1: int, n:int) -> list:
    """Returns a"""
    K1 = 23
    K2 = 21563
    K3 = 16714589
    a_prev = a1
    a_list = [a1]
    for _ in range(n - 1):
        a_list.append((K1 * a_prev + K2) % K3)
    return a_list

def sparse_matrix(n: int, a: list):
    #a = get_a_value(a1, n)
    l = 0
    k = 1
    min_a = [a]
    while 2**k < n - 1:
        l = 0
        temp_min = [a[l]]
        while l + (2 ** (k - 1)) < n - 1:
            v = min(min_a[k - 1][l], min_a[k - 1][l + (2 ** (k - 1))])
            temp_min.append(v)
            l += 1
        min_a.append(temp_min)
        k += 1
    return min_a


def query(L, R, lookup):
    # Find highest power of 2 that is smaller
    # than or equal to count of elements in
    # given range. For [2, 10], j = 3
    j = int(math.log2(R - L + 1))

    # Compute minimum of last 2^j elements
    # with first 2^j elements in range.
    # For [2, 10], we compare arr[lookup[0][3]]
    # and arr[lookup[3][3]],
    if lookup[L][j] <= lookup[R - (1 << j) + 1][j]:
        return lookup[L][j]

    else:
        return lookup[R - (1 << j) + 1][j]


a = [1, 2, 3, 4, 5, 6, 7, 8]
mins = sparse_matrix(8, a)
print(mins)
print(query(4, 5, mins))