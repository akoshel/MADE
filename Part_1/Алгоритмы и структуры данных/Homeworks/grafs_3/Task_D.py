import sys


class Disjoint:

    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.dist = [1 for _ in range(n)]

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


def main() -> None:
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    edges = []
    for _ in range(m):
        i, j, w = list(map(int, sys.stdin.readline().split(' ')))
        if i != j:
            edges.append([w, i - 1, j - 1])
    edges = sorted(edges)
    snm = Disjoint(n)
    dist = 0
    for w, i, j in edges:
        if snm.get(i) != snm.get(j):
            dist += w
            snm.join(i, j)
    sys.stdout.write(str(dist))

if __name__ == '__main__':
    main()
