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


class Disjoint:

    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.clan = [[i] for i in range(n)]
        self.exp = [0 for _ in range(n)]

    def get(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parent[x] = y
        self.clan[y].extend(self.clan[x])
        self.clan[x] = []

    def add(self, x, v):
        x = self.get(x)
        for gamer in self.clan[x]:
            self.exp[gamer] += v


def main() -> None:
    stdin, stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    n, m = map(int, stdin.readline().split(' '))
    snm = Disjoint(n)
    for _ in range(m):
        cmd = stdin.readline().split(' ')
        if cmd[0] == 'join':
            snm.join(int(cmd[1]) - 1, int(cmd[2]) - 1)
        elif cmd[0] == 'get':
            stdout.write(str(snm.exp[int(cmd[1]) - 1]) + '\n')
        else:
            snm.add(int(cmd[1]) - 1, int(cmd[2]))


if __name__ == '__main__':
    main()
