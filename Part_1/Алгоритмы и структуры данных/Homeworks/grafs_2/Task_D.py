import sys
import threading

def dfs(smezh_list, v, used, inv_used):
    used[v] = True
    inv_used[v] = False
    for u, _ in smezh_list[v]:
        if not used[u]:
            dfs(smezh_list, u, used, inv_used)


def main() -> None:
    n, m, s = list(map(int, sys.stdin.readline().split(' ')))
    s -= 1
    smezh_list = [[] for _ in range(n)]
    edges_list = []
    for _ in range(m):
        a, b, w = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        smezh_list[a].append([b, w])
        edges_list.append([a, b, w])

    distances = {i: float('Inf') for i in range(n)}
    distances[s] = 0
    for _ in range(n):
        for u, v, w in edges_list:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    inv_used = {i: True for i in range(n)}
    used = {i: False for i in range(n)}
    for u, v, w in edges_list:
        if distances[v] > distances[u] + w:
            dfs(smezh_list, v, used, inv_used)

    for k, v in distances.items():
        if v == float('Inf'):
            sys.stdout.write('*' + '\n')
        elif not inv_used[k]:
            sys.stdout.write('-' + '\n')
        else:
            sys.stdout.write(str(v) + '\n')


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()
