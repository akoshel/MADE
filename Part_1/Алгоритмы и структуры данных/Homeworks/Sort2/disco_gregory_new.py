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


def count_combinations(gregory_string, m,  cards):
    counter = 0
    cards_dict = count_letters(cards)
    unique_cards = set(cards)
    for i in range(len(gregory_string)):
        j = 0
        try:
            if gregory_string[0] not in unique_cards:
                gregory_string = gregory_string[1:]
            if gregory_string[-1] not in unique_cards:
                gregory_string = gregory_string[:-1]
        except IndexError:
            return counter
        if len(gregory_string) == 0:
            return (counter)
        while j <= min(len(gregory_string), m):
            if gregory_string[j] not in unique_cards:
                gregory_string = gregory_string[j:]
                for n in range(j):
                    counter += n
                break
            j += 1
            break_flag = False
            candidate = gregory_string[:j]
            candidate_dict = count_letters(candidate)
            #print(counter, candidate)
            for letter in candidate_dict.keys():
                if cards_dict[letter] < candidate_dict[letter]:
                    break_flag = True
                    break
            if not break_flag:
                counter += 1
                if j == len(gregory_string):
                    gregory_string = ''
                    print(f'j {j}')
                    for n in range(j):
                        counter += n
                    break

    return(counter)



print(count_combinations(gregory_string, m, cards))
