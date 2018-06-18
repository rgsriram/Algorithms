def fib(n):

    if n < 0:
        return -1

    if n == 0:
        return 1

    fibo = [0] * (n+1)

    fibo[1] = 1
    sum = fibo[0] + fibo[1]

    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        sum += fibo[i]

    return fibo


def check_sum(n, fibo, minimum_hops_req):
    # print n

    if n < 0:
        return 0

    for i in range(1, len(fibo)):

        if fibo[i] == n:
            return minimum_hops_req

        elif n % fibo[i] == 0:

            if minimum_hops_req == 0:
                minimum_hops_req = n/fibo[i]

            else:
                minimum_hops_req = min(minimum_hops_req, n/fibo[i])

        else:
            _sum = n - fibo[i]
            check_sum(_sum, fibo, minimum_hops_req + 1)

    return minimum_hops_req

n = 7
fibo = fib(n)
minimum_hops_req = 0
print check_sum(n, fibo, minimum_hops_req)