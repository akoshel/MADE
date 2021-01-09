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
    def __init__(self, key, value):
        self.key = key
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
            nodes.append((node.key, node.value))
            node = node.next
        nodes.append(None)
        return ('->'.join(list(map(str, nodes))))

    def add_last(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            self.size = 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def remove_node(self, target_key):
        if self.head.key == target_key:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
                self.size = 0
            return
        previous_node = self.head
        node = self.head
        while node.next != None:
            node = node.next
            if node.key == target_key:
                previous_node.next = node.next
                if node.next == None:
                    self.tail = previous_node
                self.size -= 1
                return
            previous_node = node
        return

def str_hash_func(value, size):
    P = 999983
    A = 97
    a_pow = 97
    res = 0
    for i, symbol in enumerate(reversed(value)):
        res = ((ord(symbol) * a_pow) % P + res) % P
        a_pow = (a_pow * A) % P
    return res % size

class Map:

    def __init__(self):
        self.SIZE = 100003
        self.table = [LinkedList() for _ in range(self.SIZE)]

    def put(self, key, value):
        hash_key = str_hash_func(key, self.SIZE)
        if self.table[hash_key].head == None:
            self.table[hash_key].add_last(Node(key, value))
            return
        elif self.table[hash_key].head.key == key:
            self.table[hash_key].head.value = value
            return
        else:
            node = self.table[hash_key].head
            while node.next != None:
                node = node.next
                if node.key == key:
                    node.value = value
                    return
        self.table[hash_key].add_last(Node(key, value))


    def delete(self, key):
        hash_key = str_hash_func(key, self.SIZE)
        if self.table[hash_key].head == None:
            return
        else:
            self.table[hash_key].remove_node(key)
            return

    def get(self, key):
        hash_key = str_hash_func(key, self.SIZE)
        if self.table[hash_key].head == None:
            return 'none'
        elif self.table[hash_key].head.key == key:
            return str(self.table[hash_key].head.value)
        else:
            node = self.table[hash_key].head
            while node.next != None:
                node = node.next
                if node.key == key:
                    return str(node.value)
            return 'none'


def main() -> None:
    my_map = Map()
    stdin, stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

    for inp in stdin:
        inp = inp.split(' ')
        inp = [val.strip() for val in inp]
        if inp[0] == 'put':
            my_map.put(inp[1], inp[2])
        elif inp[0] == 'delete':
            my_map.delete(inp[1])
        elif inp[0] == 'get':
            stdout.write(my_map.get(inp[1]) + '\n')


if __name__ == '__main__':
    main()
