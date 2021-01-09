import sys
import threading


def conn_comps(smezh_list, v, cur, color, cur_len):
    color[v] = cur
    cur_len += 1
    global max_len
    max_len = max(max_len, cur_len)
    for u in smezh_list[v]:
        if color[u] == 0:
            conn_comps(smezh_list, u, cur, color, cur_len)



def main() -> None:
    n = int(sys.stdin.readline())
    i = 1
    user_dict = {}
    user_dict['polycarp'] = 0
    graph_branches = []
    for _ in range(n):
        inp = sys.stdin.readline()
        a, b = inp.split('reposted')
        try:
            user_dict[a.strip().lower()]
        except KeyError:
            user_dict[a.strip().lower()] = i
            i += 1
        try:
            user_dict[b.strip().lower()]
        except KeyError:
            user_dict[b.strip().lower()] = i
            i += 1
        graph_branches.append((user_dict[a.strip().lower()], user_dict[b.strip().lower()]))
    nunique_names = len(user_dict.keys())
    smezh_list = [[] for _ in range(nunique_names)]
    for a, b in graph_branches:
        smezh_list[a].append(b)
        smezh_list[b].append(a)
    global max_len
    max_len = 0
    color = {i: 0 for i in range(n + 1)}
    cnt = 0
    for v in range(n + 1):
        if color[v] == 0:
            cnt += 1
            conn_comps(smezh_list, v, cnt, color, 0)
    sys.stdout.write(str(max_len) + ' ')


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=main)
    thread.start()