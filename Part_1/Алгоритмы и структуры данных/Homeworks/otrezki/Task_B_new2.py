import sys


def get_sparse_table(arr: int, n: int):
    min_matrix = []
    i = 0
    while i < n:
        j = 1
        min_matrix.append([arr[i]])
        while 1 << j < n:
            min_matrix[i].append(None)
            j += 1
        i += 1
    j = 1
    while (1 << j) <= n:
        i = 0
        while (i + (1 << j) - 1) < n:
            min_matrix[i][j] = min(min_matrix[i][j - 1], min_matrix[i + (1 << (j - 1))][j - 1])
            i += 1
        j += 1
    return min_matrix


def get_min(l: int, r: int, min_matrix: list, arr: list):
    if l == r:
        return arr[l]
    j = 0
    while 1 << j < r - l + 1:
        j += 1
    j -= 1
    return min(min_matrix[l][j], min_matrix[r - (1 << j) + 1][j])


def get_a(a1: int, n: int) -> list:
    """Returns a"""
    K1 = 23
    K2 = 21563
    K3 = 16714589
    a_prev = a1
    a_list = [a1]
    for _ in range(n - 1):
        temp_val = (K1 * a_prev + K2) % K3
        a_list.append(temp_val)
        a_prev = temp_val
    return a_list


def get_u(u_prev: int, n: int, r: int, i: int) -> int:
    """Returns u"""
    K1 = 17
    K2 = 751
    K3 = 2
    return ((K1 * u_prev + K2 + r + K3 * i) % n) + 1


def get_v(v_prev: int, n: int, r: int, i: int) -> int:
    """Returns v"""
    K1 = 13
    K2 = 593
    K3 = 5
    return ((K1 * v_prev + K2 + r + K3 * i) % n) + 1


n, m, a1 = list(map(int, sys.stdin.readline().split(' ')))
u, v = list(map(int, sys.stdin.readline().split(' ')))
arr = get_a(a1, n)
min_matrix = get_sparse_table(arr, n)

for i in range(1, m + 1):
    res = get_min(min(u, v) - 1, max(u, v) - 1, min_matrix, arr)
    if i < m:
        u = get_u(u, n, res, i)
        v = get_v(v, n, res, i)
    else:
        sys.stdout.write(str(u) + ' ')
        sys.stdout.write(str(v) + ' ')
        sys.stdout.write(str(res))

