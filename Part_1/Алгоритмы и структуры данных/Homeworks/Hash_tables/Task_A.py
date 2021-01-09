import sys
import fileinput

import sys
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



def hash_func(value, size):
    P = 5000011
    return ((1467 * value) % P) % size


class Set:

    def __init__(self):
        self.SIZE = 1000003
        self.table = [None] * self.SIZE
        self.rip_cnt = 0

    def insert(self, value):
        hash_key = hash_func(value, self.SIZE)
        while True:
            if self.table[hash_key] == value:
                return
            if hash_key < self.SIZE - 1:
                hash_key += 1
            else:
                hash_key = 0
            if self.table[hash_key] == None:
                self.table[hash_key] = value
                return
            elif self.table[hash_key] == 'rip':
                self.rip_cnt -= 1
                self.table[hash_key] = value
                return

    def delete(self, value):
        hash_key = hash_func(value, self.SIZE)
        while True:
            if self.table[hash_key] == value:
                self.rip_cnt += 1
                self.table[hash_key] = 'rip'
                if self.rip_cnt > self.SIZE / 100:
                    self.rebuild_table()
                return
            if hash_key < self.SIZE - 1:
                hash_key += 1
            else:
                hash_key = 0
            if self.table[hash_key] == None:
                return

    def contains(self, value):
        hash_key = hash_func(value, self.SIZE)
        while True:
            if self.table[hash_key] == value:
                return sys.stdout.write('true' + '\n')
            if hash_key < self.SIZE - 1:
                hash_key += 1
            else:
                hash_key = 0
            if self.table[hash_key] == None:
                return sys.stdout.write('false' + '\n')

    def rebuild_table(self):
        old_table = self.table
        self.table = [None] * self.SIZE
        for value in old_table:
            if value == None:
                continue
            elif value == 'rip':
                continue
            else:
                self.insert(value)
        self.rip_cnt = 0


my_set = Set()
stdin, stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

for inp in stdin:
    inp = inp.split(' ')
    if inp[0] == 'insert':
        my_set.insert(int(inp[1]))
    elif inp[0] == 'delete':
        my_set.delete(int(inp[1]))
    else:
        my_set.contains(int(inp[1]))
