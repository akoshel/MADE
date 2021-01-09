import sys
import string
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


M = 999979
P = 47


def get_hash(l, r, hash_list, powp):
    if l == 0:
        return hash_list[r]
    return (hash_list[r] - (hash_list[l - 1] * powp[r - l + 1]) % M + M) % M


def main():
    stdin, stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    word = stdin.readline().strip()
    n = int(stdin.readline())
    hash_list = [None] * len(word)
    powp = [None] * len(word)
    hash_list[0] = ord(word[0])
    powp[0] = 1
    for i in range(1, len(word)):
        s = ord(word[i])
        hash_list[i] = ((hash_list[i - 1] * P) + s) % M
        powp[i] = (powp[i - 1] * P) % M

    for _ in range(n):
        a, b, c, d = map(int, stdin.readline().split(' '))
        sub_hash1 = get_hash(a - 1, b - 1, hash_list, powp)
        sub_hash2 = get_hash(c - 1, d - 1, hash_list, powp)
        if sub_hash1 == sub_hash2:
            stdout.write('Yes' + '\n')
        else:
            stdout.write('No' + '\n')


if __name__ == '__main__':
    main()
