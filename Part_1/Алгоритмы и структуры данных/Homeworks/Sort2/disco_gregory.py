n, m = list(map(int, input().split(' ')))
gregory_string = input()
cards = input()


def count_letters(cards):
    count_letters_dict = {}
    for letter in cards:
        try:
            count_letters_dict[letter] += 1
        except KeyError:
            count_letters_dict[letter] = 1
    return (count_letters_dict)


def count_combinations(gregory_string, gregory_str_lenght, num_of_cards, cards):
    counter = 0
    cards_dict = count_letters(cards)
    unique_cards = set(cards)
    m = num_of_cards if num_of_cards < gregory_str_lenght else gregory_str_lenght
    for comb_len in reversed(range(1, m + 1)):
        if num_of_cards < comb_len:
            continue
        j = -1
        while j + comb_len + 1 <= gregory_str_lenght:

            if gregory_string[0] not in unique_cards:
                gregory_string = gregory_string[1:]
                gregory_str_lenght -= 1
                continue
            if gregory_string[-1] not in unique_cards:
                gregory_string = gregory_string[:-1]
                gregory_str_lenght -= 1
                continue

            j += 1
            comb_candidate = gregory_string[j: j + comb_len]
            if set(comb_candidate) - unique_cards:
                j += comb_len - 1
                continue
            break_flag = False
            candidate_dict = count_letters(comb_candidate)
            for letter in candidate_dict.keys():
                if cards_dict[letter] < candidate_dict[letter]:
                    break_flag = True
                    break
            if not break_flag:
                if comb_candidate == gregory_string:
                    for n in range(1, comb_len + 1):
                        counter += n
                    return counter
                elif (j + comb_len == gregory_str_lenght):
                    counter += comb_len
                    gregory_string = gregory_string[: -1]
                    gregory_str_lenght -= 1
                elif (j == 0):
                    counter += comb_len
                    gregory_string = gregory_string[1:]
                    gregory_str_lenght -= 1
                    j -= 1
                else:
                    counter += 1
    return counter

print(count_combinations(gregory_string, n, m, cards))
