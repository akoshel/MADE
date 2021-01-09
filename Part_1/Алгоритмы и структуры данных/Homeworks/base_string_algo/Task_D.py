import sys

MAX_LEN = 30
ALPHABET_LEN = 26
ORD_A = ord('a')


class Trie:

    def __init__(self):
        self.next = [[-1] * ALPHABET_LEN for _ in range(10**6)]
        self.is_terminal = [False] * (10**5)
        self.size = 1

    def insert(self, s):
        v = 0
        for letter in s:
            si = ord(letter) - ORD_A
            if self.next[v][si] == -1:
                self.next[v][si] = self.size
                self.size += 1
            v = self.next[v][si]
        self.is_terminal[v] = True

    def contains(self, s):
        v = 0
        cnt = 0
        for letter in s:
            cnt += 1
            si = ord(letter) - ORD_A
            if self.next[v][si] == -1:
                return False, cnt
            v = self.next[v][si]
        return True, cnt


def main():
    trie = Trie()
    source_word = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    candidates = []
    for _ in range(n):
        pat = sys.stdin.readline().strip()
        trie.insert(pat)
        candidates.append(pat)
    word_len = len(source_word)
    ans = set()
    set_words = set(candidates)
    for i in range(word_len):
        for j in range(1, min(MAX_LEN + 1, word_len - i + 1)):
            substring = source_word[i: i + j]
            if substring in set_words:
                if trie.contains(substring):
                    ans.add(substring)
    for candidate in candidates:
        if candidate in ans:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
