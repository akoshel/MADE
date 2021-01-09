import sys
import threading


def conn_comps(smezh_list, v, cur, color):
    color[v] = cur
    for u in smezh_list[v]:
        if color[u] == 0:
            conn_comps(smezh_list, u, cur, color)


def main() -> None:
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    smezh_list = [[] for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        smezh_list[a].append(b)
        smezh_list[b].append(a)
    color = {i: 0 for i in range(n)}
    cnt = 0
    for v in range(n):
        if color[v] == 0:
            cnt += 1
            conn_comps(smezh_list, v, cnt, color)

    sys.stdout.write(str(max(color.values())) + '\n')
    for val in color.values():
        sys.stdout.write(str(val) + ' ')


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()


