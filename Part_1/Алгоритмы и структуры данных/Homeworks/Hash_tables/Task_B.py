import sys
import fileinput
from io import IOBase, BytesIO
from os import read, write, fstat

BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, size: int = ...):
        while self.newlines == 0:
            b = read(self._fd, max(fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node != None:
            nodes.append(node.value)
            node = node.next
        nodes.append(None)
        return ('->'.join(list(map(str, nodes))))

    def add_last(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def remove_node(self, target_value):
        if self.head.value == target_value:
            self.head = self.head.next
            return
        previous_node = self.head
        node = self.head
        while node != None:
            node = node.next
            if node.value == target_value:
                if previous_node.next == self.tail:
                    self.tail = previous_node
                previous_node.next = node.next
                self.size -= 1
                return
            previous_node = node

def str_hash_func(value):
    p = 500009
    a = 17
    res = 0
    for i, symbol in enumerate(reversed(value)):
        res = (ord(symbol) * (a**i) % p + res) % p
    return res % 100003

class Map:

    def __init__(self):
        self.size = 100003
        self.table = []
        for ll in range(self.size):
            self.table.append(LinkedList())

    def put(self, key, value):
        hash_key = str_hash_func(key)
        self.table[hash_key].add_last(Node(key, value))

    def delete(self, value):
        hash_key = str_hash_func(value)
        self.table[hash_key].remove_node(value)

    def get(self, value):
        hash_key = str_hash_func(value)
        if self.table[hash_key].head == None:
            return sys.stdout.write('none' + '\n')
        elif self.table[hash_key].head.value == value:
            return sys.stdout.write(value + '\n')

        node = self.table[hash_key].head
        while node.next != None:
            node = node.next
            if node.value == value:
                return sys.stdout.write(value + '\n')
        return sys.stdout.write('none' + '\n')


my_map = Map()
stdin = fileinput.input()
#stdin, stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

for inp in stdin:
    inp = inp.replace('\n', '')
    inp = inp.split(' ')
    if inp[0] == 'put':
        for i in range(1, len(inp)):
            my_map.put(inp[i])
    elif inp[0] == 'delete':
        my_map.delete(inp[1])
    else:
        my_map.get(inp[1])