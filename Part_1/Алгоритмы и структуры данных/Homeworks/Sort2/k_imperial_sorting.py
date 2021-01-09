from random import randint

num_of_clones = int(input())
all_clones = list(map(int, input().split(' ')))

def k_stat_step(input_list, l, r):
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

def k_stat(init_list, l, r):
    if l < r:
        m = randint(l, r)
        init_list[m], init_list[l] = init_list[l], init_list[m]
        ll, hh = k_stat_step(init_list, l, r)
        global k
        if k < ll:
            k_stat(init_list, l, ll - 1)
        else:
            k_stat(init_list, hh + 1, r)


for test in range(int(input())):
    test = list(map(int, input().split(' ')))
    i, j, k = [ind - 1 for ind in test] #  List starts from 0, so input indicies decreased on 1
    test_clones = all_clones[i:j+1]
    k_stat(test_clones, 0, j-i)
    print(test_clones[k])





