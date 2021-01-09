import sys

def longest_common_subsequence(input_str1: str, input_str2: str) -> int:
    len_in1 = len(input_str1)
    len_in2 = len(input_str2)
    dp = [[j + 1] + [None for _ in range(len_in2)] for j in range(len_in1)]
    dp = [[i for i in range(len_in2 + 1)]] + dp
    for i in range(1, len_in1 + 1):
        for j in range(1, len_in2 + 1):
            if input_str1[i - 1] == input_str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[len_in1][len_in2]


def main() -> None:
    input_str1 = sys.stdin.readline().strip()
    input_str2 = sys.stdin.readline().strip()
    num_of_operations = longest_common_subsequence(input_str1, input_str2)
    sys.stdout.write(str(num_of_operations) + '\n')

if __name__ == '__main__':
    main()

