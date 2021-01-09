import sys

class Node:
    """Binary tree node"""
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.key = key


def insert(root: Node, key: int):
    """Insert key to tree"""
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

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

def delete(root: Node, key: int):
    """Remove key from tree"""
    if root is None:
        return None
    else:
        if key < root.key:
            root.left = delete(root.left, key)
        elif key > root.key:
            root.right = delete(root.right, key)
        elif root.left is None and root.right is None:
            root = None
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            max_key = findmax(root.left)
            root.key = max_key.key
            root.left = delete(root.left, root.key)
    return root

def findmax(root: Node):
    while root.right is not None:
        root = root.right
    return root

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

tree = None

for _ in range(100):
    inp = sys.stdin.readline().split(' ')
    if inp[0] == 'insert':
        tree = insert(tree, int(inp[1]))
    elif inp[0] == 'delete':
        tree = delete(tree, int(inp[1]))
    elif inp[0] == 'exists':
        sys.stdout.write(str(exists(tree, int(inp[1]))).lower() + '\n')
    elif inp[0] == 'next':
        sys.stdout.write(str(next(tree, int(inp[1]))).lower() + '\n')
    elif inp[0] == 'prev':
        sys.stdout.write(str(prev(tree, int(inp[1]))).lower() + '\n')
    else:
        break


