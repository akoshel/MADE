from random import randint
list_lenght = int(input())
raw_list = list(map(int, input().split(' ')))
assert(len(raw_list) == list_lenght)


def quick_sort_step(input_list, l, r):
    ll = l
    i = l
    hh = r
    x = input_list[l]
    while i <= hh:
        if input_list[i] < x:
            input_list[ll], input_list[i] = input_list[i], input_list[ll]
            ll += 1
            i += 1
        elif input_list[i] > x:
            input_list[i], input_list[hh] = input_list[hh], input_list[i]
            hh -= 1
        else:
            i += 1
    return ll, hh

def quick_sort(init_list, l, r):
    if l < r:
        m = randint(l, r)
        init_list[m], init_list[l] = init_list[l], init_list[m]
        ll, hh = quick_sort_step(init_list, l, r)
        quick_sort(init_list, l, ll - 1)
        quick_sort(init_list, hh + 1, r)

quick_sort(raw_list, 0, len(raw_list)-1)
print(' '.join(list(map(str, raw_list))))
