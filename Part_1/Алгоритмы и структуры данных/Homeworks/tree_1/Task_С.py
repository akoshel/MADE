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


def exists(root: Node, key: int):
    """Search key to tree"""
    if root is None:
        return False
    else:
        if root.key == key:
            return True
        elif key < root.key:
            return exists(root.left, key)
        else:
            return exists(root.right, key)

def next(root: Node, key: int):
    cur_root = root
    res = None
    while cur_root is not None:
        if cur_root.key > key:
            res = cur_root.key
            cur_root = cur_root.left
        else:
            cur_root = cur_root.right
    return res

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

def display(tree):
    lines, *_ = _display_aux(tree)
    for line in lines:
        print(line)

def _display_aux(tree):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if tree.right is None and tree.left is None:
        line = '%s' % tree.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if tree.right is None:
        lines, n, p, x = _display_aux(tree.left)
        s = '%s' % tree.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if tree.left is None:
        lines, n, p, x = _display_aux(tree.right)
        s = '%s' % tree.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(tree.left)
    right, m, q, y = _display_aux(tree.right)
    s = '%s' % tree.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def findmax(root: Node):
    while root.right is not None:
        root = root.right
    return root.key

def find_k_max(root: Node, k:int):
    max_key = findmax(root)
    if k == 1:
        return max_key
    for _ in range(k - 1):
        max_key = prev(root, max_key)
        if max_key is None:
            return max_key
    return max_key


tree = None
tree = insert(tree, 2)
tree = insert(tree, 5)
tree = insert(tree, 1)
tree = insert(tree, 8)
tree = insert(tree, 7)

display(tree)
print(find_k_max(tree, 1))
print(find_k_max(tree, 2))
print(find_k_max(tree, 3))
print(find_k_max(tree, 4))
print(find_k_max(tree, 5))
print(find_k_max(tree, 6))
print(find_k_max(tree, 7))
