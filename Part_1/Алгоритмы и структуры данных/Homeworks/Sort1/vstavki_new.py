list_lenght = int(input())
raw_list = list(map(int, input().split(' ')))
assert(len(raw_list) == list_lenght)
for i in range(list_lenght):
    j = i
    while (j > 0) and (raw_list[j-1] > raw_list[j]):
        raw_list[j], raw_list[j-1] = raw_list[j-1], raw_list[j]
        j += -1
print(' '.join(list(map(str, raw_list))))
# Различие, чтобы codeforce принял. Случайно не тот файл залил поверх нормального :)
