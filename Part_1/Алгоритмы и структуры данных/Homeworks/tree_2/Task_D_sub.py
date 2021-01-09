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

    def move_elements(self, pos1: int, pos2: int) -> Node:
        if pos1 == pos2:
            return
        elif pos2 > pos1:
            max_pos = pos2
            min_pos = pos1
        else:
            max_pos = pos1
            min_pos = pos2

        t1, t2 = self.split(self.root, max_pos)
        t11, t12 = self.split(t1, min_pos - 1)
        t21 = t12
        nodes_to_reverse = []
        for i in range(max_pos - min_pos - 1, -1, -1):
            t21, t22 = self.split(t21, i)
            nodes_to_reverse.append(t22)

        t12 = nodes_to_reverse[0]
        for node in nodes_to_reverse[1:]:
            t12 = self.merge(t12, node)
        t12 = self.merge(t12, t21)
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
        tree.move_elements(pos1 - 1, pos2 - 1)
    get_answer(tree.root)

if __name__ == '__main__':
    main()
