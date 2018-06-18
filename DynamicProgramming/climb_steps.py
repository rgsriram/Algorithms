def no_of_steps(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    return no_of_steps(n-1) + no_of_steps(n-2)


def no_of_steps_dp(n):
    s = [0] * (n + 1)
    s[1] = 1
    s[2] = 2

    for i in range(3, n+1):
        s[i] = s[i-1] + s[i-2]

    return s[n]


n = 3

print no_of_steps_dp(n)