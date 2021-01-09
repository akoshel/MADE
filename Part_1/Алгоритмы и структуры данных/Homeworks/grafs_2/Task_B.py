import sys
from collections import de

def dijkstra(graph, start, n):
    dist = {i: float('Inf') for i in range(n)}
    dist[start] = 0
    used = {i: False for i in range(n)}
    queue = set()
    queue.add((0, start))
    for _ in range(n):
        if len(queue) == 0:
            break
        min_pair = min(queue)
        next_e = min_pair[1]
        queue.remove(min_pair)
        used[next_e] = True
        for w, u in graph[next_e]:
            if dist[u] > dist[next_e] + w:
                try:
                    queue.remove((dist[u], u))
                except KeyError:
                    pass
            dist[u] = min(dist[u], dist[next_e] + w)
            queue.add((dist[u], u))
    return dist


def main() -> None:
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    smezh_list = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        smezh_list[a].append((w, b))
        smezh_list[b].append((w, a))
    for i in range(n):
        d = dijkstra(smezh_list, i, n)
        #sys.stdout.write(str(d[0]) + ' ')
        print(d)

if __name__ == '__main__':
    main()
