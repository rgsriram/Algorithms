def fib(n):

    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)


def fib_dp(n):
    results = [0] * (n+1)

    results[1] = 1
    results[2] = 1

    for i in range(3, n+1):
        results[i] = results[i-1] + results[i-2]

    return results[n]


print fib_dp(20)
