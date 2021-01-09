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


def main() -> None:
    tree = Treap()
    for _ in range(100000):
        inp = sys.stdin.readline().split(' ')
        if inp[0] == 'insert':
            tree.insert(int(inp[1]))
        elif inp[0] == 'delete':
            tree.delete(int(inp[1]))
        elif inp[0] == 'exists':
            sys.stdout.write(str(exists(tree.root, int(inp[1]))).lower() + '\n')
        elif inp[0] == 'next':
            sys.stdout.write(str(next(tree.root, int(inp[1]))).lower() + '\n')
        elif inp[0] == 'prev':
            sys.stdout.write(str(prev(tree.root, int(inp[1]))).lower() + '\n')
        else:
            break

if __name__ == '__main__':
    main()
