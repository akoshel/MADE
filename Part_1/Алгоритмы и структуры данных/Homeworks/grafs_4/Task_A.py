import sys
import threading


def pushflow(cost, v, t, curflow, used, flow):
    used[v] = True
    if v == t:
        return curflow
    for u, c in enumerate(cost[v]):
        if not used[u] and flow[v][u] < c:
            nextflow = min(curflow, c - flow[v][u])
            delta = pushflow(cost, u, t, nextflow, used, flow)
            if delta > 0:
                flow[u][v] -= delta
                flow[v][u] += delta
                return delta
    return 0


def main() -> None:
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    flow = {i: [0] * n for i in range(n)}
    cost = {i: [0] * n for i in range(n)}
    for _ in range(m):
        a, b, c = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        cost[a][b] += c
        cost[b][a] += c
    ans = 0
    while True:
        used = {i: False for i in range(n)}
        delta = pushflow(cost, 0, n - 1, 20, used, flow)
        if delta > 0:
            ans += delta
        else:
            break
    print(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()