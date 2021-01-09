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


class Parser:
    def __init__(self, lexer):
        self.tokens = []
        self.cur = 0
        while not lexer.last:
            self.tokens.append(lexer.next_token())
        self.size = len(self.tokens)

    def parse(self):
        result = self.parse_operation()
        if self.cur != self.size - 1:
            raise ValueError()
        return result

    def parse_operation(self):
        num1 = self.parse_mult()
        while self.cur < self.size:
            operation = self.tokens[self.cur]
            if operation == '+' or operation == '-':
                self.cur += 1
            else:
                break
            num2 = self.parse_mult()
            if operation == '+':
                num1 += num2
            else:
                num1 -= num2
        return num1

    def parse_mult(self):
        num1 = self.parse_bracket()
        while self.cur < self.size:
            operation = self.tokens[self.cur]
            if operation == '*':
                self.cur += 1
            else:
                break
            num2 = self.parse_bracket()
            num1 *= num2
        return num1

    def parse_bracket(self):
        current_token = self.tokens[self.cur]
        if current_token == '(':
            self.cur += 1
            result = self.parse_operation()
            if self.cur == self.size:
                raise ValueError()
            next_token = self.tokens[self.cur]
            if next_token != ')':
                raise ValueError()
        else:
            result = int(current_token)
        self.cur += 1
        return result


def main():
    word = sys.stdin.readline().strip()
    lexer = Lexer(word)
    parser = Parser(lexer)
    try:
        sys.stdout.write(str(parser.parse()))
    except ValueError:
        sys.stdout.write('WRONG')


if __name__ == '__main__':
    main()
