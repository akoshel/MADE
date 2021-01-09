import sys

def floyd(d, n):
    graph = d[:]
    next_v = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            next_v[i][j] = j
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if graph[u][v] > graph[u][k] + graph[k][v]:
                    graph[u][v] = graph[u][k] + graph[k][v]
                    next_v[u][v] = next_v[u][k]
    return next_v, graph


def main() -> None:
    n = int(sys.stdin.readline())
    smezh_matrix = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split(' ')))
        row = [float('Inf') if x == 100000 else x for x in row]
        smezh_matrix.append(row)
    next_v, d = floyd(smezh_matrix, n)
    cycle_flag = False
    for i in range(n):
        if d[i][i] < 0:
            cycle_flag = True
            start = i
            break
    if not cycle_flag:
        sys.stdout.write('NO' + '\n')
    else:
        sys.stdout.write('YES' + '\n')
        cur = next_v[start][start]
        ans = [cur]
        while cur != start:
            cur = next_v[cur][start]
            if cur in ans:
                start = cur
                cur = next_v[start][start]
                ans = [cur]
            else:
                ans.append(cur)


        sys.stdout.write(str(len(ans)) + '\n')
        for a in (ans):
            sys.stdout.write(str(a + 1) + ' ')


if __name__ == '__main__':
    main()
