import sys
from random import randint


class Node():

    def __init__(self, key: int, priority: int):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None


class Treap():

    @staticmethod
    def get_priotiry():
        return randint(1, 2 ** 64)

    def __init__(self):
        self.root = None

    def split(self, v, key):
        if v is None:
            return None, None
        if v.key > key:
            t1, t2 = self.split(v.left, key)
            v.left = t2
            return t1, v
        else:
            t1, t2 = self.split(v.right, key)
            v.right = t1
            return v, t2

    def merge(self, t1, t2):
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        elif t1.priority > t2.priority:
            t1.right = self.merge(t1.right, t2)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            return t2

    def insert(self, key) -> Node:
        new_node = Node(key, self.get_priotiry())
        if self.root is None:
            self.root = new_node
        else:
            t1, t2 = self.split(self.root, key - 1)
            self.root = self.merge(t1, new_node)
            self.root = self.merge(self.root, t2)

    def delete(self, key: int) -> Node:
        t1, t2 = self.split(self.root, key)
        t11, t12 = self.split(t1, key - 1)
        self.root = self.merge(t11, t2)


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


tree = Treap()
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(3)
tree.insert(13)
tree.insert(9)
print(next(tree.root, 5))
print(prev(tree.root, 7))
#display(tree.root)
tree.delete(6)
print(next(tree.root, 5))
print(prev(tree.root, 7))

#display(tree.root)
