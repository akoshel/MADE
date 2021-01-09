import sys

DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
OTHER_SYMBOLS = {'+', '-', '*', '/', '(', ')'}
END_EXPRESSION = '.'


class Lexer:
    def __init__(self, word):
        self.word = word
        self.cur = 0
        self.last = False

    def next_token(self):
        symbol = self.word[self.cur]
        if symbol in DIGITS:
            result = ''
            while symbol in DIGITS:
                result += symbol
                self.cur += 1
                symbol = self.word[self.cur]
            self.cur -= 1
        elif symbol in OTHER_SYMBOLS:
            result = symbol
        else:
            self.last = True
            result = ''
        self.cur += 1
        return result


def main():
    word = sys.stdin.readline().strip()
    lexer = Lexer(word)
    while not lexer.last:
        sys.stdout.write(str(lexer.next_token()) + '\n')


if __name__ == '__main__':
    main()
