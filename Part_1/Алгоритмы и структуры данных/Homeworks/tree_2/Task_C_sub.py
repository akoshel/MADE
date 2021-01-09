import sys
from random import randint


class Node():

    def __init__(self, key: int, priority: int):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.size = 1


class ImplicitTreap():

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

    def swap_elements(self, pos1: int, pos2: int):
        t1, t2 = self.split(self.root, pos1)
        t11, t12 = self.split(t1, pos1 - 1)
        key1 = t12.key
        t1 = self.merge(t11, t12)
        self.root = self.merge(t1, t2)

        t1, t2 = self.split(self.root, pos2)
        t11, t12 = self.split(t1, pos2 - 1)
        key2 = t12.key
        t12.key = key1
        t1 = self.merge(t11, t12)
        self.root = self.merge(t1, t2)

        t1, t2 = self.split(self.root, pos1)
        t11, t12 = self.split(t1, pos1 - 1)
        t12.key = key2
        t1 = self.merge(t11, t12)
        self.root = self.merge(t1, t2)


def get_size(root):
    if root is None:
        return 0
    else:
        return root.size


def get_answer(root: Node):
    if root:
        get_answer(root.left)
        sys.stdout.write(str(root.key) + ' ')
        get_answer(root.right)



def main() -> None:
    tree = ImplicitTreap()
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    for i in range(n):
        tree.insert(i + 1, i)
    for _ in range(m):
        pos1, pos2 = list(map(int, sys.stdin.readline().split(' ')))
        tree.swap_elements(pos1 - 1, pos2 - 1)
    get_answer(tree.root)

if __name__ == '__main__':
    main()
