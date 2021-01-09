import sys

def longest_common_subsequence(input_str1: str, input_str2: str) -> (list, list):
    len_in1 = len(input_str1)
    len_in2 = len(input_str2)
    dp = [[[float('-Inf'), None, None]] + [[0, None, None] for _ in range(len_in2)] for _ in range(len_in1)]
    dp = [[[float('-Inf'), None, None] for _ in range(len_in2 + 1)]] + dp
    dp[0][1][0] = 0
    for i in range(1, len_in1 + 1):
        for j in range(1, len_in2 + 1):
            if dp[i - 1][j][0] > dp[i][j - 1][0]:
                prev = dp[i - 1][j][0]
                i_prev = i - 1
                j_prev = j
            else:
                prev = dp[i][j - 1][0]
                i_prev = i
                j_prev = j - 1
            if input_str1[i - 1] == input_str2[j - 1]:
                dp[i][j][0] = prev + 1
            else:
                dp[i][j][0] = prev
            dp[i][j][1] = i_prev
            dp[i][j][2] = j_prev
    # составим списки с индексами букв в общей последовательности для обеих строк
    com_ind_str1 = []
    com_ind_str2 = []
    i = len_in1
    j = len_in2
    i_prev = dp[i][j][1]
    j_prev = dp[i][j][2]
    while i_prev != None:
        if dp[i][j][0] > dp[i_prev][j_prev][0]:
            com_ind_str1 = [i - 1] + com_ind_str1
            com_ind_str2 = [j - 1] + com_ind_str2
        i = i_prev
        j = j_prev
        i_prev = dp[i][j][1]
        j_prev = dp[i][j][2]
    return com_ind_str1, com_ind_str2

def count_operations(input_str1: str, input_str2: str, com_ind_str1: list, com_ind_str2: list) -> int:
    operations_cnt = 0
    for i in range(len(com_ind_str1) - 1): # количество операций между внутри общей последовательности
        del_operations = com_ind_str1[i + 1] - com_ind_str1[i] - 1
        insert_operations = com_ind_str2[i + 1] - com_ind_str2[i] - 1
        operations_cnt += max(del_operations, insert_operations)
    operations_cnt += max(com_ind_str1[0], com_ind_str2[0]) # добавляем количество вставок/удалений вначале
    operations_cnt += max((len(input_str1) - com_ind_str1[-1] - 1), (len(input_str2) - com_ind_str2[-1] - 1)) # добавляем количество вставок/удалений в конец
    return min(operations_cnt, max(len(input_str1) - 1, len(input_str2) - 1))

def main() -> None:
    input_str1 = sys.stdin.readline()
    input_str2 = sys.stdin.readline()
    com_ind_str1, com_ind_str2 = longest_common_subsequence(input_str1, input_str2)
    operations_cnt = count_operations(input_str1, input_str2, com_ind_str1, com_ind_str2)
    sys.stdout.write(str(operations_cnt) + '\n')

if __name__ == '__main__':
    main()

