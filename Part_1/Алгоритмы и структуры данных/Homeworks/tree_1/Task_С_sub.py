import sys


class Node:
    """Binary tree node"""

    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1


def balance_tree(root: Node):
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    if get_balance(root) > 1:
        if get_balance(root.right) < 0:
            root.right = rotate_right(root.right)
        root = rotate_left(root)

    if get_balance(root) < -1:
        if get_balance(root.right) > 0:
            root.left = rotate_left(root.left)
        root = rotate_right(root)
    return root


def insert(root: Node, key: int):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)

    return balance_tree(root)


def delete(root: Node, key: int):
    """Remove key from tree"""
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        q = root.left
        r = root.right
        if not r:
            return q
        root_min = findmin(r)
        root_min.right = remove_min(r)
        root_min.left = q
        return balance_tree(root_min)
    return balance_tree(root)


def findmin(root: Node):
    while root.left is not None:
        root = root.left
    return root


def remove_min(root: Node):
    if root.left is None:
        return root.right
    root.left = remove_min(root.left)
    return balance_tree(root)


def rotate_left(q: Node):
    p = q.right
    temp = p.left
    p.left = q
    q.right = temp
    q.height = 1 + max(get_height(q.left), get_height(q.right))  # fix height
    p.height = 1 + max(get_height(p.left), get_height(p.right))  # fix height
    return p


def rotate_right(p):
    q = p.left
    temp = q.right
    q.right = p
    p.left = temp
    p.height = 1 + max(get_height(p.left), get_height(p.right))  # fix height
    q.height = 1 + max(get_height(q.left), get_height(q.right))  # fix height
    return q


def get_balance(root):
    if not root:
        return 0
    return get_height(root.right) - get_height(root.left)


def get_height(root):
    if not root:
        return 0
    return root.height


def prev(root: Node, key: int):
    cur_root = root
    res = None
    while cur_root is not None:
        if cur_root.key < key:
            res = cur_root.key
            cur_root = cur_root.right
        else:
            cur_root = cur_root.left
    return res


def findmax(root: Node):
    while root.right is not None:
        root = root.right
    return root.key


def find_k_max(root: Node, k: int) -> int:
    max_key = findmax(root)
    if k < 2:
        return max_key
    for _ in range(k - 1):
        max_key = prev(root, max_key)
    return max_key


tree = None
n = int(sys.stdin.readline())
for _ in range(n):
    inp = sys.stdin.readline().split(' ')
    if int(inp[0]) == 1:
        tree = insert(tree, int(inp[1].strip()))
    elif int(inp[0]) == -1:
        tree = delete(tree, int(inp[1].strip()))
    elif int(inp[0]) == 0:
        k_max = find_k_max(tree, int(inp[1].strip()))
        sys.stdout.write(str(k_max) + '\n')
    else:
        pass