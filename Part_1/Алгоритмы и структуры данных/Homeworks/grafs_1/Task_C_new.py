import sys
import threading


def find_cycle(smezh_list, v, color):
    color[v] = 1
    for u in smezh_list[v]:
        if color[u] == 0:
            find_cycle(smezh_list, u, color)
        elif color[u] == 1:
            global cycle_flag
            cycle_flag = True
    color[v] = 2

def topology_sort(smezh_list, v, used, result):
    used[v] = True
    for u in smezh_list[v]:
        if not used[u]:
            topology_sort(smezh_list, u, used, result)
    result.append(v)


def main() -> None:
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    smezh_list = [[] for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        a -= 1
        b -= 1
        smezh_list[a].append(b)

    global cycle_flag
    cycle_flag = False
    color = {i: 0 for i in range(n)}
    for v in range(n):
        if color[v] == 0:
            find_cycle(smezh_list, v, color)
            if cycle_flag:
                sys.stdout.write('-1')
                return

    used = {i: False for i in range(n)}
    result = []
    for v in range(n):
        if not used[v]:
            topology_sort(smezh_list, v, used, result)
    for res in reversed(result):
        sys.stdout.write(str(res + 1) + ' ')


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()


