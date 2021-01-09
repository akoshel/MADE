import sys
from random import randint


class Node():

    def __init__(self, key: int, priority: int):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.size = 1


class Treap():

    @staticmethod
    def get_prioriry():
        return randint(1, 2 ** 64)

    @staticmethod
    def fix_size(root):
        size = get_size(root.left) + get_size(root.right) + 1
        return size

    def __init__(self):
        self.root = None

    def split(self, v, x):
        if v is None:
            return None, None
        if get_size(v.left) > x:
            t1, t2 = self.split(v.left, x)
            v.left = t2
            v.size = self.fix_size(v)
            return t1, v
        else:
            t1, t2 = self.split(v.right, x - get_size(v.left) - 1)
            v.right = t1
            v.size = self.fix_size(v)
            return v, t2

    def merge(self, t1, t2):
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        elif t1.priority > t2.priority:
            t1.right = self.merge(t1.right, t2)
            t1.size = self.fix_size(t1)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            t2.size = self.fix_size(t2)
            return t2

    def insert(self, key: int, pos: int):
        new_node = Node(key, self.get_prioriry())
        if self.root is None:
            self.root = new_node
        else:
            t1, t2 = self.split(self.root, pos - 1)
            self.root = self.merge(t1, new_node)
            self.root = self.merge(self.root, t2)

    def delete(self, pos: int):
        t1, t2 = self.split(self.root, pos)
        t11, t12 = self.split(t1, pos - 1)
        self.root = self.merge(t11, t2)


def get_size(root):
    if root is None:
        return 0
    else:
        return root.size


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

out_list = []
def inorder(root: Node):
    if root:
        inorder(root.left)
        out_list.append(root.key)
        inorder(root.right)

tree = Treap()
init_list = [1, 2, 4]
for i in range(len(init_list)):
    tree.insert(init_list[i], i)


tree.delete(2)

tree.insert(9, 0)
tree.insert(8, 3)
display(tree.root)

tree.delete(1
            )
out_list = []
inorder(tree.root)
print(out_list)

#print(out_list)
#