MAX_INT = float("inf")


def minimum_coins_required(arr, n, v):
    table = [MAX_INT] * (v+1)
    table[0] = 0

    for i in range(1, v+1):
        for j in range(n):
            if arr[j] <= i:
                sum_res = table[i-arr[j]]

                table[i] = min(sum_res+1, table[i])

    return table[v]


def minimum_coins_required2(coins, n, v):
    table = [MAX_INT] * (v+1)
    table[0] = 0

    for coin in coins:
        # print coin
        for i in range(coin, v+1):
            # print table
            table[i] = min(table[i], table[i-coin]+1)

    return table[v]

coins = [9, 6, 5, 1]
v = 100
print minimum_coins_required(coins, len(coins), v)
# coins.sort()
print minimum_coins_required2(coins, len(coins), v)