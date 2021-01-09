import sys


def zfunction(word):
    left = 0
    right = 0
    n = len(word)
    z = [0 for _ in range(n)]
    z[0] = None
    for i in range(1, n):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < n and word[z[i]] == word[i + z[i]]:
            z[i] += 1
            if i + z[i] > right:
                left = i
                right = i + z[i]
    return z


def main():
    word = sys.stdin.readline().strip()
    ans = [str(a) for a in zfunction(word)[1:]]
    sys.stdout.write(' '.join(ans))


if __name__ == '__main__':
    main()
