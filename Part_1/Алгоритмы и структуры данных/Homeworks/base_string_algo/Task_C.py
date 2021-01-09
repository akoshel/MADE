import sys


def pfunction(word):
    n = len(word)
    p = [0 for _ in range(n)]
    for i in range(1, n):
        k = p[i - 1]
        while k > 0 and word[i] != word[k]:
            k = p[k - 1]
        if word[i] == word[k]:
            k += 1
        p[i] = k
    return p


def main():
    pat = sys.stdin.readline().strip()
    word = sys.stdin.readline().strip()
    pat_len = len(pat)
    word_len = len(word)
    answer = []#[0] * word_len
    cnt = 0
    p = pfunction(pat + '#' + word)
    for i in range(word_len):
        if p[pat_len + i + 1] == pat_len:
            answer.append(i - pat_len + 2)
            cnt += 1
    sys.stdout.write(str(cnt) + '\n')
    for ans in answer:
        sys.stdout.write(str(ans) + ' ')
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
