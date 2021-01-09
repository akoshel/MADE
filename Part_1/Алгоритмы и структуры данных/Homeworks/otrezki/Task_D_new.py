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


def RMQUtil(st, ss, se, qs, qe, index):
    # If segment of this node is a part
    # of given range, then return
    # the min of the segment
    if (qs <= ss and qe >= se):
        return st[index];

        # If segment of this node
    # is outside the given range
    if (se < qs or ss > qe):
        return float('Inf')

        # If a part of this segment
    # overlaps with the given range
    mid = ss + (se - ss) // 2
    return min(RMQUtil(st, ss, mid, qs,
                          qe, 2 * index + 1),
                  RMQUtil(st, mid + 1, se,
                          qs, qe, 2 * index + 2))

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    n = len(a)
    tree = build_tree(a)
    print(rmq(tree, 1, 4))
    tree = updateTreeNode(tree, 2, 1)
    print(rmq(tree, 1, 3))
    print(RMQUtil(tree, 0, 4, 2, 4, 0))