import sys

def kuznechic(n: int, k: int, coins: list) -> (int, int, list):
    dp = [[float('-Inf'), 0] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -1
    for i in range(1, n):
        for j in range(1, min(i, k) + 1):
            dp_candidate = dp[i - j][0] + coins[i - 1]
            if dp_candidate > dp[i][0]:
                dp[i][0] = dp_candidate
                dp[i][1] = i - j
    best_root = [n]
    point = dp[n - 1][1]
    while point >= 0:
        best_root.append(point + 1)
        point = dp[point][1]
    steps_cnt = len(best_root) - 1
    max_coins = dp[n - 1][0]
    best_root.reverse()
    return max_coins, steps_cnt, best_root

def main() -> None:
    n, k = list(map(int, sys.stdin.readline().split(' ')))
    coins = list(map(int, sys.stdin.readline().split(' '))) + [0] # 0 добавил для последнего столбика для удобства
    max_coins, steps_cnt, best_root = kuznechic(n, k, coins)
    sys.stdout.write(str(max_coins) + '\n')
    sys.stdout.write(str(steps_cnt) + '\n')
    for step in best_root:
        sys.stdout.write(str(step) + ' ')

if __name__ == '__main__':
    main()
