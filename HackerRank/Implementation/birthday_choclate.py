import sys

"""
5
1 2 1 3 2 
3 2
"""


def solve(n, s, d, m):
    shareable = 0

    for i in range(n - m + 1):
        _sum = s[i]

        for j in range(i + 1, i + m):
            _sum += s[j]

        if _sum == d:
            shareable += 1

    return shareable


n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)