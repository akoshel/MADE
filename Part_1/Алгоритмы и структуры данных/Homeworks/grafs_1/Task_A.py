import sys

smezh_list = []
for _ in range(100):
    try:
        a, b = list(map(int, sys.stdin.readline().split(' ')))
    except ValueError:
        break
    a -= 1
    b -= 1
    while len(smezh_list) <= max(a, b):
        smezh_list.append([])
    smezh_list[a].append(b)
    smezh_list[b].append(a)

def dfs(smezh_list, v):
    used[v] = True
    for u in smezh_list[v]:
        if not used[u]:
            dfs(smezh_list, u)

sl_lenght = len(smezh_list)
used = {i: False for i in range(sl_lenght)}
for v in range(sl_lenght):
    if not used[v]:
        print(v)
        dfs(smezh_list, v)

