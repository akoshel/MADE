import sys

def longest_increasing_subsequence(n:int, input_array:list) -> (int, list):
    dp = [[1, None] for _ in range(n)]
    max_length = 1
    max_index = 0
    for i in range(1, n):
        for j in range(i):
            if input_array[i] > input_array[j] and dp[j][0] > dp[i][0] - 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = j
        if dp[i][0] > max_length:
            max_length = dp[i][0]
            max_index = i
    longest_sub = [input_array[max_index]]
    next_index = dp[max_index][1]
    while next_index != None:
        longest_sub = [input_array[next_index]] + longest_sub
        next_index = dp[next_index][1]
    return max_length, longest_sub

def main() -> None:
    n = int(sys.stdin.readline())
    input_array = list(map(int, sys.stdin.readline().split(' ')))
    max_length, longest_sub = longest_increasing_subsequence(n, input_array)
    sys.stdout.write(str(max_length) + '\n')
    for val in longest_sub:
        sys.stdout.write(str(val) + ' ')

if __name__ == '__main__':
    main()