import sys


class NaiveTree:
    def __init__(self):
        self.root = set()

    def exists(self, x):
        return (x in self.root)

    def insert(self, x):
        self.root.add(x)

    def delete(self, x):
        if x in self.root:
            self.root.remove(x)

    def next(self, x):
        r = [y for y in self.root if y > x]
        return min(r) if r else None

    def prev(self, x):
        r = [y for y in self.root if y < x]
        return max(r) if r else None

tree = NaiveTree()
#print(tree.root)
for _ in range(100000):
    inp = sys.stdin.readline().split(' ')
    if inp[0] == 'insert':
        tree.insert(int(inp[1]))
    elif inp[0] == 'delete':
        tree.delete(int(inp[1]))
    elif inp[0] == 'exists':
        if tree.exists(int(inp[1])):
            print('true')
        else:
            print('false')
    elif inp[0] == 'next':
        out = tree.next(int(inp[1]))
        if out is None:
            print('none')
        else:
            print(out)
    elif inp[0] == 'prev':
        out = tree.prev(int(inp[1]))
        if out is None:
            print('none')
        else:
            print(out)
    else:
        break