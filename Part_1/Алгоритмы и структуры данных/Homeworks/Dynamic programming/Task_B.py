import sys

def turtle(n: int, m: int, coins_map: list) -> (int, str):
    dp =[[[float('-Inf'), None, None] for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][1][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i - 1][j][0] > dp[i][j - 1][0]:
                dp[i][j][0] = dp[i - 1][j][0] + coins_map[i][j]
                dp[i][j][1] = i - 1
                dp[i][j][2] = j
            else:
                dp[i][j][0] = dp[i][j - 1][0] + coins_map[i][j]
                dp[i][j][1] = i
                dp[i][j][2] = j - 1
    best_root = ''
    i = n
    j = m
    i_prev = dp[n][m][1]
    j_prev = dp[n][m][2]
    while i_prev != None:
        if i == i_prev:
            best_root = 'R' + best_root
        else:
            best_root = 'D' + best_root
        i = i_prev
        j = j_prev
        i_prev = dp[i][j][1]
        j_prev = dp[i][j][2]
    max_coins = dp[n][m][0]
    return max_coins, best_root[1:]


def main() -> None:
    n, m = list(map(int, sys.stdin.readline().split(' ')))
    coins_map = [[float('-Inf')] * (m + 1)]
    for _ in range(n):
        coins_map.append([float('-Inf')] + list(map(int, sys.stdin.readline().split(' '))))
    max_coins, best_root = turtle(n, m, coins_map)
    sys.stdout.write(str(max_coins) + '\n')
    sys.stdout.write(best_root + '\n')

if __name__ == '__main__':
    main()


