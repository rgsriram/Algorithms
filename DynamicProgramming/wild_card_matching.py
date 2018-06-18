
import sys

input = raw_input()
pattern = raw_input()


def match(input, pattern):
    input_str = input.split()
    pattern_str = pattern.split()

    index = 0
    occured = False

    for i in range(len(pattern_str)-1):
        if pattern_str == '*':
            if occured:
                pattern_str[index] = pattern_str[i]
                occured = False

        else:
            pattern_str[index] = pattern_str[i]
            occured = True

        index += 1

    res = [[0]* len(input_str)] * (index+1)

    if index > 0 and pattern_str[0] == '?':
        res[0][1] = 1

    res[0][0] = 1

    for i in range(1, len(res)-1):
        for j in range(len(res[0]) - 1):
            if pattern_str[j-1] == '?' and input_str[j-1] == pattern_str[j-1]:
                res[i][j] = res[i-1][j-1]

            elif pattern[j-1] == '*':
                res[i][j] = res[i-1][j] or res[i][j-1]

    return res[len(input_str)-1][index]

print match(input, pattern)