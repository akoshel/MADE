import sys


def update_bit(fenw_tree: list, n: int, i: int, v: int) -> list:
    i += 1
    while i <= n:
        fenw_tree[i] += v
        i += i & (-i)
    return fenw_tree


def build_tree(arr: list, n: int) -> list:
    fenw_tree = [0] * (n + 1)
    for i in range(n):
        fenw_tree = update_bit(fenw_tree, n, i, arr[i])
    return fenw_tree


def get_sum(fenw_tree: list, i: int) -> int:
    s = 0
    i = i + 1
    while i > 0:
        s += fenw_tree[i]
        i -= i & (-i)
    return s


def set_value(arr: list, fenw_tree: list, n: int, i: int, v:int) -> (list, list):
    update_value = v - arr[i]
    arr[i] = v
    fenw_tree = update_bit(fenw_tree, n, i, update_value)
    return arr, fenw_tree


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))
fenw_tree = build_tree(arr, len(arr))
for _ in range(1000000):
    inp = sys.stdin.readline().split(' ')
    if inp[0] == 'sum':
        if int(inp[1]) == 1:
            sys.stdout.write(str(get_sum(fenw_tree, int(inp[2]) - 1)) + '\n')
        else:
            sys.stdout.write(str(get_sum(fenw_tree, int(inp[2]) - 1) - get_sum(fenw_tree, int(inp[1]) - 2)) + '\n')
    elif inp[0] == 'set':
        arr, fenw_tree = set_value(arr, fenw_tree, n, int(inp[1]) - 1, int(inp[2]))
    else:
        break