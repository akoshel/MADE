import sys


def bfs(graph, start, end, used):
    d = {start: start}
    queue = [start]
    used[start] = True
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if not used[u]:
                used[u] = True
                queue.append(u)
                d[u] = v
                if u == end:
                    return d


def get_horse_moves(i, j, n):
    result = []
    possible_moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
    for move in possible_moves:
        i_new = i + move[0]
        j_new = j + move[1]
        if 0 <= i_new < n and 0 <= j_new < n:
            k = i_new * n + j_new
            result.append(k)
    return result


def main() -> None:
    n = int(sys.stdin.readline())
    start_i, start_j = list(map(int, sys.stdin.readline().split(' ')))
    end_i, end_j = list(map(int, sys.stdin.readline().split(' ')))
    start = (start_i - 1) * n + (start_j - 1)
    end = (end_i - 1) * n + (end_j - 1)
    k = -1
    smezh_list = [[] for _ in range(n ** 2)]
    for i in range(n):
        for j in range(n):
            k += 1
            smezh_list[k] = get_horse_moves(i, j, n)

    used = {i: False for i in range(n ** 2)}
    hist_dict = bfs(smezh_list, start, end, used)
    ans = []
    k = end
    while k != start:
        ans.append((int(k / n), k % n))
        k = hist_dict[k]
    ans.append((int(start / n), start % n))

    sys.stdout.write(str(len(ans)) + '\n')
    for a in reversed(ans):
        sys.stdout.write(f'{a[0] + 1} {a[1] + 1}' + '\n')


if __name__ == '__main__':
    main()
