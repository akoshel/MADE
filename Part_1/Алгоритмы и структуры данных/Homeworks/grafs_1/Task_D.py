import sys
import threading

def conn_comps(smezh_list, v, cur, color):
    color[v] = cur
    for u in smezh_list[v]:
        if color[u] == 0:
            conn_comps(smezh_list, u, cur, color)


def topology_sort(smezh_list, v, used, result):
    used[v] = True
    for u in smezh_list[v]:
        if not used[u]:
            topology_sort(smezh_list, u, used, result)
    result.append(v)


def main() -> None:
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    smezh_list = [[] for _ in range(n)]
    smezh_list_obr = [[] for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        smezh_list[a].append(b)
        smezh_list_obr[b].append(a)

    used = {i: False for i in range(n)}
    result = []
    for v in range(n):
        if not used[v]:
            topology_sort(smezh_list, v, used, result)

    color = {i: 0 for i in range(n)}
    cnt = 0
    for v in reversed(result):
        if color[v] == 0:
            cnt += 1
            conn_comps(smezh_list_obr, v, cnt, color)

    ans_set = set()
    for v, targets in enumerate(smezh_list):
        for u in targets:
            if color[v] != color[u]:
                ans_set.add((color[v], color[u]))
    sys.stdout.write(str(len(ans_set)))



if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()


