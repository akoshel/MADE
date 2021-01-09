import sys


class Disjoint:

    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.min = [i for i in range(n)]
        self.max = [i for i in range(n)]
        self.cnt = [1 for _ in range(n)]

    def get(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        min_x, max_x, cnt_x = self.min[x], self.max[x], self.cnt[x]
        min_y, max_y, cnt_y = self.min[y], self.max[y], self.cnt[y]

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parent[x] = y
        self.min[y] = min(min_x, min_y)
        self.max[y] = max(max_x, max_y)
        self.cnt[y] = cnt_x + cnt_y


def main() -> None:
    n = int(sys.stdin.readline())
    snm = Disjoint(n)
    while True:
        cmd = sys.stdin.readline().split(' ')
        if cmd[0] == 'union':
            snm.join(int(cmd[1]) - 1, int(cmd[2]) - 1)
            print(snm.parent)
        elif cmd[0] == 'get':
            x = snm.get(int(cmd[1]) - 1)
            sys.stdout.write(str(snm.min[x] + 1) + ' ')
            sys.stdout.write(str(snm.max[x] + 1) + ' ')
            sys.stdout.write(str(snm.cnt[x]) + '\n')
        else:
            break


if __name__ == '__main__':
    main()
