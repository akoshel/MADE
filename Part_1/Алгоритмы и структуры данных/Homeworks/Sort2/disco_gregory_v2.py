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

def count_combinations(gregory_string, cards):
    counter = 0
    cards_dict = count_letters(cards)
    for i in range(len(gregory_string)):
