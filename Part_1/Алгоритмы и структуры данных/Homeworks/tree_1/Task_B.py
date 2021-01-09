import sys


class Node:
    """Binary tree node"""

    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1


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

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1 and key < root.left.key:
        root = rotate_right(root)

    if balance < -1 and key > root.right.key:
        root = rotate_left(root)

    if balance > 1 and key > root.left.key:  # big rotate left
        root.left = rotate_left(root.left)
        root = rotate_right(root)

    if balance < -1 and key < root.right.key:  # big rotate right
        root.right = rotate_right(root.right)
        root = rotate_left(root)
    return root


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

    root.height = 1 + max(get_height(root.left),
                          get_height(root.right))

    balance = get_balance(root)
    if balance > 1 and key < root.left.key:
        root = rotate_right(root)

    if balance < -1 and key > root.right.key:
        root = rotate_left(root)

    if balance > 1 and key > root.left.key:  # big rotate left
        root.left = rotate_left(root.left)
        root = rotate_right(root)

    if balance < -1 and key < root.right.key:  # big rotate right
        root.right = rotate_right(root.right)
        root = rotate_left(root)
    return root

def findmax(root: Node):
    while root.right is not None:
        root = root.right
    return root


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
    return get_height(root.left) - get_height(root.right)


def get_height(root):
    if not root:
        return 0
    return root.height


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.key, root.height)
        inorder(root.right)

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


tree = None

for _ in range(10000):
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