import sys

class Node:

    def __init__(self):
        self.next = [None] * 26
        self.is_terminal = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, s, node):
        ind = ord(s[0]) - 97
        if node.next[ind] is not None:
            next_node = node.next[ind]
        else:
            next_node = Node()
            node.next[ind] = next_node
        if len(s) == 1:
            next_node.is_terminal = True
        else:
            substring = s[1:]
            self.insert(substring, next_node)

    def contains(self, s, node):
        ind = ord(s[0]) - 97
        if node.next[ind] is None:
            return False
        next_node = node.next[ind]
        if len(s) == 1:
            if next_node.isTerminal:
                return True
            return False
        else:
            substring = s[1:]
            return self.contains(substring, next_node)


def main():
    trie = Trie()
    word = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    len_word = len(word)
    for i in range(len_word):
        for j in range(1, min(30 + 1, len_word - i + 1)):
            substring = word[i: i + j]
            if trie.contains(substring, trie.root):
                set_of_found_words.add(substring)

if __name__ == '__main__':
    main()
