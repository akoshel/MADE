import sys


def dijkstra(n, s, graph):
    d = {i: float('Inf') for i in range(n)}
    used = {i: False for i in range(n)}
    d[s] = 0
    for _ in range(n):
        next_e = -1
        for v in range(n):
            if next_e == -1 or (d[v] < d[next_e] and not used[v]):
                next_e = v
        if d[next_e] == float('Inf'):
            break
        used[next_e] = True
        for w, u in graph[next_e]:
            d[u] = min(d[u], d[next_e] + w)
    return d


def main() -> None:
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    smezh_list = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        smezh_list[a].append((w, b))
        smezh_list[b].append((w, a))
    #for i in range(n):
    d = dijkstra(n, 4, smezh_list)
     #   sys.stdout.write(str(d[0]) + ' ')
    print(d)


if __name__ == '__main__':
    main()
