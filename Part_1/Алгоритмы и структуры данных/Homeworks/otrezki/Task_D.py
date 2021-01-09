import sys

def build_tree(arr):
    tree = [0] * (2 * 10000)
    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[i << 1], tree[i << 1 | 1])
    return tree


def updateTreeNode(tree, p, value):
    tree[p + n] = value
    p = p + n
    i = p
    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1
    return tree

def rmq(tree, l, r):
    res = float('Inf')
    l += n
    r += n
    while l < r:
        if (l & 1):
            res = min(tree[l], res)
            l += 1
        if (r & 1):
            r -= 1
            res = min(tree[r], res)
        l >>= 1
        r >>= 1
    return res


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5];

    # n is global
    n = len(a)

    # build tree
    tree = build_tree(a)

    # print the sum in range(1,2) index-based
    print(query(tree, 1, 4))

    # modify element at 2nd index
    tree = updateTreeNode(tree, 2, 1)

    # print the sum in range(1,2) index-based
    print(rmq(tree, 1, 3));